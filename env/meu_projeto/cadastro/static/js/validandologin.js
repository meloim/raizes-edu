document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const form = event.target;
    const formData = new FormData(form);

    fetch(form.action, {
        method: 'POST',
        body: formData,
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
        },
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        const feedbackMessage = document.getElementById('feedbackMessage');
        feedbackMessage.textContent = data.message;
        feedbackMessage.style.display = 'block';

        if (data.success) {
            feedbackMessage.style.backgroundColor = 'green';
            setTimeout(() => {
                window.location.href = "{% url 'homelider' %}";
            }, 1000);
        } else {
            feedbackMessage.style.backgroundColor = 'red';
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});