pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Setup') {
            steps {
                script {
                    docker.image('python:3.10').inside {
                        sh '''
                            python3 -m venv venv
                            source venv/bin/activate
                            python --version
                        '''
                    }
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
