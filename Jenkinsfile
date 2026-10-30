pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out source code from GitHub...'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                bat 'python -m pip install --default-timeout=300 --retries 5 -r requirements.txt'
            }
        }

        stage('Run Application') {
            steps {
                echo 'Running application...'
                bat 'python app\\hello.py'
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running pytest...'
                bat 'python -m pytest -v'
            }
        }

        stage('Evidently Monitoring') {
            steps {
                echo 'Running Evidently monitoring...'
                bat 'python monitoring\\monitor.py'
            }
        }
    }

    post {
        success {
            echo 'UAT DRY RUN SUCCESSFUL'
        }

        failure {
            echo 'UAT DRY RUN FAILED'
        }
    }
}