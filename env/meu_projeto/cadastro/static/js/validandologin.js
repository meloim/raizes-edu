// forms.js

document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const formData = new FormData(event.target);

    fetch('/login/', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        const feedbackMessage = document.getElementById('feedbackMessage');
        
        if (data.status === 'error') {
            // Exibir mensagem de erro
            feedbackMessage.textContent = data.message;
            feedbackMessage.style.display = 'block';
            feedbackMessage.style.backgroundColor = '#ff6347'; // Cor de fundo vermelha para erro
        } else if (data.status === 'success') {
            // Exibir mensagem de sucesso
            feedbackMessage.textContent = data.message;
            feedbackMessage.style.display = 'block';
            feedbackMessage.style.backgroundColor = '#4caf50'; // Cor de fundo verde para sucesso
            
            // Redirecionar para a página homelider após 2 segundos
            setTimeout(() => {
                window.location.href = '/homelider/';
            }, 2000);
        }
    })
    .catch(error => {
        console.error('Erro:', error);
    });
});