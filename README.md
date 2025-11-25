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


**Docker setup commands used for the project**
- Building the image from the current directory  - docker build -t flask-app .
- Running the container - docker run -p 5000:5000 flask-app

**Steps for project execution**







**Errors encountered during steps**
1. First challenges encountered was when the dockerfile directory could not be identified in github actions.
2. Docker build having issues with the build process

   **<img width="468" height="191" alt="image" src="https://github.com/user-attachments/assets/73404192-e0f7-412d-8f28-2c6e74abe71d" />**

2.1 Docker image build problem has been fixed. This was done perfectly by rectifying isses with the requirements.txt after which we updated the ci.yml file.

  <img width="468" height="176" alt="image" src="https://github.com/user-attachments/assets/52d3eead-9715-4a03-8c57-53813ed2aab7" />



**This project demonstrates:**

CI/CD with GitHub Actions

Docker image building & optimization

Automated testing pipeline

Secure secrets management

Pushing images to Docker Hub

Container-based deployment

Python Flask microservice architecture





