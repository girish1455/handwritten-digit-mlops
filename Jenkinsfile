pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git 'https://github.com/girish1455/handwritten_digit_mlops_project.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
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
                bat 'docker run -d -p 8000:8000 digit-api'
            }
        }

    }
}