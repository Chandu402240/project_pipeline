pipeline {
  agent { docker { image 'python:3.7.2' } }
  stages {
    stage('SCM Checkout') {
      steps {      
        git credentialsId: 'chandu402240', url: 'https://github.com/Chandu402240/project_pipeline.git'
      }
    }
    stage('test') {
      steps {
        sh 'python project_test.py'
      }
    }   
    stage('Build Docker Image') {
      steps {
        sh "docker build -t flaskpipeline:${BUILD_NUMBER} ."
        sh "docker tag flaskpipeline:${BUILD_NUMBER} chandu402240/flaskpipeline:${BUILD_NUMBER}"
      }
    }
    stage('Push Docker Image to Registry') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'DockerHub', passwordVariable: 'DOCKER_HUB_PASSWORD', usernameVariable: 'DOCKER_HUB_USER')]) {
          sh "docker login -u ${DOCKER_HUB_USER} -p ${DOCKER_HUB_PASSWORD}"
        }
        sh "docker push chandu402240/flaskpipeline:${BUILD_NUMBER}"
      }
    }
    stage('Deploy/Run Container on DEV Server') {
      steps {
        sh "docker rm -f chandu402240/flaskpipeline:${BUILD_NUMBER} || true"
        sh "docker run -p 5000:5000 -d --name flaskpipeline chandu402240/flaskpipeline:${BUILD_NUMBER}"
      }
    }
  }
}
