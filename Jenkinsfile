pipeline {
    agent any

    triggers {
        githubPush()
    }

    stages {
        stage("Checkout Code") {
            steps {
                echo "GitHub hpp webhook triggered this build"
                checkout scm
            }
        }
    }
}
