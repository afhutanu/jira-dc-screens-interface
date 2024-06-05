function updateForm() {
    var authType = document.querySelector('input[name="auth_type"]:checked').value;
    let basicForm = document.getElementById('basicForm');
    let bearerForm = document.getElementById('bearerForm');

    basicForm.style.display = "none";
    bearerForm.style.display = "none";

    if(authType == 'basic') 
        basicForm.style.display = "block";
    else
        bearerForm.style.display = "block";
}

