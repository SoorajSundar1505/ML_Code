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

                    // def commitMessage = env.CHANGE_MESSAGE ?: 'Default Commit Message'
                    // def commitAuthor = env.CHANGE_AUTHOR

                    def commit = sh(returnStdout: true, script: 'git log -1 --oneline').trim()

                    String commitMsg = ""
                    
                    List commitMsgPre = commit.split(" ")
                    
                    for(int i=1; i<commitMsgPre.size(); i++){
                      commitMsg += commitMsgPre.getAt(i) + " "
                    }

                    echo "Commit Message: ${commitMsg}"
                    // echo "Commit Author: ${commitAuthor}"

                    // Now you can use 'commitMessage' in your ml_integration step
                    // For example:
                    // sh "Integration.py '${commitMsg}'"

                }
            }
        }
    }
}
