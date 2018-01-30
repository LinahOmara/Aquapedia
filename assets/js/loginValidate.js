var myUsers = [
    {user_username:"aya", user_password:"123"},
    {user_username:"iman", user_password:"123"},
    {user_username:"possy", user_password:"123"},
    {user_username:"linah", user_password:"123"}
    ]

//Below function Executes on click of login button
function validate(){
	var username = document.getElementById("username").value;
	var password = document.getElementById("password").value;

for ( var i = 0 ; i < myUsers.length ; i ++){
	if ( username == myUsers[i].user_username && password == myUsers[i].user_password)
	{
		alert ("Login successfully");
		window.location.href = "customer.html"; //redirecting to other page
		return false;
	}
  }alert ("Wrong Username or password");
}