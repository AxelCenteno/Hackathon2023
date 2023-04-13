<p align="center">
  <img alt="MemorIA Logo" src="https://github.com/AxelCenteno/Hackathon2023/blob/main/Logo.png" width=100  >
</p>
<h1 align="center">
  <a href="#">
    MemorIA
  </a>
</h1>

<p align="center">
  <strong>Solución propuesta para el reto NXP "HoverGames Drones y Robotica para la Sociedad" Talent Land 2023</strong><br>
  @Hackaton Scott's TOTS
</p>

<p align="center">
  MemorIA es un sistema embebido capaz de facilitar el cuidado de personas con enfermedad de Alzheimer, este sistema cuenta con sensores, sistema de alertas mediante la nube y musicoterapia los cuales seran controlados por el cuidador mediante una pagina web. 
</p>  

<h3 align="center">
      <strong>Tecnologías (Software)</strong>
  
  <h5 align="center">
    ☑️Python 3.*
    ☑️Flask
    ☑️OpenCV
    ☑️Micropython
    ☑️Azure
  </h4>
</h3>

<h3 align="center">
      <strong>Tecnologías (Hardware)</strong>
  
  <h5 align="center">
    ☑️ESP32
    ☑️Sensor de Gas MQ135
    ☑️Sensor de Obstaculos Infrarrojo FC-51
    ☑️Camara (Integrada PC)
    ☑️Bocina (Integradas PC)
    ☑️GPS NEO-6M
  </h4>
</h3>
  
  
# Funcionalidades de proyecto
- Sistema de alertas: El sistema mediante camaras y sensores es capaz de reconocer patrones del paciente, y   al detectar una anomalia enviara una alerta a azure la cual sera notificada al cuidador
- Refuerzo de memoria: Mediante las bocinas del sistema se reproducira musica preseleccionada por el cuidador que provocen recuerdos en el paciente, ademas de que el cuidador podra grabar audios guia de actividades basicas, con el objetivo de ser reproducidas por el sistema en caso de que el paciente olvide como efectuar estas actividades.
- El sistema estara integrado con una pulsera GPS el cual estara conectado a Azure para el recibimiento de alertas para conocer su posicion en caso de que este salga de su domicilio.

# Flujo de la página

### Pantalla principal
![Página principal](https://user-images.githubusercontent.com/76974066/231741782-b48be752-bac5-4d34-9769-d3a0b0a4f828.jpeg)

### Ubicación del paciente
![Ubicación del paciente](https://user-images.githubusercontent.com/76974066/231741229-9a7d208d-c621-4c63-9ed7-321ed825410b.jpeg)


### Lista de cursos
![Datos del paciente](https://user-images.githubusercontent.com/76974066/231741761-1e42ec78-e5e8-44f0-9edb-9e24c1a77af3.jpeg)

## Diagrama del sistema
![Sistema](https://user-images.githubusercontent.com/76974066/231743054-e17c661d-98c2-4771-8c56-cd5e8d697dd5.jpeg)

## Diagrama de recursos de Azure
![Diagrama Azure](https://user-images.githubusercontent.com/76974066/231742372-f8c8702f-41ca-454b-8c7a-829e87dd5fac.PNG)


# Correr la aplicación 💻

### Crear entorno virtual

### Instalar requerimientos

  - Deberás instalar los requerimientos mencionados en el archivo 'requirements.txt'
pip install -r requirements.txt

### Establecer variables de entorno
  - set "FLASK_APP=run.py"

### Ejecutar en Flask
  - flask run

# Autores ✒️
- Axel Centeno: https://github.com/AxelCenteno
- David Camarero: https://github.com/DavidCM6
- Diego Hernandez:
- Zinedine Bautista:
- Fernando Rosal
