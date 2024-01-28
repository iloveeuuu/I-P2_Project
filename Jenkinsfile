pipeline {
    agent {
        kubernetes {
            defaultContainer 'python'
            yaml """
                apiVersion: v1
                kind: Pod
                metadata:
                  labels:
                    app: my-python-app
                spec:
                  containers:
                  - name: python
                    image: 'jenkins/inbound-agent-python:latest'
                    command:
                    - 'sleep'
                    args:
                    - '30d'
            """
        }
    }

    stages {
        stage('Get a Python Project') {
            steps {
                script {
                    checkoutCode()
                    installPython()
                }
            }
        }

        stage('Installing packages') {
            steps {
                script {
                    installPackages()
                }
            }
        }

        stage('Static Code Check') {
            steps {
                script {
                    staticCodeCheck()
                }
            }
        }

        stage('Unit Test Check') {
            steps {
                script {
                    unitTestCheck()
                }
            }
        }
    }

    post {
        always {
            cleanUp()
        }
    }
}

def checkoutCode() {
    container('python') {
        echo 'Checking out code...'
        sh 'apt update && apt install -y nano && apt install -y git'
        sh 'git clone https://github.com/iloveeuuu/jenkins_python.git'
        sh 'ls -la jenkins_python'
        sh 'python3 jenkins_python/cal.py'
    }
}

def installPython() {
    container('python') {
        echo 'Installing Python...'
        sh 'apt install -y python3'
        sh 'python3 -V'
        sh 'hostname'
    }
}

def installPackages() {
    container('python') {
        echo 'Installing packages...'
        sh 'apt install -y pip && apt install -y python3-psutil && apt install -y python3-requests'
        sh 'python3 jenkins_python/cal.py'
    }
}

def staticCodeCheck() {
    container('python') {
        echo 'Running static code check...'
        sh 'apt install -y pylint'
        sh 'pylint jenkins_python/menu_selection.py'
    }
}

def unitTestCheck() {
    container('python') {
        echo 'Running unit tests...'
        sh 'python3 jenkins_python/unittest check_os.py'
    }
}

def cleanUp() {
    echo 'Performing cleanup...'
    // Add cleanup steps here if needed
}
