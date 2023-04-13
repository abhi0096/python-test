pipeline {
    agent any
    stages {

        stage('Clone') {
            steps {
                // Get some code from a GitHub repository
                git branch: 'main', credentialsId: 'office-git-creds', url: 'https://git.rezo.ai/abhishek.khandelwal/script.py.git'
            }
        }

        stage('Run Python Script') {
            steps {
                sh 'python3 script.py'
            }
        }
    }
}
