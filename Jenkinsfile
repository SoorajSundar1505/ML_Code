// pipeline {
//     agent any

//     stages {
//         stage('Checkout') {
//             steps {
//                 // Checkout the source code.
//                 checkout scm
//             }
//         }

//         stage('Print Environment Variables') {
//             steps {
//                 script {
//                     bat 'set'
//                 }
//             }
//         }

//         stage('Read Commit Message and Run ML Integration') {
//             steps {
//                 script {
//                     // Access the commit message and author
//                     def commitMessage = env.CHANGE_REQUEST
//                     def commitAuthor = env.CHANGE_AUTHOR
//                     echo "Commit Message: ${commitMessage}"
//                     // echo "Commit Author: ${commitAuthor}"

//                     // Now you can use 'commitMessage' in your ml_integration step
//                     // For example:
//                     // sh "Integration.py '${commitMsg}'"

//                 }
//             }
//         }
//     }
// }


pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from your version control system (e.g., Git)
                script {
                    checkout scm
                }
            }
        }

        stage('Set Commit Message') {
            steps {
                script {
                    // Get the commit message from Git
                    def commitMessage = bat(script: 'git log -1 --pretty=format:"%s%n%n%b"', returnStdout: true).trim()

                    // Check if the git command was successful
                    if (!commitMessage.isEmpty()) {
                        // Set the environment variable for the commit message
                        env.CHANGE_MESSAGE = commitMessage

                        // Print the commit message for verification
                        echo "Commit Message: ${env.CHANGE_MESSAGE}"
                    } else {
                        error "Failed to retrieve the commit message."
                    }
                }
            }
        }

        // Your other stages go here
    }
}
