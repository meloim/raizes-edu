// Espera o carregamento completo do documento
document.addEventListener("DOMContentLoaded", function() {
    // Acha o campo de CEP e adiciona um evento de input (quando o usuário digitar)
    const cepInput = document.getElementById("id_cep");

    // Função para limpar os campos de endereço
    function limparCampos() {
        document.getElementById("id_uf").value = "";
        document.getElementById("id_bairro").value = "";
        document.getElementById("id_rua").value = "";
    }

    // Função para preencher os campos após a busca no ViaCEP
    function preencherCampos(dados) {
        if (dados && !dados.erro) {
            document.getElementById("id_uf").value = dados.uf;
            document.getElementById("id_bairro").value = dados.bairro;
            document.getElementById("id_rua").value = dados.logradouro;
        } else {
            // Caso o CEP não seja encontrado, limpa os campos
            limparCampos();
            alert("CEP não encontrado.");
        }
    }

    // Função para fazer a requisição ao ViaCEP
    function buscarCep(cep) {
        // Limpa os campos antes de fazer uma nova requisição
        limparCampos();

        // Faz a requisição AJAX usando Fetch
        fetch(`https://viacep.com.br/ws/${cep}/json/`)
            .then(response => response.json())
            .then(dados => preencherCampos(dados))
            .catch(error => {
                limparCampos();
                alert("Erro ao buscar o CEP.");
            });
    }

    // Adiciona o evento de mudança (input) ao campo de CEP
    cepInput.addEventListener("blur", function() {
        // Pega o valor do CEP e remove qualquer caractere não numérico
        let cep = cepInput.value.replace(/\D/g, '');

        // Verifica se o CEP tem 8 dígitos
        if (cep.length === 8) {
            buscarCep(cep);
        } else {
            // Se o CEP for inválido (não tem 8 dígitos), limpa os campos
            limparCampos();
            alert("CEP inválido.");
        }
    });
});
