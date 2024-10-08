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
  

// ------ON E OFF PESSOAS------

var btnUsuarios = document.querySelector(".ret1");
var btnFornecedores = document.querySelector(".ret0");
var btnClientes = document.querySelector(".ret00")
if (btnUsuarios && btnFornecedores && btnClientes) {
    if (entidade === 'usuarios') {
        btnUsuarios.classList.add("ativo");
        btnFornecedores.classList.remove("ativo");
        btnClientes.classList.remove("ativo");
      } else if (entidade === 'fornecedores') {
        btnUsuarios.classList.remove("ativo");
        btnFornecedores.classList.add("ativo");
        btnClientes.classList.remove("ativo");
      } else if (entidade === 'clientes') {
        btnUsuarios.classList.remove("ativo");
        btnFornecedores.classList.remove("ativo");
        btnClientes.classList.add("ativo");
  }
}


// ------SELEÇÃO NO BOTÃO USUÁRIOS PARA QUANDO A PÁGINA CARREGAR------
document.addEventListener("DOMContentLoaded", function() {
    var btnUsuarios = document.querySelector(".ret1");
    var btnFornecedores = document.querySelector(".ret0");
    var btnClientes = document.querySelector(".ret00");
  
    if (btnUsuarios && btnFornecedores && btnClientes) {
      btnUsuarios.classList.add("ativo");
      btnFornecedores.classList.remove("ativo");
      btnClientes.classList.remove("ativo");
    }
  });

// ------ON E OFF PRODUÇÃO------

var btnEntradas = document.querySelector(".ret1");
var btnProdutos = document.querySelector(".ret0");
var btnSubprodutos = document.querySelector(".ret00")
if (btnEntradas && btnProdutos && btnSubprodutos) {
    if (entidade === 'entradas') {
        btnEntradas.classList.add("ativo");
        btnProdutos.classList.remove("ativo");
        btnSubprodutos.classList.remove("ativo");
      } else if (entidade === 'produtos') {
        btnEntradas.classList.remove("ativo");
        btnProdutos.classList.add("ativo");
        btnSubprodutos.classList.remove("ativo");
      } else if (entidade === 'subprodutos') {
        btnEntradas.classList.remove("ativo");
        btnProdutos.classList.remove("ativo");
        btnSubprodutos.classList.add("ativo");
  }
}

// ------SELEÇÃO NO BOTÃO PRODUÇÃO PARA QUANDO A PÁGINA CARREGAR------

document.addEventListener("DOMContentLoaded", function() {
  var btnEntradas = document.querySelector(".ret1");
  var btnProdutos = document.querySelector(".ret0");
  var btnSubprodutos = document.querySelector(".ret00");

  if (btnEntradas && btnProdutos && btnSubprodutos) {
    btnEntradas.classList.add("ativo");
    btnProdutos.classList.remove("ativo");
    btnSubprodutos.classList.remove("ativo");
  }
});

// ------ON e OFF Lançamentos------

var btnOrdem_producao = document.querySelector(".ret1");
var btnLan_entradas = document.querySelector(".ret0");
if (btnOrdem_producao && btnLan_entradas) {
    if (entidade === 'Ordem_producao') {
        btnOrdem_producao.classList.add("ativo");
        btnLan_entradas.classList.remove("ativo");
      } else if (entidade === 'Lan_entradas') {
        btnOrdem_producao.classList.remove("ativo");
        btnLan_entradas.classList.add("ativo");
}
}

// Se quiser colocar mais uma div mostrarCadastro,
// extenda a chave

// ------SELEÇÃO NO BOTÃO LANÇAMENTO PARA QUANDO A PÁGINA CARREGAR------

document.addEventListener("DOMContentLoaded", function() {
  var btnOrdem_producao = document.querySelector(".ret1");
  var btnLan_entradas = document.querySelector(".ret0");

  if (btnOrdem_producao && btnLan_entradas) {
    btnOrdem_producao.classList.add("ativo");
    btnLan_entradas.classList.remove("ativo");
  }
});

// ------ON E OFF EstOQUE------

var btnEst_Entradas = document.querySelector(".ret1");
var btnEst_Produtos = document.querySelector(".ret0");
var btnEst_Subprodutos = document.querySelector(".ret00")
if (btnEst_Entradas && btnEst_Produtos && btnEst_Subprodutos) {
    if (entidade === 'Est_Entradas') {
        btnEst_Entradas.classList.add("ativo");
        btnEst_Produtos.classList.remove("ativo");
        btnEst_Subprodutos.classList.remove("ativo");
      } else if (entidade === 'Est_Produtos') {
        btnEst_Entradas.classList.remove("ativo");
        btnEst_Produtos.classList.add("ativo");
        btnEst_Subprodutos.classList.remove("ativo");
      } else if (entidade === 'Est_Subprodutos') {
        btnEst_Entradas.classList.remove("ativo");
        btnEst_Produtos.classList.remove("ativo");
        btnEst_Subprodutos.classList.add("ativo");
  }
}
}

// ------SELEÇÃO NO BOTÃO EstOQUE PARA QUANDO A PÁGINA CARREGAR------

document.addEventListener("DOMContentLoaded", function() {
  var btnEst_Entradas = document.querySelector(".ret1");
  var btnEst_Produtos = document.querySelector(".ret0");
  var btnEst_Subprodutos = document.querySelector(".ret00");

  if (btnEst_Entradas && btnEst_Produtos && btnEst_Subprodutos) {
    btnEst_Entradas.classList.add("ativo");
    btnEst_Produtos.classList.remove("ativo");
    btnEst_Subprodutos.classList.remove("ativo");
  }
});

// ------Crud de produção------

