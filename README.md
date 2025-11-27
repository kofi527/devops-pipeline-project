# Flask application-devops pipeline-project

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
* The various files and folders were created in vscode together with their required configuration
* The files and folders were committed with the command  "git init".
* The commited files were staged and added to the repository

**Github secrets configuraiton**
GitHub Repo → Settings → Secrets and Variables → Actions → New Repository Secret

**Dockerhub secret and configuration**
The secret token generated in dockerhub and integrated into the new repository secret in github. In this case the image created is directly
pushed into dockerhub from github directly.



**folder structure**

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



**Docker setup commands used for the project**
- Highlighting the repository name of the image is very important in the docker tag
- 
  <img width="468" height="59" alt="image" src="https://github.com/user-attachments/assets/14572f08-9047-4573-8628-e9952ac01ca5" />

- Building the image from the current directory  - docker build -t flask-app .
- Running the container - docker run -p 5000:5000 flask-app

**Errors encountered during steps**
1. First challenges encountered was when the dockerfile directory could not be identified in github actions.
2. Docker build having issues with the build process

   **<img width="468" height="191" alt="image" src="https://github.com/user-attachments/assets/73404192-e0f7-412d-8f28-2c6e74abe71d" />**

2.1 Docker image build problem has been fixed. This was done perfectly by rectifying isses with the requirements.txt after which we updated the ci.yml file.

  <img width="468" height="176" alt="image" src="https://github.com/user-attachments/assets/52d3eead-9715-4a03-8c57-53813ed2aab7" />



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





