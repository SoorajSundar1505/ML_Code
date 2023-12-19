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
    tools {
        // Install the Maven version configured as "M3" and add it to the path.
        maven 'MAVEN_HOME'
        jdk 'JAVA_HOME'
    }
    environment {
         PATH = "C:\\Users\\suraj\\AppData\\Local\\Programs\\Python\\Python311;${env.PATH}"
         PREDICT_OUTCOME=''
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
                    bat 'python -m pip install -U joblib'
                    bat 'python -m pip install scikit-learn==1.2.2'
                    bat 'python -m pip install -U requests'
                    // bat 'python -m pip install --upgrade joblib'
                }
            }
        }

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
                    
                     def getCommitMessage = env.CHANGE_MESSAGE
                     def outputFilePath = "output.txt"
                    bat(script: "python Integration.py \"${getCommitMessage}\"", returnStatus: true)
                    
                    // Read the content of the file
                    def outcome = readFile(file: outputFilePath).trim()

                    
                    // The outcome variable now contains the outcome prediction result
                    echo "Outcome prediction result: ${outcome}"
                    
                     // def outcome = bat(script: "python Integration.py \"${getCommitMessage}\"", returnStatus: false,returnStdout: true).trim()
                     // echo "the output string is: ${outcome}"
                     // PREDICT_OUTCOME = ${outcome}
                     // println "the PREDICT_OUTCOME string is: ${PREDICT_OUTCOME}"
                    if(outcome=="1"){
                        git 'https://github.com/SoorajSundar1505/restAPI'
                        bat "mvn compile"
                        bat "mvn clean test"
                        bat "mvn package"
                    }else{
                        echo "No regression required"
                    }
                    
                }
            }
        }
    //     stage('Run Regression'){
    //           steps{
    //               script{
    //                   if(PREDICT_OUTCOME==
    //                     git 'https://github.com/SoorajSundar1505/restAPI'
    //                     bat "mvn compile"
    //                     bat "mvn clean test"
    //                     bat "mvn package"
    //               }
    //           }
    //     }             
                      
    // }
}
}
