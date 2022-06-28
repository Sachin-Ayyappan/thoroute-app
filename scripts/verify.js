function verifyPassword() {  
    var pw = document.getElementById("pswd").value;  
    var us = document.getElementById("usnm").value; 
    if(pw == "password" && us=="admin") {
        window.location.href = "../index.html";
        alert("Vro, y this no redir?");
    }  
    else{
        alert("Not so success vro!! :(");
    }
}
function redir(){
    window.location.href("https://www.google.com")
}
