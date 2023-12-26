pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Replace 'your-git-repo-url' with the actual URL of your Git repository
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
                // Run the Docker container which will execute the tests
                sh 'docker run --rm my-python-app python -m unittest discover -v'
            }
        }
        stage('Cleanup') {
            steps {
                // Clean up the built Docker image to save space
                sh 'docker rmi my-python-app'
            }
        }
    }
}