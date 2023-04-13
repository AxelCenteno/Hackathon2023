const videoElement = document.getElementById('camera-stream');

navigator.mediaDevices.getUserMedia({ video: true })
  .then(stream => {
    videoElement.srcObject = stream;
  })
  .catch(error => {
    console.error('Error al acceder a la cámara', error);
  });
