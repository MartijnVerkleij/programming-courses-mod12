node {
    stage('build-flake') {

        failFast false;
        steps {
            sh 'pip install flake8'
        }
    }
    stage('build-sandbox') {
        steps {
            sh '''
            rm -rf pynbox
            git clone https://github.com/dsagal/pynbox.git

            cd pynbox
            ./pynbox install ../sandbox-env python tests

            cd ../
            sandbox-env/bin/test_pynbox
            '''
        }
    }
    stage('test') {
        steps {
            sh 'export DISPLAY=:0 && cd search && python tests.py'
        }
    }
    stage('test-sandbox') {
        try {
            sh 'export DISPLAY=:0 && cd search && ../sandbox-env/bin/run python $(pwd)/tests.py'
        } catch (Exception e) {
            unstable e.getMessage()
        }
    }
    stage('checkstyle') {
        steps {
            sh 'flake8 --config=jenkins/flake8.ini search'
        }
    }
    stage('EMMA') {
        steps {
            sh 'flake8 --config=jenkins/flake8.ini search'
        }
    }
}
