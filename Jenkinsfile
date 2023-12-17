pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the source code.
                checkout scm
            }
        }

        stage('Read Commit Message') {
            steps {
                script {
                    // Access the commit message and author

                    // def commitMessage = env.CHANGE_MESSAGE ?: 'Default Commit Message'
                    // def commitAuthor = env.CHANGE_AUTHOR

                    // echo "Commit Message: ${commitMessage}"
                    // echo "Commit Author: ${commitAuthor}"

                    // Now you can use 'commitMessage' in your ml_integration step
                    // For example:
                    // sh "python ML_Integration.py '${commitMessage}'"

                     // Get the commit message directly from Git
                    def commitMessage = sh(script: 'git log -1 --pretty=%B', returnStdout: true).trim()
                    
                    // Get the commit author directly from Git
                    def commitAuthor = sh(script: 'git log -1 --pretty=%an', returnStdout: true).trim()

                    // Print the commit message and author
                    echo "Commit Message: ${commitMessage}"
                    echo "Commit Author: ${commitAuthor}"
                }
            }
        }

        stage('Run ML Integration') {
            steps {
                // You can call your ml_integration.py script here
                // For example:
                sh "Integration.py '${commitMessage}'"
            }
        }
    }
}
