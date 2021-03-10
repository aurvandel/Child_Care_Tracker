(function() {
    var days = ['Sun','Mon','Tue','Wed','Thur','Fri','Sat'];

    var months = ['Jan','Feb','Mar','Arp','May','June','July','Aug','Sept','Oct','Nov','Dec'];

    Date.prototype.getMonthName = function() {
        return months[ this.getMonth() ];
    };
    Date.prototype.getDayName = function() {
        return days[ this.getDay() ];
    };
})();

function currentTime() {
  var date = new Date(); /* creating object of Date class */
  var hour = date.getHours();
  var min = date.getMinutes();
  var sec = date.getSeconds();
  var day = date.getDayName();
  var month = date.getMonthName();
  var year = date.getFullYear();
  var midday = "AM";
  midday = (hour >= 12) ? "PM" : "AM"; /* assigning AM/PM */
  hour = (hour == 0) ? 12 : ((hour > 12) ? (hour - 12): hour); /* assigning hour in 12-hour format */
  hour = updateTime(hour);
  min = updateTime(min);
  sec = updateTime(sec);
  document.getElementById("clock").innerHTML = hour + " : " + min + " : " + sec + " " + midday; /* adding time to the div */
  document.getElementById("date").innerHTML = day + ", " + month + " " + " " + year;
  var t = setTimeout(currentTime, 1000); /* setting timer */
}

function updateTime(k) { /* appending 0 before time elements if less than 10 */
  if (k < 10) {
    return "0" + k;
  }
  else {
    return k;
  }
}

