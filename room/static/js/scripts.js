let pcs = {
    1: [
        { id: 1, tipo: "Desktop", marca: "Dell", modelo: "Optiplex 7090", numeroSerie: "ABC123", fechaAdquisicion: "2023-01-15", estado: "Operativo" },
        { id: 2, tipo: "Laptop", marca: "Lenovo", modelo: "ThinkPad T14", numeroSerie: "XYZ789", fechaAdquisicion: "2022-11-30", estado: "En mantenimiento" },
    ],
    2: [
        { id: 3, tipo: "Desktop", marca: "HP", modelo: "EliteDesk 800 G6", numeroSerie: "DEF456", fechaAdquisicion: "2023-03-10", estado: "Fuera de servicio" },
    ],
    3: [
        { id: 4, tipo: "Laptop", marca: "Apple", modelo: "MacBook Pro", numeroSerie: "MNO321", fechaAdquisicion: "2023-02-20", estado: "En préstamo" },
    ],
};

let editingPCId = null;

function getStatusStyle(status) {
    switch (status) {
        case "Operativo":
            return "bg-green-500";
        case "En mantenimiento":
            return "bg-yellow-500";
        case "Fuera de servicio":
            return "bg-red-500";
        case "En préstamo":
            return "bg-blue-500";
        default:
            return "bg-gray-500";
    }
}

function filterBySala() {
    const salaSelect = document.getElementById("salaSelect");
    const selectedSala = salaSelect.value;
    const table = document.getElementById("pcsTable");
    const tbody = document.getElementById("pcsTableBody");
    tbody.innerHTML = "";
    if (selectedSala && pcs[selectedSala]) {
        pcs[selectedSala].forEach((pc) => {
            const row = document.createElement("tr");
            row.innerHTML = `
                <td>${pc.tipo}</td>
                <td>${pc.marca}</td>
                <td>${pc.modelo}</td>
                <td>${pc.numeroSerie}</td>
                <td>${pc.fechaAdquisicion}</td>
                <td>
                    <span class="status-tag ${getStatusStyle(pc.estado)}">${pc.estado}</span>
                </td>
                <td>
                    <button class="btn-crud" onclick="openEditModal(${pc.id}, ${selectedSala})">✏️</button>
                    <button class="btn-crud" onclick="handleDelete(${pc.id}, ${selectedSala})">🗑️</button>
                </td>
            `;
            tbody.appendChild(row);
        });
        table.style.display = "table";
    } else {
        table.style.display = "none";
    }
}

function openAddModal() {
    editingPCId = null;
    document.getElementById("modalTitle").textContent = "Añadir PC";
    document.getElementById("tipo").value = "";
    document.getElementById("marca").value = "";
    document.getElementById("modelo").value = "";
    document.getElementById("numeroSerie").value = "";
    document.getElementById("fechaAdquisicion").value = "";
    document.getElementById("estado").value = "Operativo";
    document.getElementById("modal").style.display = "flex";
}

function openEditModal(id, salaId) {
    const pc = pcs[salaId].find((p) => p.id === id);
    editingPCId = id;
    document.getElementById("modalTitle").textContent = "Editar PC";
    document.getElementById("tipo").value = pc.tipo;
    document.getElementById("marca").value = pc.marca;
    document.getElementById("modelo").value = pc.modelo;
    document.getElementById("numeroSerie").value = pc.numeroSerie;
    document.getElementById("fechaAdquisicion").value = pc.fechaAdquisicion;
    document.getElementById("estado").value = pc.estado;
    document.getElementById("modal").style.display = "flex";
}

function closeModal() {
    document.getElementById("modal").style.display = "none";
}

function savePC() {
    const tipo = document.getElementById("tipo").value;
    const marca = document.getElementById("marca").value;
    const modelo = document.getElementById("modelo").value;
    const numeroSerie = document.getElementById("numeroSerie").value;
    const fechaAdquisicion = document.getElementById("fechaAdquisicion").value;
    const estado = document.getElementById("estado").value;
    const salaSelect = document.getElementById("salaSelect");
    const selectedSala = salaSelect.value;

    if (!tipo || !marca || !modelo || !numeroSerie || !fechaAdquisicion || !estado || !selectedSala) {
        alert("Por favor, complete todos los campos.");
        return;
    }

    if (editingPCId) {
        // Editar PC existente
        pcs[selectedSala] = pcs[selectedSala].map((pc) =>
            pc.id === editingPCId
                ? { id: editingPCId, tipo, marca, modelo, numeroSerie, fechaAdquisicion, estado }
                : pc
        );
    } else {
        // Añadir nuevo PC
        const newPCId = Math.max(...Object.values(pcs).flat().map(pc => pc.id)) + 1;
        const newPC = { id: newPCId, tipo, marca, modelo, numeroSerie, fechaAdquisicion, estado };
        pcs[selectedSala].push(newPC);
    }

    filterBySala();
    closeModal();
}

// Función para manejar la edición o adición de PCs
function handleSavePC(editingPCId, selectedSala, tipo, marca, modelo, numeroSerie, fechaAdquisicion, estado) {
    if (editingPCId) {
        // Editar PC existente
        pcs[selectedSala] = pcs[selectedSala].map((pc) =>
            pc.id === editingPCId
                ? { id: editingPCId, tipo, marca, modelo, numeroSerie, fechaAdquisicion, estado }
                : pc
        );
    } else {
        // Añadir nuevo PC
        const newPCId = Math.max(...Object.values(pcs).flat().map(pc => pc.id)) + 1;
        const newPC = { id: newPCId, tipo, marca, modelo, numeroSerie, fechaAdquisicion, estado };
        pcs[selectedSala].push(newPC);
    }

    filterBySala();
    closeModal();
}

// Función para manejar la eliminación de PCs
function handleDelete(id, salaId) {
    pcs[salaId] = pcs[salaId].filter((pc) => pc.id !== id);
    filterBySala();
}

// Ejemplo de uso de handleSavePC
// handleSavePC(null, 'sala1', 'Laptop', 'Dell', 'XPS 13', '12345', '2023-01-01', 'Nuevo');
// handleSavePC(1, 'sala1', 'Desktop', 'HP', 'EliteDesk', '67890', '2022-06-15', 'Usado');

// Ejemplo de uso de handleDelete
// handleDelete(1, 'sala1');