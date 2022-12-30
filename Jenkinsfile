
def buildDockingFactory(){
    script {
        sh("python3 -m venv buildDockingFactory && source ./buildDockingFactory/bin/activate")
        sh("python3 -m pip install --upgrade --user pip build")
        sh("python3 -m build")
        sh("aws s3 mv --recursive --include '*' ./dist  s3://${SCIP_DEPLOYMENT_BUCKET}/python_packages/")
    }
}

pipeline {
    
    agent none

    stages {
        stage("Build and publish") {
            agent { label 'linux' }
            
            steps {
                buildDockingFactory()
                cleanWs()
            }
        }
    }
}
