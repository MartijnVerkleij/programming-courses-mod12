node {
    stage('build-flake') {
        sh 'pip install flake8'
    }
    stage('build-sandbox') {
        sh '''
        rm -rf pynbox
        git clone https://github.com/dsagal/pynbox.git

        cd pynbox
        ./pynbox install ../sandbox-env python tests

        cd ../
        sandbox-env/bin/test_pynbox
        '''
    }
    stage('test') {
        sh 'export DISPLAY=:0 && cd search && python tests.py'
    }
    
    catchError {
        stage('test-sandbox') {
            sh 'export DISPLAY=:0 && cd search && ../sandbox-env/bin/run python $(pwd)/tests.py'
        }
    }
    catchError {
        stage('checkstyle') {
            sh 'flake8 --config=jenkins/flake8.ini search'
        }
    }
    
    currentBuild.rawBuild.@result = hudson.model.Result.SUCCESS
s
}
