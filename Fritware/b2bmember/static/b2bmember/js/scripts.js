const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});


function disp(){
    alert("This is on click alart")
}


console.log('scripts.js is loaded');  // Debug line

function validatePasswords() {
    console.log('validatePasswords() is called');  // Debug line

    const password1 = document.getElementById('password1').value;
    const password2 = document.getElementById('password2').value;
    const errorDiv = document.getElementById('password-error');

    // Create error div if not already in template
    if (!errorDiv) {
        const newErrorDiv = document.createElement('div');
        newErrorDiv.id = 'password-error';
        newErrorDiv.className = 'error';
        newErrorDiv.style.color = 'red';
        newErrorDiv.style.marginBottom = '10px';
        const form = document.querySelector('form');
        form.insertBefore(newErrorDiv, form.querySelector('button'));
    }

    if (password1 !== password2) {
        document.getElementById('password-error').textContent = "Passwords do not match!";
        return false;  // Prevent submission
    } else {
        document.getElementById('password-error').textContent = "";
        return true;   // Allow form submit
    }
}
