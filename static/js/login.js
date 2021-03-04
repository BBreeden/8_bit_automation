function login(){
    login_field = document.getElementById('login_field');
    password_field = document.getElementById('password_field');

    if ((login_field.value.toLowerCase() == 'admin') && (password_field.value.toLowerCase() =='kirby')){
        login_field.classList.remove('is-error');
        password_field.classList.remove('is-error');
        login_field.classList.add('is-success');
        password_field.classList.add('is-success');
    } else {
        login_field.classList.remove('is-success');
        password_field.classList.remove('is-success');
        login_field.classList.add('is-error');
        password_field.classList.add('is-error');
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