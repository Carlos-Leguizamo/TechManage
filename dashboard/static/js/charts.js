document.addEventListener('DOMContentLoaded', function() {
    var ctx = document.getElementById('computersChart').getContext('2d');
    
    var computersChart = new Chart(ctx, {
      type: 'bar', // Gráfico de barras
      data: {
        labels: [ 'Operativos', 'Dados de Baja', 'En Reparación'], 
        datasets: [{
          data: [
            total_computadores_operativos, 
            total_computadores_dañados, 
            total_computadores_en_reparacion
          ], 
          backgroundColor: [
            '#198754', // Color para Operativos
            '#DC3545', // Color para Dados de Baja
            '#FD7E14'  // Color para En Reparación
          ],
          borderColor: [
            '#198754',
            '#DC3545',
            '#FD7E14'
          ],
          borderWidth: 1
        }]
      },
      options: {
        scales: {
          y: {
            beginAtZero: true 
          }
        },
        plugins: {
          legend: {
            display: false 
          }
        }
      }
    });
});
