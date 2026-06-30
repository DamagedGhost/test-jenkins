pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                // Compilar el código fuente [cite: 32]
                echo 'Compilando el código fuente...' 
            }
        }
        
        stage('Test') {
            steps {
                // Ejecutar pruebas unitarias [cite: 33]
                echo 'Ejecutando pruebas unitarias...' 
            }
        }
        
        stage('Generate Documentation') {
            steps {
                echo 'Generando documentación...'
                sh 'doxygen Doxyfile' 
            }
        }
        
        stage('Version Control') {
                    steps {
                        echo 'Preparando commit con la nueva documentación...' 
                        
                        // Asegúrate de que 'github-token' sea el ID exacto que le pusiste a la credencial en Jenkins
                        withCredentials([usernamePassword(credentialsId: 'Repo-Token', passwordVariable: 'GIT_PASSWORD', usernameVariable: 'GIT_USERNAME')]) {
                            sh '''
                                # Configurar la identidad de Git
                                git config user.name "Jenkins Automator"
                                git config user.email "jenkins@local"
                                
                                # Añadir la carpeta docs generada
                                git add docs/
                                
                                # Hacer commit
                                git commit -m "docs: Actualización automática de Doxygen" || echo "No hay cambios para commitear"
                                
                                # Hacer push usando las variables de entorno inyectadas
                                git push https://${GIT_USERNAME}:${GIT_PASSWORD}@github.com/DamagedGhost/test-jenkins.git HEAD:main
                            '''
                        }
                    }
                }
        
        stage('Deploy') {
            steps {
                // Desplegar la aplicación en un entorno de prueba [cite: 36]
                echo 'Desplegando en entorno de prueba...' 
            }
        }
    }
}