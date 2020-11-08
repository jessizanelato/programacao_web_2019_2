var ws = new WebSocket("ws://localhost");
ws.onopen = function(e) {
    console.log("Conexão estabelecida", e);
}
ws.onmessage = function(e) {
    console.log("Mensagem recebida", e, e.data);
}

$(function() {
    $("#form-chat").on('submit', function(e) {
        let msg = $("#txt-input").val();
        ws.send(msg);
        
        let html = '<div class="panel-body msg_container_base">';
            html += '<div class="row msg_container base_sent">';
            html += '<div class="col-md-10 col-xs-10">';
            html += '<div class="messages msg_sent">';
            html += '<p>' + msg + '</p>';
            html += '</div></div></div></div>';
        $("#container-base").append(html);
        $('#txt-input').val('');

        e.preventDefault();
    });
});