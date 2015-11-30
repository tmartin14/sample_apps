require('newrelic');
var express = require("express"),
    app = express();

var port = process.env.VCAP_APP_PORT || 8080;

app.use(express.static(__dirname + '/public'));

app.get("/", function (request, response) {
    response.writeHead(200, {"Content-Type": "text/html"})
    response.end("<h1>Hello World!</h1>  <br/>This is a <b>Node.js</b> app running on Cloud Foundry.<br/><br/><br/><b>Time:</b> " + new Date().toUTCString())
});

app.listen(port);
