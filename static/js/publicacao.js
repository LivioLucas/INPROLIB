// Função para inicializar o estado do botão ao carregar a página
window.onload = function () {
    const termosCheckbox = document.getElementById('termos');
    const submitBtn = document.getElementById('submitBtn');
  
    // Inicia o botão desativado
    submitBtn.disabled = true;
  
    // Adiciona evento de clique no checkbox
    termosCheckbox.addEventListener('change', function () {
      submitBtn.disabled = !termosCheckbox.checked; // Alterna o estado
    });
  };
  