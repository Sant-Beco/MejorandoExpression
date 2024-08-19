// Pruebas sweetalert admin producto

// inhabilitar


  const inhabilitarBoton = document.getElementById('inhabilitarBoton');

  inhabilitarBoton.addEventListener('click', function() {
    Swal.fire({
      title: "Inhabilitar Producto",
      footer: "Recuerda que debe ser coherente con las reglas de negocio de cultural expression",
      icon: "warning",
      showCancelButton: true,
      confirmButtonColor: "#0ff",
      cancelButtonColor: "#f00",
      confirmButtonText: "Aceptar"
    }).then((result) => {
      if (result.isConfirmed) {
        Swal.fire({
          title: "Producto inhabilitado", 
          text: "El producto ha sido inhabilitado exitosamente.",
          icon: "success"
        });
      }
    });
  });

// habilitar

const habilitarBoton = document.getElementById('habilitarBoton');

habilitarBoton.addEventListener('click', function() {
  Swal.fire({
    title: "habilitar Producto",
    footer: "Recuerda que debe ser coherente con las reglas de negocio de cultural expression",
    icon: "warning",
    showCancelButton: true,
    confirmButtonColor: "#0ff",
    cancelButtonColor: "#f00",
    confirmButtonText: "Aceptar"
  }).then((result) => {
    if (result.isConfirmed) {
      Swal.fire({
        title: "Producto habilitado", 
        text: "El producto ha sido habilitado exitosamente.", 
        icon: "success"
      });
    }
  });
});
