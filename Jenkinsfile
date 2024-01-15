pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = 'docker.io/nabinchoudhary342/python-flask-app1'
        KUBE_DEPLOYMENT_FILE = 'kubernetes/deployment.yaml'
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    // Clone the GitHub repository and switch to the develop branch
                    checkout([$class: 'GitSCM', branches: [[name: '*/develop']], userRemoteConfigs: [[url: 'https://github.com/ChoudharyNabin/python-flask-app1.git']]])
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    sh "docker build -t $DOCKER_IMAGE_NAME ."
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    // Push the Docker image to your Docker repository
                    sh "docker push $DOCKER_IMAGE_NAME"
                }
            }
        }

        stage('Deploy to Minikube') {
            steps {
                script {
                    // Deploy the application to Minikube using kubectl
                    sh "kubectl apply -f $KUBE_DEPLOYMENT_FILE"
                }
            }
        }
    }
}