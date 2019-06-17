pipeline {
    agent any
        stages {
            stage('test') {
                steps {
                    sh 'export DISPLAY=:0 && cd search && python tests.py'
                }
            }
        }
    }
