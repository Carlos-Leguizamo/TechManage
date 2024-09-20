// Función para validar el campo con el patrón y mostrar el mensaje de error
function validateField(field, pattern, errorMessage) {
    const errorElement = document.getElementById('error-message');
    
    field.addEventListener('input', function () {
        const value = field.value;

        // Si no cumple con el patrón, muestra el error
        if (!pattern.test(value)) {
            field.setCustomValidity(errorMessage);
            errorElement.classList.remove('d-none'); // Muestra el mensaje de error
        } else {
            field.setCustomValidity('');
            errorElement.classList.add('d-none'); // Oculta el mensaje de error
        }
    });
}


const descripcionField = document.getElementById('descripcion');

// Nueva expresión regular que permite letras, acentos, espacios y signos de puntuación comunes, pero evita letras consecutivas repetidas.
const pattern = /^[A-ZÁÉÍÓÚÑ](?!.*([A-Za-zÀ-ÿ])\1)[A-Za-zÀ-ÿ0-9\s,.\-—;:¡!¿?()]+$/;
const errorMessage = "Solo se permiten letras, signos de puntuación y espacios, sin caracteres repetidos consecutivamente.";


validateField(descripcionField, pattern, errorMessage);
