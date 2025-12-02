# Flask application-devops pipeline-project

<img width="600" height="600" alt="devops-logo-png_seeklogo-423085" src="https://github.com/user-attachments/assets/4066dc53-5d32-4819-8d02-861fb4305c01" />


Project overview and description
This is an exclusive project that highlights the processes of automating a an application from building an image to pushing it in dockerhub and running the application. 

**<ins>This is a full DevOps project demonstrating:</ins>**

* Docker containerization

* Automated builds & tests using GitHub Actions

* Pushing Docker images to Docker Hub

* Deployment using Docker Hub images

* Unit testing with PyTest

* A simple Python/Flask application

**Tools&Softwares**

* Flask (simple Python API)

* Docker containerization

* Pytest unit testing

* GitHub Actions CI/CD Pipeline

* Automatic build & push to Docker Hub

* Deployment using Docker Hub image

**Steps for project execution**
  --
1. The various files and folders were created in vscode together with their required configuration
2. The files and folders were committed with the command  "git init".
3. The commited files were staged and added to the repository

4.**Github secrets configuraiton**

GitHub Repo → Settings → Secrets and Variables → Actions → New Repository Secret

<img width="468" height="282" alt="image" src="https://github.com/user-attachments/assets/9980a5d8-10a5-4dea-bbb1-9fca8487c853" />

5. **Dockerhub secret and configuration**

The secret token generated in dockerhub and integrated into the new repository secret in github. In this case the image created is directly
pushed into dockerhub from github directly.

6.  **folder structure**

* devops-pipeline-project/
│── flaskapp/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── tests/
│       └── test_app.py
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
└── README.md



7.  **Docker setup commands used for the project**
   
    - Highlighting the repository name of the image is very important in the docker tag

    <img width="468" height="59" alt="image" src="https://github.com/user-attachments/assets/14572f08-9047-4573-8628-e9952ac01ca5" />

    - Building the image from the current directory  - docker build -t flask-app .
    - Running the container - docker run -p 5000:5000 flask-app

**Errors encountered during Project execution**
--

1. First challenges encountered was when the dockerfile directory could not be identified in github actions.
2. Docker build having issues with the build process

   **<img width="468" height="191" alt="image" src="https://github.com/user-attachments/assets/73404192-e0f7-412d-8f28-2c6e74abe71d" />**



2.1 Docker image build problem has been fixed. This was done perfectly by rectifying isses with the requirements.txt after which we updated the ci.yml file.

  <img width="468" height="176" alt="image" src="https://github.com/user-attachments/assets/52d3eead-9715-4a03-8c57-53813ed2aab7" />

2.2  Having issues with the build process stating unauthorized or insufficient scopes within the build process. The read and write option is very important during the create access token process. 

  <img width="468" height="215" alt="image" src="https://github.com/user-attachments/assets/1ed3870e-2dc4-4088-a9af-c25c75d48d3c" />

2.1 Exiting due to SVC_UNREACHABLE: service not available: no running pod for service flaskapp-service found : That error means your Service is running but there are zero running Pods matching the Service selector, so Kubernetes has nothing to       route traffic to. This shows that our pods exist but are service is not conneected to the points the image below is an example of the error we encounter during that process

  -<img width="468" height="40" alt="image" src="https://github.com/user-attachments/assets/e91e94e4-c218-4e87-a96c-d285bde5df93" />

    As part of getting the problem solved we check the pods showing the labels And we add extra details with the following commands

      <img width="468" height="107" alt="image" src="https://github.com/user-attachments/assets/0c3470b3-f14e-4555-878d-a9e11344f45c" />

  
**DEPLOYMENT OF PROJECT USING KUBERNETES**
  --
  MINIKUBE:
  --
  •	Minikube is a tool that allows users to run a single-node Kubernetes cluster locally on their personal computer (Windows, macOS, or Linux).
  •	It simplifies the process of setting up a local Kubernetes environment for development, testing, and learning purposes, eliminating the need for a complex multi-node setup.
  •	Minikube provides the underlying infrastructure for a local Kubernetes cluster, typically within a virtual machine.

  KUBECTL:
  --
  •	Kubectl is the official command-line interface (CLI) tool for interacting with Kubernetes clusters, regardless of where they are running (local Minikube, cloud provider, on-premises).
  •	It is used to deploy and manage applications, inspect and manage cluster resources, and perform various administrative tasks within a Kubernetes cluster.
  •	Kubectl commands communicate with the Kubernetes API server to create, update, delete, and retrieve information about Kubernetes objects like Pods, Deployments, Services, etc. 

  
1. **Start Kubernetes Cluster (Minikube)**

    •	Minikube start
    •	Kubectl get nodes

<img width="468" height="144" alt="image" src="https://github.com/user-attachments/assets/d5f1dd65-3fcf-4125-a693-f6bebddc4151" />

  Cluster has been started

2. **Kubernetes deployment file – deployment.yaml**

  <img width="468" height="199" alt="image" src="https://github.com/user-attachments/assets/99d9a0a6-9f8b-4f98-85c6-338077d59c74" />

3. Create a service.yaml
   
  * kubectl apply -f k8s/deployment.yaml
  * kubectl  apply -f k8s/service.yaml
    
  Running applications seen in the image below
  
  <img width="468" height="45" alt="image" src="https://github.com/user-attachments/assets/f1139243-c7da-4e0f-bfbf-28e3136e2ab8" />



**This project demonstrates:**

* CI/CD with GitHub Actions

* Docker image building & optimization

* Automated testing pipeline

* Secure secrets management

* Pushing images to Docker Hub

* Container-based deployment

Python Flask microservice architecture

**Technology Stack**

* Python Flask – Application framework

* Pytest – Unit testing

* Docker – Containerization

* Docker Hub – Image registry

* GitHub Actions – CI/CD workflow

* GitHub Secrets – Secure credentials







