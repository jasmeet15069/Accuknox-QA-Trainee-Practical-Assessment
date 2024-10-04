
# Assignment: Deploying Wisecow Application on Kubernetes

## 1. **Introduction**
   - Brief overview of Kubernetes and its significance in container orchestration.
   - Introduction to the Wisecow application and its purpose.

## 2. **Prerequisites**
   - List of software and tools required:
     - Minikube
     - Docker
     - kubectl
     - Git Bash (or preferred terminal)

## 3. **Setting Up the Environment**
   - Instructions to install Minikube and Docker.
   - How to start Minikube:
     ```bash
     minikube start
     ```
   - Setting up Docker environment:
     ```bash
     eval $(minikube docker-env)
     ```

## 4. **Building the Docker Image**
   - Create a Dockerfile for the Wisecow application:
     ```dockerfile
     FROM ubuntu:20.04
     RUN apt-get update && \
         apt-get install -y cowsay fortune netcat && \
         rm -rf /var/lib/apt/lists/* 
     COPY wisecow.sh /usr/local/bin/wisecow.sh
     ENTRYPOINT ["/usr/local/bin/wisecow.sh"]
     ```
   - Build the Docker image:
     ```bash
     docker build -t wisecow-app:01 .
     ```

## 5. **Creating Kubernetes Manifests**
   - **Deployment Manifest (wisecow-deployment.yaml)**:
     ```yaml
     apiVersion: apps/v1
     kind: Deployment
     metadata:
       name: wisecow-deployment
     spec:
       replicas: 2
       selector:
         matchLabels:
           app: wisecow
       template:
         metadata:
           labels:
             app: wisecow
         spec:
           containers:
           - name: wisecow-container
             image: wisecow-app:01
             ports:
             - containerPort: 4499
     ```

   - **Service Manifest (wisecow-service.yaml)**:
     ```yaml
     apiVersion: v1
     kind: Service
     metadata:
       name: wisecow-service
     spec:
       type: NodePort
       ports:
       - port: 4499
         targetPort: 4499
         nodePort: 30000
       selector:
         app: wisecow
     ```

## 6. **Deploying the Application**
   - Apply the manifests to create the deployment and service:
     ```bash
     kubectl apply -f wisecow-deployment.yaml
     kubectl apply -f wisecow-service.yaml
     ```

## 7. **Verifying Deployment**
   - Check the status of deployments and pods:
     ```bash
     kubectl get deployments
     kubectl get pods
     ```

## 8. **Accessing the Application**
   - Retrieve Minikube IP:
     ```bash
     minikube ip
     ```
   - Access the application using:
     ```
     http://<minikube-ip>:30000/
     ```

## 9. **Troubleshooting**
   - Common issues faced during deployment:
     - **ImagePullBackOff**: Ensure the image exists in Minikube's Docker environment.
     - **CrashLoopBackOff**: Check logs for application errors:
       ```bash
       kubectl logs <pod-name>
       ```

## 10. **Scaling the Application**
   - Instructions to scale the deployment:
     ```bash
     kubectl scale deployment wisecow-deployment --replicas=3
     ```

## 11. **Conclusion**
   - Recap of what was accomplished.
   - Potential next steps or improvements.

## 12. **References**
   - Links to relevant documentation for Kubernetes, Docker, and Minikube.
