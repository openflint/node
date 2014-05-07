/*!
 * ws: a node.js websocket client
 * Copyright(c) 2011 Einar Otto Stangvik <einaros@gmail.com>
 * MIT Licensed
 */

try {
  module.exports = process.binding('ws_bufferutil');
} catch (e) { try {
  module.exports = require('_ws_bufferutil_fallback');
} catch (e) {
  console.error('ws bufferutil seems to not have been built. Run npm install.');
  throw e;
}}
