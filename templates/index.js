// "Ligar o data-table"
$(document).ready(function () {
    $('#tabela-obras').DataTable({
        language: {
            url: '//cdn.datatables.net/plug-ins/2.0.8/i18n/pt-BR.json'
        }
    });
});

// Função executada ao clicar no botão
function alternarTema() {
    const html = document.documentElement;
    const icone = document.querySelector('#btn-tema i');
    
    // Verifica qual é o tema atual
    const temaAtual = html.getAttribute('data-bs-theme');

    if (temaAtual === 'dark') {
        // Muda para CLARO
        html.setAttribute('data-bs-theme', 'light');
        icone.className = 'bi bi-moon-stars'; // Ícone de Lua (para ativar o escuro depois)
        localStorage.setItem('tema', 'light'); // Salva na memória do navegador
    } else {
        // Muda para ESCURO
        html.setAttribute('data-bs-theme', 'dark');
        icone.className = 'bi bi-sun'; // Ícone de Sol (para voltar ao claro)
        localStorage.setItem('tema', 'dark'); // Salva na memória
    }
}

// Função para carregar o tema salvo quando a página abre
document.addEventListener('DOMContentLoaded', () => {
    const temaSalvo = localStorage.getItem('tema');
    const html = document.documentElement;
    const icone = document.querySelector('#btn-tema i');

    if (temaSalvo) {
        html.setAttribute('data-bs-theme', temaSalvo);
        // Ajusta o ícone conforme o tema carregado
        if (temaSalvo === 'dark') {
            icone.className = 'bi bi-sun';
        } else {
            icone.className = 'bi bi-moon-stars';
        }
    }
});