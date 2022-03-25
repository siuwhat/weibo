/* globals Chart:false, feather:false */


  $(document).ready(function(){ $('#show').click(function(){
       $('#show').click(func(0))
        setInterval(function (){func()},700)
     });});
  function func(f) {
    console.log('no');
    $.ajax({
      'url':'/about',
      'type':'get',
      'data':{'flag':f},
      success:function (data)
      {$("#tablebody").append('<tr>')
        var str=""
        for(var i in data.data)
        {
          str+="<td>";
          str+=data.data[i];
          str+="</td>";
        }
        console.log("where is str"+str);
        console.log(data);
        $("#tablebody").append(str+'</tr>')
      }
    })};



(function () {
  'use strict'

  feather.replace({ 'aria-hidden': 'true' })

  // Graphs
  var ctx = document.getElementById('myChart')
  // eslint-disable-next-line no-unused-vars
  var myChart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: [
        'Sunday',
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday'
      ],
      datasets: [{
        data: [
          15339,
          21345,
          18483,
          24003,
          23489,
          24092,
          12034
        ],
        lineTension: 0,
        backgroundColor: 'transparent',
        borderColor: '#007bff',
        borderWidth: 4,
        pointBackgroundColor: '#007bff'
      }]
    },
    options: {
      scales: {
        yAxes: [{
          ticks: {
            beginAtZero: false
          }
        }]
      },
      legend: {
        display: false
      }
    }
  })
})()
