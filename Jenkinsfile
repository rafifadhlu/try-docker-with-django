pipeline{
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from the repository
                checkout scm
            }
        }

        stage('Setup') {
            steps {
                script {
                    // Create a virtual environment and install dependencies
                    sh "python3 -m venv ${VENV_DIR}"
                    sh "source ${VENV_DIR}/bin/activate"
                    sh "${VENV_DIR}/bin/pip install -r requirements.txt"
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    // Run tests using pytest
                    sh "cd app"
                    sh "pytest"
                }
            }
        }
    }
}