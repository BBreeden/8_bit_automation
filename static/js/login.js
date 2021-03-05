function login(){
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
        login_fail_msg.classList.remove('hidden');
        login_counter++;

        if (login_counter == 3) {
            forgot_password.classList.remove('hidden');
            secret_sound.play()
        }
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
    forgot_password.classList.add('hidden');
    login_fail_msg.classList.add('hidden');
    login_counter = 0;
}

window.onload = function() {
    document.getElementById('login_btn').addEventListener('click', login);
    document.getElementById('cancel_btn').addEventListener('click', cancel);
    login_field = document.getElementById('login_field');
    password_field = document.getElementById('password_field');
    login_fail_msg = document.getElementById('login-fail-alert');
    forgot_password = document.getElementById('login-forgot');
    login_counter = 0;
    secret_sound = new Audio('../static/misc/secret.mp3')
  };