pipeline {
  agent {
    label 'python'
  }
  options { 
      skipDefaultCheckout() 
  }
  stages {
    stage('Checkout') {
      steps {
        sh 'git checkout develop'
      }
    }
    stage('Build') {
      steps {
        // sh 'git checkout develop'
        echo 'Build stage'
      }
    }
    stage('Test') {
      steps {
        // sh 'git checkout develop'
        echo 'Test stage'
      }
    }
    stage('Deploy') {
      steps {
        // sh 'git checkout develop'
        echo 'Deploy stage'
      }
    }
  }
}
