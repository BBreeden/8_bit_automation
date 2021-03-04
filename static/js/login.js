function login(){
    login = document.getElementById('login_field').value;
    password = document.getElementById('password_field').value;

    if ((login.toLowerCase() == 'admin') && (password.toLowerCase() =='kirby')){
        console.log('login success');
    } else {
        console.log('login failed');
    }
}

function cancel(){
    login_field = document.getElementById('login_field');
    password_field = document.getElementById('password_field');
    
    login_field.value="";
    password_field.value="";
}

window.onload = function() {
    document.getElementById('login_btn').addEventListener('click', login);
    document.getElementById('cancel_btn').addEventListener('click', cancel);
  };