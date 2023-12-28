pipeline {
    agent any
    tools {
        // Install the Maven version configured as "M3" and add it to the path.
        maven 'MAVEN_HOME'
        jdk 'JAVA_HOME'
    }
    environment {
         PATH = "C:\\Users\\suraj\\AppData\\Local\\Programs\\Python\\Python311;${env.PATH}"
    }
    stages {
        stage('Checkout') {
            steps {
                script {
                    checkout scm
                }
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    bat 'python -m pip install -U joblib'
                    bat 'python -m pip install scikit-learn==1.2.2'
                    bat 'python -m pip install -U requests'
                }
            }
        }

        stage('Read Commit Message and decide whether need to run regression') {
            steps {
                script {
                    // Get the commit message from Git using PowerShell
                    def commitMessage = powershell(returnStdout: true, script: 'git log -1 --pretty=format:"%s%n%n%b"')
                    // Check if the git command was successful
                    if (!commitMessage.isEmpty()) {
                        // Set the environment variable for the commit message
                        env.CHANGE_MESSAGE = commitMessage.trim()
                        echo "Commit Message: ${env.CHANGE_MESSAGE}"
                    } else {
                        error "Failed to retrieve the commit message."
                    }
                     def getCommitMessage = env.CHANGE_MESSAGE
                     bat(script: "python getCommitMessage.py \"${getCommitMessage}\"", returnStatus: true)
                    
                     def outputFilePath = "output.txt" 
                    // Read the content of the file
                    def outcome = readFile(file: outputFilePath).trim()
                    // The outcome variable now contains the outcome prediction result
                    echo "Outcome prediction result is: ${outcome}"
                    if(outcome=='login'){
                        echo "running regression suite....."
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
}

    post {
        always {
            script {
                def outputFilePath = "output.txt"
                // Delete the output.txt file
                bat "del ${outputFilePath}"
            }
        }
    }
}
