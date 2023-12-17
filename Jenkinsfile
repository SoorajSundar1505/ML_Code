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
    environment {
        PATH = "C:\\Users\\suraj\\AppData\\Local\\Programs\\Python\\Python311;${env.PATH}"
    }
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from your version control system (e.g., Git)
                script {
                    checkout scm
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Install required Python packages
                    // bat 'python -m pip install --upgrade pip'
                    // bat 'python -m pip install joblib'
                    bat 'pip install -U scikit-learn'
                    // bat 'python -m pip install --upgrade joblib'
                }
            }
        }

        // stage('Print Python Environment') {
        //     steps {
        //         bat 'where python'
        //         bat 'python --version'
        //         bat 'python -m pip list'
        //     }
        // }

        stage('Set Commit Message') {
            steps {
                script {
                    // Get the commit message from Git using PowerShell
                    def commitMessage = powershell(returnStdout: true, script: 'git log -1 --pretty=format:"%s%n%n%b"')

                    // Check if the git command was successful
                    if (!commitMessage.isEmpty()) {
                        // Set the environment variable for the commit message
                        env.CHANGE_MESSAGE = commitMessage.trim()

                        // Print the commit message for verification
                        echo "Commit Message: ${env.CHANGE_MESSAGE}"
                    } else {
                        error "Failed to retrieve the commit message."
                    }
                    
                     // bat 'python -m pip install joblib'
                    bat "Integration.py '${env.CHANGE_MESSAGE}'"
                }
            }
        }
        // Your other stages go here
    }
}
