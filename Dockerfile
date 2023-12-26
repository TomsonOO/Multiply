pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Replace 'your-git-repo-url' with the actual URL of your Git repository
                git 'your-git-repo-url'
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
                sh 'docker run --rm my-python-app'
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
