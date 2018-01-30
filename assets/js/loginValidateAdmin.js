var attempt = 3; //Variable to count number of attempts
var mypass = "123";
var myUser = "admin";

//Below function Executes on click of login button
function validateadmin(){
	var username = document.getElementById("usernameadmin").value;
	var password = document.getElementById("passwordadmin").value;

	if ( username == myUser && password == mypass){
		alert ("Login successfully");
		window.location.href = "company.html"; //redirecting to other page
		return false;
	}
	else{
		attempt --;//Decrementing by one
//		alert("You have left "+attempt+" attempt;");
		alert ( " pass = " + mypass + ", user = "+ myUser + "your pass = " + password + "ur username = " + username);
		
		//Disabling fields after 3 attempts
		if( attempt == 0){
			document.getElementById("username").disabled = true;
			document.getElementById("password").disabled = true;
			document.getElementById("submit").disabled = true;
			return false;
		}
	}
}