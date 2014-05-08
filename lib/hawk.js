// Export sub-modules

exports.error = exports.Error = require('boom');
exports.sntp = require('sntp');
exports.server = require('_hawk_server');
exports.client = require('_hawk_client');
exports.crypto = require('_hawk_crypto');
exports.utils = require('_hawk_utils');

exports.uri = {
    authenticate: exports.server.authenticateBewit,
    getBewit: exports.client.getBewit
};


