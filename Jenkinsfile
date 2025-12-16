pipeline {
    agent any

    triggers {
        githubPush()
    }

    stages {
        stage("Checkout Code") {
            steps {
                echo "GitHub h webhook triggered this build"
                checkout scm
            }
        }
    }
}
