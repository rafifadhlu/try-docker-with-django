pipeline {
     agent any

    stages {
        stage('Setup') {
            steps {
                script {
                    // Open the app and install dependencies
                    sh "cd app && pip install -r requirements.txt"
                                    
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run tests using pytest inside the app directory
                    sh "cd app && pytest"
                }
            }
        }
    }
}
