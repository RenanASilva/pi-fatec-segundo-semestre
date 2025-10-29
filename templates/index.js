// "Ligar o data-table"
$(document).ready(function () {
    $('#tabela-obras').DataTable({
        language: {
            url: '//cdn.datatables.net/plug-ins/2.0.8/i18n/pt-BR.json'
        }
    });
});