pipeline {
     agent any

    stages {
        stage('Setup') {
            steps {
                script {
                    // open to the project directory
                    sh 'cd app'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run tests using pytest inside the app directory
                    sh "pytest"
                }
            }
        }
    }
}
