pipeline {
    agent any
    
    stages {
        stage("Cloning Git Repository"){
            steps {
                checkout scm
            }
        }
        stage("Build Docker Image"){
            steps {
                script {
                    dockerImage = docker.Build("my-jenkins-tencode-app")
                }
            }
        }
        stage("Run Docker Container for python codes"){
            steps {
                script {
                    dockerImage.run("-d")
                }
            }
        }
    }

    post {
        always {
            echo "Pipeline has been successfully completed"
        }
    }
}
