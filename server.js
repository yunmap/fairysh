var express = require('express');
var app = express();
var http = require('http').Server(app);

app.set('views', './views');
app.engine('html', require('ejs').renderFile);
app.set('view engine', 'html'); // view engine setting

const PORT = 3000;
const HOST = "localhost"

app.get('/', function(req,res){
    res.render('index');
})

http.listen(PORT,HOST, function(){
    console.log(`Running on http://${HOST}:${PORT}`);
});
  