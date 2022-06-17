const secretKeyEl = document.querySelector('#secret_key');
const emailEl = document.querySelector('#email');
const passwordEl = document.querySelector('#password');
const confirmPasswordEl = document.querySelector('#confirm-password');
const form = document.querySelector('#signup');

const checkEmail = () => {
    let valid = false;
    const email = emailEl.value.trim();
    if (!isRequired(email)) {
        showError(emailEl, 'ایمیل نمیتواند خالی باشد!');
    } else if (!isEmailValid(email)) {
        showError(emailEl, 'فرمت ایمیل درست نیست!')
    } else {
        showSuccess(emailEl);
        valid = true;
    }
    return valid;
};

const checkSecretKey = () => {
    let valid = false;
    const max = 128;

    const secretKey = secretKeyEl.value.trim();

    if (!isRequired(secretKey)) {
        showError(secretKeyEl, 'سکرت کی نمیتواند خالی باشد!');
    } else if (!isBetween(secretKey.length,max)) {
        showError(secretKeyEl, `سکرت کی باید ${max} کاراکتر باشد !`)
    } else {
        showSuccess(secretKeyEl);
        valid = true;
    }
    return valid;
};

const checkPassword = () => {
    let valid = false;
    const password = passwordEl.value.trim();
    if (!isRequired(password)) {
        showError(passwordEl, 'پسورد نمیتواند خالی باشد!');
    } else if (!isPasswordSecure(password)) {
        showError(passwordEl, 'گذرواژه باید حداقل 8 حرف داشته باشد که 1 کاراکتر کوچک ، 1 کاراکتر بزرگ ، 1 شماره و 1 کاراکتر ویژه از (!@#$ ٪^&*) باشد!');
    } else {
        showSuccess(passwordEl);
        valid = true;
    }

    return valid;
};

const checkConfirmPassword = () => {
    let valid = false;
    const confirmPassword = confirmPasswordEl.value.trim();
    const password = passwordEl.value.trim();

    if (!isRequired(confirmPassword)) {
        showError(confirmPasswordEl, 'پسورد تکرار نباید خالی باشد!');
    } else if (password !== confirmPassword) {
        showError(confirmPasswordEl, 'پسورد تکرار یکسان نیست!');
    } else {
        showSuccess(confirmPasswordEl);
        valid = true;
    }

    return valid;
};

const isEmailValid = (email) => {
    const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
};

const isPasswordSecure = (password) => {
    const re = new RegExp("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#\$%\^&\*])(?=.{8,})");
    return re.test(password);
};

const isRequired = value => value === '' ? false : true;
const isBetween = (length, min, max) => length < min || length > max ? false : true;


const showError = (input, message) => {
    const formField = input.parentElement;
    formField.classList.remove('success');
    formField.classList.add('error');

    const error = formField.querySelector('small');
    error.textContent = message;
};

const showSuccess = (input) => {
    const formField = input.parentElement;

    formField.classList.remove('error');
    formField.classList.add('success');

    const error = formField.querySelector('small');
    error.textContent = '';
}


form.addEventListener('submit', function (e) {
    e.preventDefault();

   let isSecretKeyisValid = checkSecretKey(),
        isEmailValid = checkEmail(),
        isPasswordValid = checkPassword(),
        isConfirmPasswordValid = checkConfirmPassword();

    let isFormValid = isSecretKeyisValid &&
        isEmailValid &&
        isPasswordValid &&
        isConfirmPasswordValid;

    if (isFormValid) {
        e.currentTarget.submit()
    }
});


const debounce = (fn, delay = 1) => {
    let timeoutId;
    return (...args) => {
        if (timeoutId) {
            clearTimeout(timeoutId);
        }
        timeoutId = setTimeout(() => {
            fn.apply(null, args)
        }, delay);
    };
};

form.addEventListener('input', debounce(function (e) {
    switch (e.target.id) {
        case 'secret_key':
            checkSecretKey();
            break;
        case 'email':
            checkEmail();
            break;
        case 'password':
            checkPassword();
            break;
        case 'confirm-password':
            checkConfirmPassword();
            break;
    }
}));