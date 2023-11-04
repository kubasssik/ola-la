

const $registrInputPassword = document.querySelectorAll('.eye')
const $input = document.querySelectorAll('input')


//Глаз
$registrInputPassword.forEach(eye => {
    eye.addEventListener('click', showPassword)
})

function showPassword() {
    if (this.textContent === 'visibility_off') {
        this.textContent = 'visibility'
        this.previousElementSibling.type = 'text'
    }
    else {
        this.textContent = 'visibility_off'
        this.previousElementSibling.type = 'password'
    }
}

//placeholder
$input.forEach(input => {
    input.addEventListener('focus', showpPlaceholder)
})
$input.forEach(input => {
    input.addEventListener('blur', hidePlaceholder)
})

let p
function showpPlaceholder() {
    p = this.placeholder
    this.placeholder = ''
}

function hidePlaceholder() {
    this.placeholder = p 
}
