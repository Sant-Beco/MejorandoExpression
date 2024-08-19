document.addEventListener('DOMContentLoaded', function () {
    // Selecciona el formulario
    var formulario = document.getElementById('formulario_publi');

    // Agrega un event listener para el evento submit
    formulario.addEventListener('submit', function (event) {
        event.preventDefault(); // Evita el envío automático del formulario y la recarga de la página

        // Captura los valores ingresados en los campos
        var categoria = document.getElementById('catego_publi').value.trim();

        // Valida que el campo obligatorio (categoría) esté completo
        if (categoria === '') {
            // Muestra la alerta de campos incompletos utilizando SweetAlert
            Swal.fire({
                icon: 'error',
                title: 'Campos Incompletos',
                text: 'Por favor completa el campo de categoría antes de postear la publicación.',
            });
            return false; // Evita que se envíe el formulario si es falso
        }

        // Mostrar ventana modal de éxito
        Swal.fire({
            icon: 'success',
            title: '¡Publicación Exitosa!',
            text: 'La publicación se ha realizado exitosamente.',
        }).then((result) => {
            if (result.isConfirmed || result.isDismissed) {

                formulario.reset();
                window.location.href = publicacionURL;
            }
            
        });

        return false; // Evita que se envíe el formulario si es falso
    });
});


// Asignar la función validarFormularioProdu al evento submit del formulario
document.getElementById('formulario_publi').addEventListener('submit', validarFormularioPubli);