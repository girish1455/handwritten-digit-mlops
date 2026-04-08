pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install --upgrade pip'
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Train Model') {
            steps {
                bat 'python src/train.py'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python src/test_model.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t digit-api .'
            }
        }

        stage('Run API Container') {
            steps {
                bat 'docker rm -f digit-container || exit 0'
                bat 'docker run -d -p 8000:8000 --name digit-container digit-api'
            }
        }

    }
}