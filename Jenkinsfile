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
          stage('Checkout Code')
          {
            sh 'apt update'
            sh 'apt install -y nano'
            echo 'Y'
            sh 'apt install -y pip'
            echo 'Y'
            sh 'apt install python3'
            sh 'pwd'
            sh 'ls -la'
            sh 'python3 -V'
            sh 'hostname'
            sh 'git clone https://github.com/iloveeuuu/jenkins_python.git'
            sh 'ls -la jenkins_python'
            sh 'python3 jenkins_python/cal.py'
          }
          stage(' Installing packages')
          {
            sh 'pwd'
            sh 'ls -la'
            sh 'python3 -V'
            sh 'apt install -y pip'
            echo 'Y'
            sh 'apt install -y python3-psutil'
            echo 'Y'
            sh 'apt install -y python3-requests'
            echo 'Y'
            sh 'python3 jenkins_python/cal.py'       
          }
          stage('Static Code Check')
          {
            sh 'apt install -y pylint'
            echo 'Y'
            sh 'pylint jenkins_python/menu_selection.py'
          }
          stage('Unit Test Check')
          {
            sh 'python3 jenkins_python/unittest_os.py'          
          }
        
      }
    }
  }
}
