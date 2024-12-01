document.getElementById('loginForm').addEventListener('submit', async function(event) {
    event.preventDefault();  // Previne o envio padrão do formulário

    // Pegando os valores dos inputs
    const login = document.getElementById('login').value.trim();
    const password = document.getElementById('password').value.trim();

    // Referência ao modal
    const modal = document.getElementById('customModal');
    const modalMessage = document.getElementById('modalMessage');
    const closeModal = document.getElementsByClassName('close')[0];

    // Função para abrir o modal com a mensagem
    function showModal(message) {
        modalMessage.textContent = message;
        modal.style.display = 'block';
    }

    // Função para fechar o modal
    closeModal.onclick = function() {
        modal.style.display = 'none';
    };

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    };

    // Verificando se os campos estão vazios
    if (!login || !password) {
        showModal('Por favor, preencha todos os campos.');
        return;
    }

    // Verifica se o login está no formato de um e-mail
    const regex = /^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/; 
    if (!regex.test(login)) {
        showModal('Por favor, insira um e-mail válido.');
        return;
    }

    // Verifica se o login tem o formato esperado (ex: pelo menos 3 caracteres)
    if (login.length < 3) {
        showModal('O login deve ter pelo menos 3 caracteres.');
        return;
    }

    // Verifica se a senha tem o formato esperado (ex: pelo menos 6 caracteres)
    if (password.length < 6) {
        showModal('A senha deve ter pelo menos 6 caracteres.');
        return;
    }

    // Envia os dados para o servidor usando Fetch API
    try {
        const response = await fetch('/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: new URLSearchParams({
                login: login,
                password: password
            })
        });

        const result = await response.json();

        if (result.status === 'success') {
            // Redireciona para a página de repositórios ou qualquer outra página de sucesso
            window.location.href = '/repositorios';
        } else if (result.status === 'not_found') {
            showModal('Usuário inexistente');
        } else {
            showModal(result.message || 'Erro desconhecido ao fazer login');
        }

    } catch (error) {
        console.error('Erro na requisição:', error);
        showModal('Erro ao se conectar com o servidor.');
    }
});
