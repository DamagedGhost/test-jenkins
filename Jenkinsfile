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
                echo 'Generando documentación con contenedor efímero...'
                // Ejecutar Doxygen para generar la documentación a partir de comentarios en el código 
                // Utilizamos ${WORKSPACE} que es la variable nativa de Jenkins para la ruta del proyecto
                sh 'docker run --rm -v ${WORKSPACE}:/workspace -w /workspace ghcr.io/kingpin/doxygen-docker:latest doxygen Doxyfile'
            }
        }
        
        stage('Version Control') {
            steps {
                // Actualizar el repositorio de Git con la documentación generada 
                echo 'Preparando commit con la nueva documentación...' 
                
                sh '''
                    # Configurar la identidad de Git para este commit
                    git config user.name "Jenkins Automator"
                    git config user.email "jenkins@local"
                    
                    # Añadir la carpeta docs generada
                    git add docs/
                    
                    # Hacer commit (el || echo evita que el pipeline falle si no hubo cambios en la docu)
                    git commit -m "docs: Actualización automática de Doxygen" || echo "No hay cambios para commitear"
                    
                    # Subir los cambios a tu rama main
                    git push origin HEAD:main
                '''
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