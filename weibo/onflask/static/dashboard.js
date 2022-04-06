/* globals Chart:false, feather:false */
var start=0;
 $(document).ready(function(){ $('#stop').click(function(){
       $('#stop').click(clearInterval(start))

     });});
 $(document).ready(function(){ $('#stop2').click(function(){
       $('#stop').click(clearInterval(start))

     });});


  $(document).ready(function(){ $('#show').click(function(){
       $('#show').click(func(0))
      start=setInterval(function (){func()},700)

     });});
  function func(f) {
    console.log('no');
    $.ajax({
      'url':'/about',
      'type':'get',
      'data':{'flag':f},
      'async':true,
      success:function (data)
      {
        if(data.data==="-1")
        {alert("要展示的数据库不存在");document.location.reload();}
        else if(data.data==='-2')
        {alert("要展示的数据库内的数据为空");document.location.reload();}
        else
        {$("#tablebody").append('<tr>')
        var str=""
        var flag=data.data[0];
        for(var i in data.data)
        {
          if (flag%2===0){
            console.log(i)
            str+="<td"+"  style=\'text-align:center;vertical-align:middle;font-size:14px;width:100px;height: 120px;\'"+">";}

          else{
            console.log(i)
               str+="<td"+" style=\'text-align:center;vertical-align:middle;font-size:14px;width:100px;height: 120px;background-color:lightgray\'"+">";}


          str+=data.data[i];
          str+="</td>";
        }
        console.log("where is str"+str);
        console.log(data);
        $("#tablebody").append(str+'</tr>')
      }}
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
