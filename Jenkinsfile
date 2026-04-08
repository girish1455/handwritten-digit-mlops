pipeline {
    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\giris\\miniconda3\\python.exe" -m pip install --upgrade pip'
                bat '"C:\\Users\\giris\\miniconda3\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Train Model') {
            steps {
                bat '"C:\\Users\\giris\\miniconda3\\python.exe" src\\train.py'
            }
        }

        stage('Run Tests') {
            steps {
                bat '"C:\\Users\\giris\\miniconda3\\python.exe" src\\test_model.py'
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