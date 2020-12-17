function noty (msg, type){
    new Noty({
        text: msg,
        timeout: 3000,
        progressBar: true,
        theme: 'metroui',
        layout: 'topRight',
        killer: true,
        type: type
    }).show();
}

$('#sidebarCollapse').on('click', function () {
    $('#sidebar').toggleClass('active');
});
