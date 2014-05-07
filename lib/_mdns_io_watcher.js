var dns_sd = require('_mdns_dns_sd');
exports.IOWatcher = typeof dns_sd.SocketWatcher !== 'undefined' ?
    dns_sd.SocketWatcher : process.binding('io_watcher').IOWatcher;
