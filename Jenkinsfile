pipeline {
    agent any
        stages {
            stage('build-flake') {
            
                failFast false;
                steps {
                    sh 'pip install flake8'
                }
            }
            stage('build-sandbox') {
                failFast false;
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
                failFast false;
                steps {
                    sh 'export DISPLAY=:0 && cd search && python tests.py'
                }
            }
            stage('test-sandbox'){
                failFast false;
                try {
                steps {
                    sh 'export DISPLAY=:0 && cd search && ../sandbox-env/bin/run python $(pwd)/tests.py'
                }
                } catch (Exception e) {
                    unstable e.getMessage()
                }
            }
            stage('checkstyle') {
                failFast false;
                steps {
                    sh 'flake8 --config=jenkins/flake8.ini search'
                }
            }
            stage('EMMA') {
                failFast false;
                steps {
                    sh 'flake8 --config=jenkins/flake8.ini search'
                }
            }
        }
    }
