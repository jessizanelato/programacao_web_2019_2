const WebSocket = require('ws');

const port = 5000
const host = 'localhost'

const wss = new WebSocket.Server({host: host, port: port });

wss.on('connection', ws => {
	ws.on('message', mensagem => {
        let eco = `Mensagem recebida: ${mensagem}`;
        console.log(eco);
		ws.send(eco);
	});
	ws.send('Estou te ouvindo!');
});
console.log('Servidor rodando... //'+ host +':' + port);