function verifyPassword() {  
    var pw = document.getElementById("exampleInputUsername").value;  
    var us = document.getElementById("exampleInputPassword").value; 
    if(pw=="password" && us=="admin") {
        window.location.href="../dashboard/index.html";
        alert("Vro, y this no redir?");
    }  
    else{
        alert("Not so success vro!! :(");
    }
}
