pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the source code.
                checkout scm
            }
        }

        stage('Read Commit Message and Run ML Integration') {
            steps {
                script {
                    // Access the commit message and author
                    sh 'env'
                    def commitMessage = env.CHANGE_REQUEST
                    def commitAuthor = env.CHANGE_AUTHOR
                    echo "Commit Message: ${commitMessage}"
                    // echo "Commit Author: ${commitAuthor}"

                    // Now you can use 'commitMessage' in your ml_integration step
                    // For example:
                    // sh "Integration.py '${commitMsg}'"

                }
            }
        }
    }
}
