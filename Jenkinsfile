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
    catchError {
        stage('testRunning') {
            sh 'export DISPLAY=:0 && cd search && python tests.py'
        }
    }
    
    catchError {
        stage('testEightPuzzle') {
            sh 'python eightpuzzle.py'
        }
    }
    
    catchError {
        stage('testEast') {
            sh 'export DISPLAY=:0 && cd search && python pacman.py -l mediumDottedMaze -p StayEastSearchAgent'
        }
    }
    
    catchError {
        stage('testWest') {
            sh 'export DISPLAY=:0 && cd search && python pacman.py -l mediumScaryMaze -p StayWestSearchAgent'
        }
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

}
