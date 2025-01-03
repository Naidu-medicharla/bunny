function scrollToSection(sectionId) {
    const section = document.getElementById(sectionId);
    if (section) {
        section.scrollIntoView({ behavior: 'smooth' });
    }
}
function clearForm(event) {
    event.preventDefault();
    const form = document.getElementById('contact-form');
    const messageDiv = document.getElementById('form-message');
    const formData = new FormData(form);

    fetch(form.action, {
        method: 'POST',
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
        },
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            messageDiv.textContent = 'Message sent successfully!';
            messageDiv.style.color = 'green';
            form.reset(); // Clear the form inputs
        } else {
            messageDiv.textContent = 'Failed to send message. Please try again.';
            messageDiv.style.color = 'red';
        }
    })
    .catch(error => {
        messageDiv.textContent = 'An error occurred. Please try again later.';
        messageDiv.style.color = 'red';
        console.error('Error:', error);
    });
}
