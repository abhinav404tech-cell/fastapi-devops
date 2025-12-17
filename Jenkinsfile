pipeline {
    agent any

    parameters {
        booleanParam(
            name: 'RUN_BUILD',
            defaultValue: true,
            description: 'Run the build stage'
        )
        choice(
            name: 'ENV',
            choices: ['dev', 'qa', 'prod'],
            description: 'Select environment to build and push image'
        )
        }

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

        stage('Set Environment Config') {
            
            steps {
                script {
                    if (params.ENV == 'dev') {
                        // env.AWS_ACCOUNT_ID = '111111111111'
                        // env.ECR_REPO = 'fastapi-devops-dev'
                        echo "Building for environment: ${params.ENV}"
                        echo "Building for RUN_BUILD: ${params.RUN_BUILD}"
                    } else if (params.ENV == 'qa') {
                        // env.AWS_ACCOUNT_ID = '222222222222'
                        // env.ECR_REPO = 'fastapi-devops-qa'
                        echo "Building for environment: ${params.ENV}"
                        echo "Building for RUN_BUILD: ${params.RUN_BUILD}"
                    } else {
                        echo "Building for environment: ${params.ENV}"
                        echo "Building for RUN_BUILD: ${params.RUN_BUILD}"
                        // env.AWS_ACCOUNT_ID = '333333333333'
                        // env.ECR_REPO = 'fastapi-devops-prod'
                    }

                    // env.ECR_URI = "${env.AWS_ACCOUNT_ID}.dkr.ecr.${env.AWS_REGION}.amazonaws.com/${env.ECR_REPO}"
                }
            }
        }
        // stage('Build Docker Image') {
        //     steps {
        //         bat """
        //         docker build -t %ECR_REPO%:%IMAGE_TAG% .              
        //         """
        //     }
        // }
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

                    aws sts get-caller-identity

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
