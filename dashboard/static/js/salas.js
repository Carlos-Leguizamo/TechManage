document.addEventListener("DOMContentLoaded", function () {
  var ctx = document.getElementById("combinedChart").getContext("2d");

  var combinedChart = new Chart(ctx, {
    type: "bar",
    data: {
      labels: ["Salas", "Reportes"],
      datasets: [
        {
          data: [total_salas, total_reportes],
          backgroundColor: ["#007bff", "#ffc107"],
          borderColor: ["#28a745", "#ffc107"],
          borderWidth: 1,
        },
      ],
    },
    options: {
      scales: {
        y: {
          beginAtZero: true,
          ticks: {
            stepSize: 2, 
          },
        },
      },
      plugins: {
        legend: {
          display: false, 
        },
      },
    },
  });
});
