// form-produc.js

// Función para validar el formulario y mostrar la ventana modal de éxito
function validarFormularioProdu(event) {
    event.preventDefault(); // Evita el envío automático del formulario y la recarga de la página

    // Captura los valores ingresados en los campos
    var nombre_producto = document.getElementById('nombre_produc').value.trim();
    var descripcion = document.getElementById('descrip_produc').value.trim();
    var precio = document.getElementById('precio_produc').value.trim();
    var categoria = document.getElementById('catego_produc').value.trim();
    var archivo = document.getElementById('file_produc').value.trim(); // Validar que el campo de archivo no esté vacío

    // Valida que todos los campos requeridos estén completos
    if (nombre_producto === '' || descripcion === '' || precio === '' || categoria === '' || archivo === '') {
        // Muestra la alerta de campos incompletos utilizando
        Swal.fire({
            icon: 'error',
            title: 'Campos Incompletos',
            text: 'Por favor completa todos los campos antes de postear el producto.',
        });
        return false; // Evita que se envíe el formulario si es falso
    }

    // Mostrar ventana modal de éxito
    Swal.fire({
        icon: 'success',
        title: '¡Producto Publicado!',
        text: 'El producto se ha publicado exitosamente.',
    }).then((result) => {
        if (result.isConfirmed || result.isDismissed) {
            // Redirigir a la página de publicaciones
            window.location.href = productoURL;
        }
    });

    return false; // Evita que se envíe el formulario si es falso


}

// Asignar la función validarFormularioProdu al evento submit del formulario
document.getElementById('formulario_produ').addEventListener('submit', validarFormularioProdu);
