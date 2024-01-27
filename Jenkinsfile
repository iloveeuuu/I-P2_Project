podTemplate(containers: [ 
  containerTemplate( 
    name: 'python',  
    image: 'jenkins/inbound-agent-python:latest',  
    command: 'sleep',  
    args: '30d') 
])  
{ 
 
  node(POD_LABEL)  
  { 
      stage('Get a Python Project')  
    { 
        container('python')  
      { 
stages{        
   stage(‘Checkout Code’)  
        { 
            sh 'pwd' 
            sh 'ls -la' 
            sh 'python -V' 
            sh 'git clone https://github.com/iloveeuuu/jenkins_python.git' 
            sh 'ls -la jenkins_python' 
            sh 'python jenkins_python/cal.py' 
          } 
   stage(' Installing packages')  
        { 
            sh 'pwd' 
            sh 'ls -la' 
            sh 'python -V' 
            sh 'git clone https://github.com/iloveeuuu/jenkins_python.git' 
            sh 'ls -la jenkins_python' 
            sh 'python jenkins_python/cal.py' 
          } 
   stage(‘Static Code Check')  
        { 
            sh 'pwd' 
            sh 'ls -la' 
            sh 'python -V' 
            sh 'git clone https://github.com/iloveeuuu/jenkins_python.git' 
            sh 'ls -la jenkins_python' 
            sh 'python jenkins_python/cal.py' 
          } 
stage(‘Unit Test Check')  
        { 
            python3 -m unittest check_os.py          } 
} 
        } 
      } 
    } 
} 
