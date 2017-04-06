$(function () {
    var lineData = {
        labels: ["1", "2", "3", "4", "5", "6", "7","8","9","10"],
        datasets: [
            {
                label: "funcion",
                backgroundColor: 'rgba(26,179,148,0.5)',
                borderColor: "rgba(26,179,148,0.7)",
                pointBackgroundColor: "rgba(26,179,148,1)",
                pointBorderColor: "#fff",
                data: [28, 48, 40, 19, 86, 27, 90,8,9,10]
            }
        ]
    };
    var lineOptions = {
        responsive: true
    };
    var ctx = document.getElementById("lineChart").getContext("2d");
    new Chart(ctx, {type: 'line', data: lineData, options:lineOptions});
});