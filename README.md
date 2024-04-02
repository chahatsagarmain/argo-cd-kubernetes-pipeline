 argo-cd-kubernetes-pipeline

Utilzing Argo CD and Argo rollout for advanced deployment strategies in Kubernets  enviroment . 

###  Task 1 : Setup and Configuration 

 - Created a basic REST API in FAST API with 2 verions 0.1.0 , 0.2.0
   and pushed them to docker.io . 
 - Setup Argo CD and Argo Rollout in minikube running on WSL2  ubuntu on windows . The link to documentation - [Argo CD getting started](https://argo-cd.readthedocs.io/en/stable/getting_started/) [Argo rollout getting started](https://argo-rollouts.readthedocs.io/en/stable/installation/)
   
### Task 2 : Creating a GitOps pipeline 
 - Dockerized the two different versions of applications and pushed on
   my Docker Hub repo [Docker repo link ](https://hub.docker.com/repository/docker/chahatsagarmain/app/general)
 - Created a deployment and service file in dev namespace for testing
   the deployment of the application using the docker images pushed to
   the docker hub repository .
   
 - Created Argo CD application yaml file to monitor the and sync the
   changes on the github repository of the project in dev path .
   
 - Tested the application and made sure the service is accessible at the
   nodeport  using

minikube service app-service -n dev 

### Task 3 : Implementing Canary Release with Argo Rollouts 

 - Created rollout yaml with canary deployment strategy and application
   configuration .
 
 - Deployed a rollout for app version 0.1.0 and monitored the deployment
   of rollout using argo cd dashbaord and cli .
 
 - Reconfigured the rollout yaml to deploy the image of version 0.2.0
   and pushed it on github repository. 
 
 - Monitored the deployment of new version using argo rollout dashboard .
 -
