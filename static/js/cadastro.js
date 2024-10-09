// FORMATAÇÕES DOS DADOS INSERIDOS

let cpfInput = document.getElementById('cpfUser');
let cpfMask = IMask(cpfInput, {
    mask: '000.000.000-00'
});

let telefoneInput = document.getElementById('telefoneUser');
let telefoneMask = IMask(telefoneInput, {
    mask: '(00) 00000-0000'
});