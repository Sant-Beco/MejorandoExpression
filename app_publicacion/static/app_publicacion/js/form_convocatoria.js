// form-convo.js

// Función para validar el formulario y mostrar la ventana modal de éxito
function validarFormularioConvo(event) {
    event.preventDefault(); // Evita el envío automático del formulario y la recarga de la página

    // Captura los valores ingresados en los campos
    var titulo = document.getElementById("titulo_convo").value;
    var descripcion = document.getElementById("descrip_convo").value;
    var fecha_inicio = document.getElementById("fecha_inicio_convo").value;
    var fecha_fin = document.getElementById("fecha_fin_convo").value;
    var lugar = document.getElementById("lugar_convo").value;
    var categoria = document.getElementById("catego_convo").value;
    var foto_convo = document.getElementById("file_convo").value;

    // Valida que todos los campos requeridos estén completos
    if (fecha_inicio === "" || fecha_fin === "" || lugar === "" || categoria === "") {
        // Muestra la alerta de campos incompletos utilizando Swal
        Swal.fire({
            icon: 'error',
            title: 'Campos Incompletos',
            text: 'Por favor completa todos los campos antes de postear la convocatoria.',
        });
        return false; // Evita que se envíe el formulario si es falso
    }

    // Mostrar ventana modal de éxito
    Swal.fire({
        icon: 'success',
        title: '¡Convocatoria Publicada!',
        text: 'La convocatoria se ha publicado exitosamente.',
    }).then((result) => {
        if (result.isConfirmed || result.isDismissed) {
            // Redirigir a la página de publicaciones
            window.location.href = convocatoriaURL;
        }
    });

    return false;
}

// Asignar la función validarFormulario al evento submit del formulario
document.getElementById('formulario_convo').addEventListener('submit', validarFormularioConvo);

