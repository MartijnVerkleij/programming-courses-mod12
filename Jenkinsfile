pipeline {
/*    agent any 
    stages {
        stage('Java Stage') {
            steps {
                junit 'build/reports/**/*.xml'
            }
        }
    }
    */
    
    agent { docker { image 'python:2.7' } }
        stages {
            /*stage('build') {
                steps {
                    sh 'pip install -r requirements.txt'
                }
            }*/
            stage('test') {
                steps {
                    sh 'python search/tests.py'
                }
            }
        }
    }
    
}
