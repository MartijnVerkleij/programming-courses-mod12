pipeline {
    agent any 
    stages {
        stage('Stage 1') {
            steps {
                junit 'build/reports/**/*.xml'
            }
        }
    }
}