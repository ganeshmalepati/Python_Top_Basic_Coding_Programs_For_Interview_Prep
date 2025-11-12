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
                sh "docker build -t Basic_Code_Snippet_job:${env.BRANCH_NAME} ."
            }
        }

        stage("Run Docker Container for Python Codes") {
            steps {
                sh "docker run --rm password-pipeline-job:${env.BRANCH_NAME}"
            }
        }
    }

    post {
        always {
            echo "Pipeline completed for branch: ${env.BRANCH_NAME}"
        }
    }
}
