var attempt = 3; // Variable to count number of attempts.
// Below function Executes on click of login button.
function verifyPassword() {
  var username = document.getElementById("exampleInputUsername").value;
  var password = document.getElementById("exampleInputPassword").value;
  if (username == "thoroute" && password == "admin123") {
    location.assign("http://localhost:5500/assets/dashboard/index.html"); 
    console.log("Working!!!");  // Redirecting to other page.
    return false;
  } else {
    attempt--; // Decrementing by one.
    alert("You have " + attempt + " attempts left");
    // Disabling fields after 3 attempts.
    if (attempt == 0) {
      document.getElementById("exampleInputUsername").disabled = true;
      document.getElementById("exampleInputPassword").disabled = true;
      document.getElementById("submitButtin").disabled = true;
      return false;
    }
  }
}
