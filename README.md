argo-cd-kubernetes-pipeline

Utilizing Argo CD and Argo Rollout for advanced deployment strategies in Kubernetes environment.

### Task 1: Setup and Configuration

- Created a basic REST API in FAST API with 2 versions 0.1.0, 0.2.0 and pushed them to docker.io.

- Set up Argo CD and Argo Rollout in Minikube running on WSL2 Ubuntu on Windows. The link to documentation - [Argo CD getting started](https://argo-cd.readthedocs.io/en/stable/getting_started/) [Argo Rollout getting started](https://argo-rollouts.readthedocs.io/en/stable/installation/)

### Task 2: Creating a GitOps pipeline

- Dockerized the two different versions of applications and pushed them to my Docker Hub repo [Docker repo link](https://hub.docker.com/repository/docker/chahatsagarmain/app/general)

- Created a deployment and service file in the dev namespace for testing the deployment of the application using the Docker images pushed to the Docker Hub repository.

- Created an Argo CD application YAML file to monitor and sync the changes on the GitHub repository of the project in the dev path.

- Tested the application and made sure the service is accessible at the node port using `minikube service app-service -n dev`

### Task 3: Implementing Canary Release with Argo Rollouts

- Created a rollout YAML with canary deployment strategy and application configuration.

- Deployed a rollout for app version 0.1.0 and monitored the deployment of rollout using Argo CD dashboard and CLI.

- Reconfigured the rollout YAML to deploy the image of version 0.2.0 and pushed it to the GitHub repository.

- Monitored the deployment of the new version using Argo Rollout dashboard.

![Screenshot 2024-04-02 153418](https://github.com/chahatsagarmain/argo-cd-kubernetes-pipeline/assets/109112505/025393b9-260f-4bf5-b7b7-75638268934c)
![Screenshot 2024-04-02 154655](https://github.com/chahatsagarmain/argo-cd-kubernetes-pipeline/assets/109112505/479de145-e2d6-4611-be45-4ab456339692)
![Screenshot 2024-04-02 185508](https://github.com/chahatsagarmain/argo-cd-kubernetes-pipeline/assets/109112505/e1a67e58-bbba-4943-a426-f125c619eee8)

- The 0.2.0 version of API has an extra route /new , This verifies our application is accessible and updated after the deployement !

### Task 4: Clean Up

- Deleting the rollout from the canary namespace `kubectl delete rollout app-rollout -n canary`

- Check the services in the namespace `kubectl get service -n canary`

- Delete the service in the namespace `kubectl delete service app-service -n canary`

- Deleting the namespace `kubectl delete ns canary`

- I didn't create an ingress service but used Minikube service to directly access the service at the node port from Minikube's IP

### Experience

- The assignment had well-defined steps and could be easily followed from documentation. It was my first time using a CD on Kubernetes, but I learned a lot from this assignment.

## Thank You!
