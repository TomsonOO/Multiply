pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/TomsonOO/Multiply.git'
            }
        }
        stage('Build') {
            steps {
                sh 'docker build -t my-python-app .'
            }
        }
        stage('Test') {
            steps {
                // This will run the CMD from the Dockerfile
                sh 'docker run --rm my-python-app'
            }
        }
        stage('Cleanup') {
            steps {
                sh 'docker rmi my-python-app'
            }
        }
    }
}
