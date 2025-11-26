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
        
        // stage('Install Dependencies') {
        //     steps {
        //         echo '📦 Installing dependencies...'
        //         sh 'pip install -r requirements.txt'
        //     }
        // }
        
        stage('Run Tests') {
            steps {
                echo '🧪 Running tests...'
                sh 'python manage.py test'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                echo '🐳 Building Docker image...'
                sh 'docker build -t student-app .'
            }
        }
    }
    
    post {
        always {
            echo '📊 Pipeline completed!'
        }
        success {
            echo '🎉 SUCCESS: All stages passed!'
        }
        failure {
            echo '❌ FAILED: Pipeline has errors'
        }
    }
}
