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
│ ├── namespace.yaml
│ ├── api-deployment.yaml
│ ├── api-service.yaml
│ ├── dashboard-deployment.yaml
│ └── dashboard-service.yaml
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

## Run with Kubernetes

1. **Load the images from docker in minikube**:

```bash
minikube image load my-api:latest
minikube image load my-frontend:latest
```

2. **Ingress**:
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

3. **Apply kubernetes manifests usin Helm**:

first create a namespace for your project

#check kubectl commands by running "kubectl" in termila

```bash
kubectl apply -f ./k8s/base/namespace.yaml -n "monitoring-platform"
```
download helm. Save the helm.exe it in a folder "C:\tools" and define the variable in system variables. After run "helm version" to confirm that it is already run.

go to folder "chart" and run

```bash
helm template .
```
This command will show you if your template is it correct.

Finaly, run:
```bash
helm install chart . -n monitoring-platform 
```
It is DONE!!!
---

## Access the Dashboard
search in your browser: http://dashboard.local/

