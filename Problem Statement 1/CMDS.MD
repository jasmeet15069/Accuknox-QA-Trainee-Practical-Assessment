docker 

docker build -t wisecow-app:01 .

docker run -d -p 4499:4499 wisecow-app:01

choco install minikube

minikube start

kubectl apply -f wisecow-deployment.yaml

kubectl apply -f wisecow-service.yaml

kubectl get pods

kubectl get services

minikube ip

kubectl logs <pod-name>

# for handling traffic 
kubectl scale deployment wisecow-deployment --replicas=3

# all the process done locally



