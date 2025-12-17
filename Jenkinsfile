pipeline {
    agent any

    environment {
        AWS_REGION = 'us-east-1'
        AWS_ACCOUNT_ID = '335660922529'
        ECR_REPO = 'fastapi-devops'
        IMAGE_TAG = "${BUILD_NUMBER}"
        ECR_URI = "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${ECR_REPO}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build Docker Image') {
            steps {
                bat """
                docker build -t %ECR_REPO%:%IMAGE_TAG%                
                """
            }
        }
        stage('Login to AWS ECR') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'aws-creds',
                    usernameVariable: 'AWS_ACCESS_KEY_ID',
                    passwordVariable: 'AWS_SECRET_ACCESS_KEY'
                )]) {
                    bat """
                    aws configure set aws_access_key_id %AWS_ACCESS_KEY_ID%
                    aws configure set aws_secret_access_key %AWS_SECRET_ACCESS_KEY%
                    aws configure set region %AWS_REGION%

                    aws ecr get-login-password --region %AWS_REGION% ^
                    | docker login --username AWS --password-stdin %AWS_ACCOUNT_ID%.dkr.ecr.%AWS_REGION%.amazonaws.com
                    """
                }
            }
        }

        stage('Push Image to ECR') {
            steps {
                bat """
                docker push %ECR_URI%:%IMAGE_TAG%
                """
            }
        }

        stage('Verify') {
            steps {
                bat 'dir'
            }
        }
    }
}
