// form-produc.js
document.addEventListener('DOMContentLoaded', function () {
    var formulario = document.getElementById('formulario_produ');

    formulario.addEventListener('submit', function (event) {
        event.preventDefault();

        var nombre_producto = document.getElementById('nombre_producto').value.trim();
        var descripcion = document.getElementById('descripcion').value.trim();
        var precio = document.getElementById('precio').value.trim();
        var categoria = document.getElementById('categoria').value.trim();

        
        var errorMessages = document.querySelectorAll('.error-message'); // Limpiar mensajes de error anteriores
        errorMessages.forEach(function (msg) {
            msg.remove();
        });

        var isValid = true;

        function showError(inputId, message) {
            var inputElement = document.getElementById(inputId);
            var errorElement = document.createElement('div');
            errorElement.className = 'error-message';
            errorElement.style.color = 'red';
            errorElement.textContent = message;
            inputElement.parentNode.appendChild(errorElement);
            isValid = false;
        }

        // Validar cada campo y mostrar mensajes de error si están vacíos
        if (nombre_producto === '') {
            showError('nombre_producto', ' completa el campo');
        }
        if (descripcion === '') {
            showError('descripcion', 'complete el campo de descripción.');
        }
        if (precio === '') {
            showError('precio', 'ingresa un valor');
        }
        if (categoria === '') {
            showError('categoria', 'Por favor, selecciona una categoría.');
        }

        if (isValid) {
            Swal.fire({
                icon: 'success',
                title: '¡producto Exitosa!',
                text: 'La publicación del producto se ha realizado exitosamente.',
            }).then((result) => {
                if (result.isConfirmed || result.isDismissed) {
                    formulario.submit(); // Envía el formulario
                }
            });
        }
    });
});