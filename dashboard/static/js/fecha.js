
document.addEventListener('DOMContentLoaded', function() {
    // Obtener la fecha actual en formato YYYY-MM-DD
    const today = new Date();
    const yyyy = today.getFullYear();
    const mm = String(today.getMonth() + 1).padStart(2, '0'); // Los meses empiezan en 0
    const dd = String(today.getDate()).padStart(2, '0');
    const todayDate = `${yyyy}-${mm}-${dd}`;

    // Establecer el atributo max para el campo de fecha de adquisición en el modal de agregar
    const fechaAdquisicionAdd = document.getElementById('fecha_adquisicion_add');
    if (fechaAdquisicionAdd) {
        fechaAdquisicionAdd.setAttribute('max', todayDate);
    }

    // Establecer el atributo max para el campo de fecha de adquisición en el modal de editar
    const fechaAdquisicionEdit = document.querySelectorAll('[id^="fecha_adquisicion_edit_"]');
    fechaAdquisicionEdit.forEach(function(element) {
        element.setAttribute('max', todayDate);
    });
});
