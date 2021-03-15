function login(){
    if ((login_field.value.toLowerCase() == 'admin') && (password_field.value.toLowerCase() =='kirby')){
        login_field.classList.remove('is-error');
        password_field.classList.remove('is-error');
        login_field.classList.add('is-success');
        password_field.classList.add('is-success');
        location.replace('../../home');
    } else {
        login_field.classList.remove('is-success');
        password_field.classList.remove('is-success');
        login_field.classList.add('is-error');
        password_field.classList.add('is-error');
        login_fail_msg.classList.remove('hidden');
    }
}

function cancel(){
    login_field.value="";
    password_field.value="";

    removeStatusCSS();
}

function removeStatusCSS(){
    login_field.classList.remove('is-error');
    password_field.classList.remove('is-error');
    login_field.classList.remove('is-success');
    password_field.classList.remove('is-success');
    login_fail_msg.classList.add('hidden');
    password_hint.classList.add('hidden');
    login_counter = 0;
}

window.onload = function() {
    document.getElementById('login_btn').addEventListener('click', login);
    document.getElementById('cancel_btn').addEventListener('click', cancel);
    document.getElementById('login-forgot').addEventListener('click', function(){
        document.getElementById('password-hint').classList.remove('hidden');
    });
    login_field = document.getElementById('login_field');
    password_field = document.getElementById('password_field');
    login_fail_msg = document.getElementById('login-fail-alert');
    forgot_password = document.getElementById('login-forgot');
    password_hint = document.getElementById('password-hint');
    login_counter = 0;
    secret_sound = new Audio('../static/misc/secret.mp3')
  };