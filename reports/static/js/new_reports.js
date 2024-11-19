document.addEventListener('DOMContentLoaded', function() {
    var descripcion = document.getElementById('descripcion');
    var charCountElement = document.getElementById('charCount');
    var errorMessage = document.getElementById('error-message');
    var minLength = 30;
    var maxLength = 500;
    var reportForm = document.getElementById('reportForm');

    function updateCharCount() {
        var charCount = descripcion.value.length;
        charCountElement.textContent = 'Caracteres escritos: ' + charCount;

        // Mostrar/ocultar mensaje de error si no cumple con el mínimo
        if (charCount < minLength) {
            errorMessage.textContent = 'La descripción debe tener al menos 30 caracteres.';
            errorMessage.classList.remove('d-none');
        } else {
            errorMessage.classList.add('d-none');
        }
    }

    function autoResize() {
        descripcion.style.height = 'auto';
        descripcion.style.height = descripcion.scrollHeight + 'px';
    }

    descripcion.addEventListener('input', function() {
        updateCharCount();
        autoResize();
    });

    // Verifica el formulario antes de enviarlo
    reportForm.addEventListener('submit', function(event) {
        var charCount = descripcion.value.length;

        // Impide el envío si no se cumple con el mínimo de caracteres
        if (charCount < minLength) {
            event.preventDefault();
            errorMessage.textContent = 'La descripción debe tener al menos 30 caracteres antes de enviar.';
            errorMessage.classList.remove('d-none');
        } else {
            errorMessage.classList.add('d-none');
        }

        console.log('Formulario enviado');
    });

    // Inicializa el contador y el tamaño del textarea
    updateCharCount();
    autoResize();
});
