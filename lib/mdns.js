var dns_sd = require('_mdns_dns_sd')
    , ad = require('_mdns_advertisement')
    , browser = require('_mdns_browser')
    , st = require('_mdns_service_type')
    , nif = require('_mdns_network_interface')
    ;

exports.dns_sd = dns_sd;

exports.Advertisement = ad.Advertisement;
exports.createAdvertisement = ad.Advertisement.create;

exports.Browser = browser.Browser;
exports.createBrowser = browser.Browser.create;
exports.browseThemAll = browser.browseThemAll;
exports.resolve = browser.resolve;

exports.MDNSService = require('_mdns_service').MDNSService;

exports.ServiceType = st.ServiceType;
exports.makeServiceType = st.makeServiceType;
exports.tcp = st.protocolHelper('tcp');
exports.udp = st.protocolHelper('udp');

exports.loopbackInterface = nif.loopbackInterface;

exports.dns_sd.exportConstants(exports);

exports.rst = require('_mdns_resolver_sequence_tasks');

exports.isAvahi = require('_mdns_avahi');

