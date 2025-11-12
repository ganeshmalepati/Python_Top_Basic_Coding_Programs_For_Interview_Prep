pipeline {
    agent any

    environment {
        REPO_URL = 'https://github.com/ganeshmalepati/Basic_Ten_Code.git'
    }

    stages {
        stage("Cloning Git Repository") {
            steps {
                // Automatically use the branch Jenkins is building
                git branch: "${env.BRANCH_NAME}", url: "${REPO_URL}"
            }
        }

        stage("Build Docker Image") {
            steps {
                sh "docker build -t basic-code-snippet-job ."
            }
        }

        stage("Run Docker Container for Python Codes") {
            steps {
                sh "docker run --rm basic-code-snippet-job"
            }
        }
    }

    post {
        always {
            echo "Pipeline completed for branch: ${env.BRANCH_NAME}"
        }
    }
}
