var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);

app.get('/', function(req, res){
	res.send('<h1>Yeah! I am healthy!</h1>');
});

io.on('connection', function (socket) {
  var addedUser = false;

  // when the client emits 'new message', this listens and executes
  socket.on('new message', function (data) {
    console.log("qiu dai");
  });
});

http.listen(3000, function(){
	console.log('listening on *:3000');
});