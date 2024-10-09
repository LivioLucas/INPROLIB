// ------Botão cascata------

document.addEventListener("DOMContentLoaded", function() {
    var dropdowns = document.getElementsByClassName("dropdown-btn");
    for (var i = 0; i < dropdowns.length; i++) {
        dropdowns[i].addEventListener("click", function() {
            this.classList.toggle("active");
            var dropdownContent = this.nextElementSibling;
            if (dropdownContent.style.display === "block") {
                dropdownContent.style.display = "none";
            } else {
                dropdownContent.style.display = "block";
            }
        });
    }
  });
  
  // ------Seções de registro de pessoas------
  
  function mostrarCadastro(entidade) {
  // Esconde todos os cadastros
    var cadastros = document.getElementsByClassName("cadastro");
    for (var i = 0; i < cadastros.length; i++) {
      cadastros[i].style.display = "none";
    }
  
  // Mostra o cadastro correspondente à entidade selecionada
    document.getElementById("cadastro" + entidade.charAt(0).toUpperCase() + entidade.slice(1)).style.display = "block";
  
  // ------ON E OFF 3 DIVS------
  var btnUm = document.querySelector(".ret1");
  var btnDois = document.querySelector(".ret0");
  var btnTrês = document.querySelector(".ret00")
  if (btnUm && btnDois && btnTrês) {
    if (entidade === 'Um') {
        btnUm.classList.add("ativo");
        btnDois.classList.remove("ativo");
        btnTrês.classList.remove("ativo");
      } else if (entidade === 'Dois') {
        btnUm.classList.remove("ativo");
        btnDois.classList.add("ativo");
        btnTrês.classList.remove("ativo");
      } else if (entidade === 'Três') {
        btnUm.classList.remove("ativo");
        btnDois.classList.remove("ativo");
        btnTrês.classList.add("ativo");
  }
  }
  
  // ------SELEÇÃO NO BOTÃO USUÁRIOS PARA QUANDO A PÁGINA CARREGAR------
  document.addEventListener("DOMContentLoaded", function() {
    var btnUm = document.querySelector(".ret1");
    var btnDois = document.querySelector(".ret0");
    var btnTrês = document.querySelector(".ret00");
  
    if (btnUm && btnDois && btnTrês) {
      btnUm.classList.add("ativo");
      btnDois.classList.remove("ativo");
      btnTrês.classList.remove("ativo");
    }
  });
  
  // ------ON E OFF 2 DIVS ------
  var btnUm2 = document.querySelector(".ret1");
  var btnDois2 = document.querySelector(".ret0");
  if (btnUm2 && btnDois2) {
    if (entidade === 'Um') {
        btnUm2.classList.add("ativo");
        btnDois2.classList.remove("ativo");
      } else if (entidade === 'Dois') {
        btnUm2.classList.remove("ativo");
        btnDois2.classList.add("ativo");
      }
  }
  
  // ------SELEÇÃO NO BOTÃO USUÁRIOS PARA QUANDO A PÁGINA CARREGAR------
  document.addEventListener("DOMContentLoaded", function() {
    var btnUm2 = document.querySelector(".ret1");
    var btnDois2 = document.querySelector(".ret0");
  
    if (btnUm2 && btnDois2) {
      btnUm2.classList.add("ativo");
      btnDois2.classList.remove("ativo");
    }
  });
  }
  document.addEventListener("DOMContentLoaded", function() {
    mostrarCadastro('Um'); 
  // A entidade inicial que será mostrada ao carregar a página
  });
  document.addEventListener("DOMContentLoaded", function() {
    mostrarCadastro('Um'); 
  // A entidade inicial que será mostrada ao carregar a página
  });

  // Seleciona o botão de alternar modo
const toggleButton = document.getElementById('toggleMode');

// Função para alternar a cor de fundo entre claro e escuro
toggleButton.addEventListener('click', () => {
  // Pega o valor atual da variável CSS
  const currentBgColor = getComputedStyle(document.documentElement)
    .getPropertyValue('--bs-body-bg').trim();

  // Se a cor atual for branca, muda para cinza escuro, senão volta para branco
  if (currentBgColor === '#fff') {
    document.documentElement.style.setProperty('--bs-body-bg', '#2c2c2c');
    document.body.style.color = '#fff';  // Mudando a cor do texto para ficar visível no fundo escuro
  } else {
    document.documentElement.style.setProperty('--bs-body-bg', '#fff');
    document.body.style.color = 'black';  // Voltando a cor do texto ao normal
  }
});