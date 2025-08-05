pipeline {
     agent {
        docker {
            image 'python:3.9'
            args '-v /tmp:/tmp'   // optional
        }
    }

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Setup') {
            steps {
                script {
                    // Create a virtual environment and install dependencies
                    sh "python3 -m venv ${VENV_DIR}"
                    sh ". ${VENV_DIR}/bin/activate && ${VENV_DIR}/bin/pip install -r requirements.txt"
                
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run tests using pytest inside the app directory
                    sh ". ${VENV_DIR}/bin/activate && cd app && pytest"
                }
            }
        }
    }
}
