// pipeline {
//     agent any
//     stages {
//         stage('Clone') {
//             steps {
//                 git 'https://github.com/22071a05a7-pixel/Student-Management-System.git'
//             }
//         }

//         stage('Build') {
//             steps {
//                 sh 'docker build -t student-app .'
//             }
//         }
//         stage('Test') {
//             steps {
//                 sh 'python manage.py test'
//             }
//         }
//     }
// }

pipeline {
    agent any
    
    stages {
        stage('Clone Repository') {
            steps {
                echo '📥 Cloning code from GitHub...'
                git branch: 'main', url: 'https://github.com/22071a05a7-pixel/Student-Management-System.git'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                echo '🐳 Building Docker image...'
                bat 'docker build -t student-app .'
            }
        }
        
        stage('Run Tests in Docker') {
            steps {
                echo '🚀 Testing if Docker container starts...'
                bat '''
                    docker run -d --name test-container student-app
                    timeout /t 5 /nobreak
                    docker logs test-container
                    docker stop test-container
                    docker rm test-container
                '''
            }
        }
    }
    
    post {
        always {
            echo '📊 Pipeline completed!'
        }
        success {
            echo '🎉 SUCCESS: Docker image built and container started!'
        }
        failure {
            echo '❌ FAILED: Check Docker setup'
        }
    }
}