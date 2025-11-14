pipeline {
    agent any
    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/22071a05a7-pixel/Student-Management-System.git'
            }
        }

        stage('Build') {
            steps {
                sh 'docker build -t student-app .'
            }
        }
        stage('Test') {
            steps {
                sh 'python manage.py test'
            }
        }
    }
}
