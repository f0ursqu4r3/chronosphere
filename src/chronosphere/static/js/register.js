import { SUPABASE_ANON_KEY, SUPABASE_URL } from './constants.js'

const validateForm = () => {
    const email = document.getElementById('email').value
    const password = document.getElementById('password').value
    const confirmPassword = document.getElementById('password-confirm').value

    if (!email || !password || !confirmPassword) {
        alert('All fields are required')
        return false
    }

    if (password !== confirmPassword) {
        alert('Passwords do not match')
        return false
    }

    return true
}

const register = async (event) => {
    event.preventDefault()

    if (!validateForm()) {
        return
    }

    const email = document.getElementById('email').value
    const password = document.getElementById('password').value

    const client = supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY)

    try {
        const { data, error } = await client.auth.signUp({
            email,
            password,
        })

        if (error) {
            throw error
        }

        console.log('Registration successful:', data)
        alert('Registration successful! Please check your email to confirm your account.')
        window.location.href = '/'
    } catch (error) {
        console.error('Registration error:', error.message)
        alert(`Registration failed: ${error.message}`)
    }
}

const checkPasswordMatch = () => {
    const password = document.getElementById('password').value
    const confirmPassword = document.getElementById('password-confirm').value
    const submitButton = document.querySelector('button[type="submit"]')

    submitButton.disabled = password !== confirmPassword
}

document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('register-form')
    const passwordConfirmInput = document.getElementById('password-confirm')

    form.addEventListener('submit', register)
    passwordConfirmInput.addEventListener('input', checkPasswordMatch)
    document.getElementById('password').addEventListener('input', checkPasswordMatch)
})