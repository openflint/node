/*!
 * ws: a node.js websocket client
 * Copyright(c) 2011 Einar Otto Stangvik <einaros@gmail.com>
 * MIT Licensed
 */

module.exports = require('_ws_websocket');
module.exports.Server = require('_ws_websocket_server');
module.exports.Sender = require('_ws_sender');
module.exports.Receiver = require('_ws_receiver');

module.exports.createServer = function (options, connectionListener) {
  var server = new module.exports.Server(options);
  if (typeof connectionListener === 'function') {
    server.on('connection', connectionListener);
  }
  return server;
};

module.exports.connect = module.exports.createConnection = function (address, openListener) {
  var client = new module.exports(address);
  if (typeof openListener === 'function') {
    client.on('open', openListener);
  }
  return client;
};
