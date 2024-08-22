function showLoginModal(event) {
    event.preventDefault()
    // document.querySelector('.overlay').classList.add('showOverlay')
    // document.querySelector('.loginForm').classList.add('showloginForm')
    window.location.href = "/accounts/login/";
}
function removeLoginModal() {
    // document.querySelector('.overlay').classList.remove('showOverlay')
    // document.querySelector('.loginForm').classList.remove('showloginForm')
    window.location.href = "/";
}
function googleLogin() {
    window.location.href = "/accounts/google/login/";
}
var loginBtn = document.getElementById('login-Btn')
loginBtn.addEventListener('click', showLoginModal)

var cancelLoginBtn = document.getElementById('cancel')
cancelLoginBtn.addEventListener('click', removeLoginModal)

var google = document.getElementById('google')
google.addEventListener('click',googleLogin)
