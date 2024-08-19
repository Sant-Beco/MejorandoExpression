document.addEventListener('DOMContentLoaded', function() {
  const checkboxes = document.querySelectorAll('.form-check-input');

  checkboxes.forEach(checkbox => {
      checkbox.addEventListener('change', function(event) {
          event.preventDefault(); // Evita la redirección predeterminada al hacer clic en el checkbox

          if (checkbox.checked) {
              // Si el checkbox está marcado, mostrar mensaje de confirmación para deshabilitarlo
              Swal.fire({
                  title: '¿Desea inhabilitar?',
                  showCancelButton: true,
                  confirmButtonText: 'Sí',
                  cancelButtonText: 'No',
                  customClass: {
                      confirmButton: 'swal-button-custom',
                      cancelButton: 'swal-button-custom'
                  }
              }).then((result) => {
                  if (result.isConfirmed) {
                      checkbox.checked = true; // Marcar checkbox
                      Swal.fire({
                          icon: "success",
                          title: "inhabilitación exitosa",
                          showConfirmButton: false,
                          timer: 1500
                      });
                  } else {
                      // No hacer nada si el usuario elige no deshabilitar
                  } 
              });

          } else {
              Swal.fire({
                  title: '¿Desea habilitar nuevamente?',
                  showCancelButton: true,
                  confirmButtonText: 'Sí',
                  cancelButtonText: 'No',
                  customClass: {
                      confirmButton: 'swal-button-custom',
                      cancelButton: 'swal-button-custom'
                  }
              }).then((result) => {
                  if (result.isConfirmed) {
                      checkbox.disabled = false; // Marcar checkbox
                      Swal.fire({
                          icon: "success",
                          title: "Habilitacion exitosa",
                          showConfirmButton: false,
                          timer: 1500
                      });
                  } else {
                      // No hacer nada si el usuario elige no deshabilitar
                  } 
              });
          }
      });
  });
});