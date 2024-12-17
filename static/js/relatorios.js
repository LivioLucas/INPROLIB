    const tabelaBody = document.querySelector('.tabela-trabalhos tbody');
    tabelaBody.innerHTML = ''; // Limpa a tabela



    btn = document.getElementById("aplica_filtro")

    btn.addEventListener('click', aplicarFiltros)
    
    async function aplicarFiltros() {
        const filtros = {
            curso: document.getElementById('curso').value,
            autor: document.getElementById('autor').value,
            tipo: document.getElementById('tipo').value,
            data_inicial: document.getElementById('data_inicial').value,
            data_final: document.getElementById('data_final').value
        };

        console.log(filtros)

        const response = await fetch('/filtrar', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(filtros)
        });

        const dados = await response.json();
        if (response.ok) {
            console.log(dados.length)
            if (dados.length === 0){
                alert("NENHUMA PUBLICAÇÃO ENCONTRADA PARA OS FILTROS SELECIONADOS")
            }else{
                atualizarTabela(dados);
            }
        } else {
            console.error(dados.error);
        }
    }

    function atualizarTabela(dados) {
        const tabelaBody = document.querySelector('.tabela-trabalhos tbody');
        tabelaBody.innerHTML = ''; // Limpa a tabela

        console.log(dados)

        dados.forEach(dado => {
            data_publicacao = transformadata(dado[5])
            const row = document.createElement('tr');
            row.innerHTML = `
                <td><input type="checkbox">${dado[1]}</td>
                <td>${dado[2]}</td>
                <td>${dado[3]}</td>
                <td>${data_publicacao}</td>
            `;
            tabelaBody.appendChild(row);
        });
    }

    function transformadata(dataOriginal) {
        // String de data no formato original

        // Converte a string para um objeto Date
        const data = new Date(dataOriginal);

        // Extrai o dia, mês e ano
        const dia = String(data.getUTCDate()).padStart(2, '0'); // Garante 2 dígitos para o dia
        const mes = String(data.getUTCMonth() + 1).padStart(2, '0'); // Meses começam em 0
        const ano = data.getUTCFullYear();

        // Formata a data no padrão dd/mm/aaaa
        const dataFormatada = `${dia}/${mes}/${ano}`;

        return(dataFormatada); // Saída: 04/12/2024

    }