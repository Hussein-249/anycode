/*
Filename:     index.js
Description:  js file to provide functionality to the Exchange Rates Mini web application.
              This project is currently under construction.

              QOL updates required: {
                Write out full currency name
                Add axes labels and scale correctly to work on mobile devices
                Responsive CSS
              }

Author:       Hussein Adi
*/

// declaring all required elements
// exchange rate button
const addButtonElement = document.getElementById("erButton");

// clear fields and delete chart button
const clearButtonElement = document.getElementById("clearERButton");

// results section
const resultsElement = document.getElementById("results");

// canvas for chart.js
const chartsTEMPORARY = document.getElementById("Week Chart");

var againstCurrencyElement = document.getElementById("againstcurrency");

// creating an array of dates
let datesArray = getPastWeekDates().reverse();

let baseURL = 'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/';

addButtonElement.onclick = () => {
    getRates(datesArray);
}

clearButtonElement.onclick = () => {

  document.getElementById("basecurrency").value = '';
  document.getElementById("againstcurrency").value = '';
}

// WIP functionality make clear button reset input fields and delete chart 

// event listening for enter key on second form
// calls getRates() like when button is clicked
againstCurrencyElement.addEventListener("keyup", function(event) {
  if (event.key === "Enter") {
      getRates(datesArray);
  }
});

window.onload = function() {
  document.querySelectorAll('input').forEach(function(input) {
    input.value = '';
  });
}

document.addEventListener("keyup", function(event) {
  if (event.key === "Delete") {
    document.getElementById("basecurrency").value = '';
    document.getElementById("againstcurrency").value = '';
  }
})

/* ##################################### */

// getRates must be an async function to allow promises
// await all promises before generating the chart.js chart
async function getRates(datesArray) {

    // retrieve the value of the input currency field
    var inputCurrency = document.getElementById("basecurrency").value;

    // retrieve the value of the against currency field
    var againstCurrency = document.getElementById("againstcurrency").value;

    // convert the input fields to lowercase
    // this is because the API request must have the currencies in lowercase
    inputCurrency = inputCurrency.toLowerCase();

    againstCurrency = againstCurrency.toLowerCase();

    var inputCurrencyUpper = inputCurrency.toUpperCase();

    var againstCurrencyUpper = againstCurrency.toUpperCase();

    // construct the API URL to fetch the currency data
    var newURL = baseURL + "latest/currencies/" + inputCurrency + ".json"

    // fetch API request
    fetch(newURL)
        .then(response => response.json())
        // store the data in the variable named "rates"
        .then(data => {var rates = data;

            // edit the results HTML to show the rate
            resultsElement.innerHTML = "1 " + inputCurrencyUpper + " is equal to " + rates[inputCurrency][againstCurrency] + " " + againstCurrencyUpper;
            
        })

    let valuesArray = [];
  
    // declare promises array
    // await will later await for all promises to be resolved
    let promises = [];
    
    // for loop to fetch the exchange rate for each date over the past week
    for (let i = 0; i < 7; i++) {

      // URL changes depending on the date 
      newURL = baseURL + datesArray[i] + "/currencies/" + inputCurrency + ".json";

      // promise
      promises.push(fetch(newURL)
        .then(response => response.json())

        // store the data in the variable named "rates"
        .then(data => {var rates = data;

          valuesArray.push(rates[inputCurrency][againstCurrency]);

        })
      );
    }
      
      // await for the promises so that the chart is not created before data is retrieved
      await Promise.all(promises);
      
      // reverse values array
      valuesArray = valuesArray.reverse();
      
      // create chart object using chart.js library functions
      const myChart = new Chart("rateChart", {
        type: "line",
        data: {
          labels: datesArray,
          datasets: [{
            fill: false, 
            lineTension: 0,

            // points colour
            backgroundColor:"#000000",

            // line colour
            borderColor: "#000000",
            data: valuesArray
          }]
        },

        options:{

          scales: {
            yAxes: [{
              ticks: {
                stepSize: 0.01
              }
            }]
          },

          legend: {display: false},

          title : {display: true,
                  text: 'Conversion Rate over the past week between ' + inputCurrencyUpper + " and " + againstCurrencyUpper,
                  fontSize: 20,
                  // fontfamily: 'Raleway'
                  }
          
        }
      });
    }

/* ##################################### */

function getPastWeekDates() {
  
  // declare array that will be returned
  let datesArray = [];
  
  // loop 7 times for each of the seven dates
  // over the past week
  for (let i = 0; i < 7; i++) {
      
      // declare a new date object
      let date = new Date();

      // get today's date when i = 0
      // the previous days when i > 0
      date.setDate(date.getDate() - i);

      // get the current month, day, and year
      // store in variables
      let month = '' + (date.getMonth() + 1);
      let day = '' + date.getDate();
      let year = date.getFullYear();

      // format the month to mm format
      if (month.length < 2) month = '0' + month;

      // format the day to dd format
      if (day.length < 2) day = '0' + day;

      // join the years, month, and day variables with "-"
      // push the final string to the results array
      datesArray.push([year, month, day].join('-'));
  }
  return datesArray;
}
/* End of file */