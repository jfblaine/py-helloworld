pipeline {
    agent any
    options {
        skipStagesAfterUnstable()
    }
    stages {
         stage('Clone repository') { 
            steps { 
                script{
                checkout scm
                }
            }
         }
         stage('Sleep') {
            steps {
                sleep(120)
                echo 'Done Sleeping'
                }
         }
    }
}
