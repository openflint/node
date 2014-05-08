// Copyright 2011 Joyent, Inc.  All rights reserved.

var parser = require('_http_signature_parser');
var signer = require('_http_signature_signer');
var verify = require('_http_signature_verify');
var util = require('_http_signature_util');



///--- API

module.exports = {

  parse: parser.parseRequest,
  parseRequest: parser.parseRequest,

  sign: signer.signRequest,
  signRequest: signer.signRequest,

  sshKeyToPEM: util.sshKeyToPEM,
  sshKeyFingerprint: util.fingerprint,

  verify: verify.verifySignature,
  verifySignature: verify.verifySignature
};
