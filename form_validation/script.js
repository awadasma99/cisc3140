/**  Example of form validation for class CISC3140
     Brooklyn College
     author: @katychuang
     url: http://github.com/DataMascara/cisc3140
**/

function checkVal(v){
  /* uncomment the line below to view v in the console */
  //console.log(v);
  console.log(v.value);

  let log = document.querySelector('p');

  //display placeholder
  if (v.value.length > 4){
    log.textContent = `the value is ${v.value.length} character(s) long`;
  }

  if (v.value.length > 10) {
    // conditional to show submit button
    document.getElementById("submit").classList.remove("hidden");
  }
}

function whitespacing(v){
    let enteredValue = document.querySelector('input#inputmask');

    if (v.match(/^\d{4}$/) !== null) {
      enteredValue.value = v + ' ';
    } else if (v.match(/^\d{4}\ \d{4}$/) !== null) {
      enteredValue.value = v + ' ';
    }
}
