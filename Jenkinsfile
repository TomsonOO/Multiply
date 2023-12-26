pipeline {
    agent any

    environment {
        // Define environment variables if needed
        DOCKER_IMAGE = 'my-python-app'
    }

    stages {
        stage('Checkout') {
            steps {
                // Checks out the source code from Git repository
                checkout scm
            }
        }
        stage('Build') {
            steps {
                // Builds a Docker image from your Dockerfile
                script {
                    docker.build("$DOCKER_IMAGE")
                }
            }
        }
        stage('Test') {
            steps {
                // Runs tests inside the Docker container
                script {
                    docker.run("--rm $DOCKER_IMAGE python -m unittest discover")
                }
            }
        }
        stage('Cleanup') {
            steps {
                // Optional: Clean up Docker images
                script {
                    sh "docker rmi $DOCKER_IMAGE"
                }
            }
        }
    }
}
