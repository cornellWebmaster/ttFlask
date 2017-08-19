
function validateForm(){
var form = document.forms["form_52391084313147"];
var name = form["input_1"].value;
var email = form["input_2"].value;
var resume = form["input_3"].value;
var headshot = form["input_4"].value;

if(name == null || name == ""){
    alert("Name is Missing");
    return false;
}

if(email == null || email == ""){
    alert("Email is Missing");
    return false;
}

if(resume == null || resume == ""){
    alert("Resume is Missing");
    return false;
}

if(headshot == null || headshot == ""){
    alert("Headshot is Missing");
    return false;
}
return true;
}