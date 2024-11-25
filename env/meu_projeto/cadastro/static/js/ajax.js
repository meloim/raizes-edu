function preencherEndereco(dados) {
    if (dados.erro) {
        alert("CEP não encontrado.");
    } else {
        document.getElementById("id_rua").value = dados.logradouro || '';
        document.getElementById("id_bairro").value = dados.bairro || '';
        document.getElementById("id_uf").value = dados.uf || '';
        document.getElementById("id_complemento").value = dados.complemento || '';
    }
}

function buscarCep() {
    const cep = document.getElementById("id_cep").value.replace(/\D/g, ''); // Remove caracteres não numéricos

    if (cep.length === 8) { // Verifica se o CEP tem 8 dígitos
        fetch(`/buscar_cep/?cep=${cep}`)  // Envia a requisição AJAX para a view do Django
            .then(response => response.json())
            .then(data => preencherEndereco(data))
            .catch(error => alert('Erro ao buscar o CEP.'));
    }
}

// Adiciona um evento para chamar a função buscarCep sempre que o campo de CEP perder o foco
document.getElementById("id_cep").addEventListener("blur", buscarCep);
