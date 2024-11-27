// Função para formatar CPF para o padrão xxx.xxx.xxx-xx
function formatarCPF(cpf) {
    return cpf.replace(/(\d{3})(\d{3})(\d{3})(\d{2})/, '$1.$2.$3-$4');
}

// Função para validar CPF com regex
function validarCPF(cpf) {
    var regex = /^\d{3}\.\d{3}\.\d{3}-\d{2}$/; // Exemplo de formato: 123.456.789-00
    return regex.test(cpf);
}

// Função para validar todos os campos obrigatórios
function validarFormulario(event) {
    let formIsValid = true; // Variável para verificar se o formulário é válido
    const camposObrigatorios = document.querySelectorAll('input[required], select[required]'); // Todos os campos obrigatórios

    // Limpar bordas vermelhas de todos os campos obrigatórios
    camposObrigatorios.forEach(function(campo) {
        campo.style.border = ''; // Limpa a borda vermelha
    });

    // Verificando campos obrigatórios e CPF
    camposObrigatorios.forEach(function(campo) {
        if (!campo.value.trim()) { // Se o campo estiver vazio
            campo.style.border = '2px solid red'; // Borda vermelha
            formIsValid = false;
        }
    });

    // Validação do CPF
    const cpfField = document.getElementById('id_cpf');
    let cpfValue = cpfField.value.replace(/[^\d]/g, ''); // Remove todos os caracteres não numéricos
    if (cpfValue && !validarCPF(formatarCPF(cpfValue))) {
        cpfField.style.border = '2px solid red'; // Borda vermelha se CPF for inválido
        formIsValid = false;
    } else if (cpfValue && validarCPF(formatarCPF(cpfValue))) {
        cpfField.style.border = ''; // Limpa a borda se CPF for válido
    }

    // Se o formulário não for válido, previne o envio
    if (!formIsValid) {
        event.preventDefault(); // Impede o envio do formulário
        alert("Por favor, preencha todos os campos obrigatórios corretamente.");
    } else {
        // Se o formulário for válido, mostrar um log de sucesso
        console.log("Cadastro concluído com sucesso!");
    }
}

// Função para validar o CPF enquanto o usuário digita (ao vivo)
function validarCPFaoVivo(event) {
    const cpfField = document.getElementById('id_cpf');
    let cpfValue = cpfField.value.replace(/[^\d]/g, ''); // Remove todos os caracteres não numéricos

    // Verifica se o valor contém algum caractere não numérico
    if (/[^0-9]/.test(cpfField.value)) {
        cpfField.style.border = '2px solid red'; // Borda vermelha se houver letra
        event.preventDefault(); // Impede a digitação de caracteres não numéricos
    } else {
        cpfField.style.border = ''; // Limpa a borda se o CPF for válido
    }

    if (cpfValue && !validarCPF(formatarCPF(cpfValue))) {
        cpfField.style.border = '2px solid red'; // Borda vermelha para CPF inválido
    } else {
        cpfField.style.border = ''; // Limpa a borda se o CPF for válido
    }
}

// Adicionando evento de validação ao formulário
document.querySelector("form").addEventListener("submit", validarFormulario);

// Adicionando evento de validação ao campo CPF enquanto o usuário digita
document.getElementById('id_cpf').addEventListener('input', validarCPFaoVivo);
