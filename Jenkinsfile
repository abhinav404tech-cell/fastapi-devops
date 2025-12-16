pipeline {
    agent any

    triggers {
        githubPush()
    }

    stages {
        stage("Checkout Code") {
            steps {
                echo "GitHub webhook triggered this build"
                checkout scm
            }
        }
    }
}
