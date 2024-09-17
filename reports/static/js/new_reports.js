document.addEventListener('DOMContentLoaded', function() {
    const descripcion = document.getElementById('descripcion');
    const charCount = document.getElementById('charCount');
    const form = document.getElementById('reportForm');
    const errorMessage = document.getElementById('error-message');
    const minLength = 500;

    function updateCharCount() {
        const length = descripcion.value.length;
        const remaining = minLength - length;
        charCount.textContent = `Caracteres restantes: ${remaining >= 0 ? remaining : 0}`;
        charCount.style.color = remaining < 0 ? 'red' : 'gray';
    }

    function validateForm(event) {
        const length = descripcion.value.length;
        if (length < minLength) {
            event.preventDefault(); // Evita que el formulario se envíe
            errorMessage.classList.remove('d-none'); // Muestra el mensaje de error
        } else {
            errorMessage.classList.add('d-none'); // Oculta el mensaje de error
        }
    }

    descripcion.addEventListener('input', updateCharCount);
    form.addEventListener('submit', validateForm);

    updateCharCount(); // Inicializa el contador de caracteres
});