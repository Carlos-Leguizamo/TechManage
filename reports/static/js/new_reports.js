document.addEventListener('DOMContentLoaded', function() {
    var descripcion = document.getElementById('descripcion');
    var maxLength = 500;

    function updateCharCount() {
        var charCount = descripcion.value.length;
        var charCountElement = document.getElementById('charCount');
        charCountElement.textContent = 'Caracteres restantes: ' + (maxLength - charCount);
    }

    function autoResize() {
        descripcion.style.height = 'auto';
        descripcion.style.height = descripcion.scrollHeight + 'px';
    }

    function enforceMaxLength() {
        if (descripcion.value.length > maxLength) {
            descripcion.value = descripcion.value.slice(0, maxLength);
        }
    }

    descripcion.addEventListener('input', function() {
        updateCharCount();
        autoResize();
        enforceMaxLength();
    });

    updateCharCount(); // Inicializa el contador de caracteres
    autoResize(); // Inicializa el tamaño del textarea
});