# Mini Fullstack Dashboard

This repository contains a **mini fullstack application** with a frontend, an API backend, and Kubernetes manifests. You can run it either locally using Docker or on Minikube/Kubernetes.

---

## Table of Contents

- [Project Structure](#project-structure)  
- [Run with Docker](#run-with-docker)  
- [Run with Minikube / Kubernetes](#run-with-minikube--kubernetes)  
- [Access the Dashboard](#access-the-dashboard)

---

## Project Structure
```
services/
├── api/
│ ├── Dockerfile
│ ├── app.py
│ └── requirements.txt
├── frontend/
│ ├── Dockerfile
│ ├── index.html
│ ├── style.css
│ └── app.js
k8s/
├── base/
│ ├── namespace.yml
│ ├── api-deployment.yml
│ ├── api-service.yml
│ ├── ingress.yml
│ ├── dashboard-deployment.yml
│ └── dashboard-service.yml
```

---

## Run with Docker

1. **Create a Docker network**:

```bash
docker network create my-network

docker build -t my-api:latest ./services/api
docker build -t my-frontend:latest ./services/frontend

docker run -d --name api -p 5000:5000 --network my-network my-api:latest
docker run -d --name frontend -p 8080:80 --network my-network my-frontend:latest

```
2. **Download and run minikube**:

search in dockerhub for minikube and pull the image. after that run

```bash
minikube start --driver=docker
```
---

## Run with Minikube / Kubernetes

1. **Load the images from docker in minikube**:

```bash
minikube image load my-api:latest
minikube image load my-frontend:latest
```

2. **Apply kubernetes manifests**:

first create a namespace for your project

#check kubectl commands by running "kubectl" in termila

```bash
kubectl apply -f ./k8s/base/namespace.yaml -n "monitoring-platform"
```

apply deployments and services for each image you tested in docker before

```bash
kubectl apply -f ./k8s/base/api-deployment.yaml -n "monitoring-platform"
kubectl apply -f ./k8s/base/dashboard-deployment.yaml -n "monitoring-platform"
kubectl apply -f ./k8s/base/api-service.yaml -n "monitoring-platform"
kubectl apply -f ./k8s/base/dashboard-deployment.yaml -n "monitoring-platform"
```
---


3. **Ingress**:
```bash
minikube addons enable ingress
```
copy and paste 

```bash
127.0.0.1 dashboard.local
``` 
in "hosts" file with admin privileges.

run in PS:

```bash
minikube tunnel
``` 
## Access the Dashboard

http://dashboard.local/

