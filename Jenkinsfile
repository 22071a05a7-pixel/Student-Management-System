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
        stage('Setup') {
            steps {
                echo '🚀 Starting Jenkins Pipeline...'
                git branch: 'main', url: 'https://github.com/22071a05a7-pixel/Student-Management-System.git'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                echo '🐳 Building Docker image...'
                bat 'docker build -t student-app .'
                bat 'docker images student-app'
            }
        }
        
        stage('Run Tests') {
            steps {
                echo '🧪 Running test suite...'
                bat 'docker run --rm student-app python manage.py test --verbosity=2'
            }
        }
        
        stage('Verify Web App') {
            steps {
                echo '🌐 Testing web application startup...'
                script {
                    bat 'docker run -d --name web-test student-app'
                    bat 'timeout /t 10 /nobreak'
                    bat 'docker logs web-test'
                    bat 'docker stop web-test'
                    bat 'docker rm web-test'
                }
            }
        }
    }
    
    post {
        always {
            echo '📊 Pipeline execution completed'
        }
        success {
            echo '🎉 SUCCESS: All tests passed!'
            echo '💡 To run locally: docker run -p 8000:8000 student-app'
            echo '🌐 Then visit: http://localhost:8000/api/students/page/'
        }
    }
}