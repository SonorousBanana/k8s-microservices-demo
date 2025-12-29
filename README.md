This repository: if you want to test the service in docker env: 

docker create network

#in ./service run the commands below

#to build the images local
docker build -t my-api:latest ./api
docker build -t my-frontend:latest

#to run the images in docker in the same network
docker run -d --name frontend -p 8080:80 --network my-network my-api:latest
docker run -d --name frontend -p 8080:80 --network my-network my-frontend:latest

in terminal rum:
minikube image load my-api:latest
minikube image load my-frontend:latest

kubectl apply all in service/base folder

port-forward service/frontend 30080:80 -n monitoring-platform
http://localhost:30080

