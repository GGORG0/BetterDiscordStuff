/**
 * @name GnomeBadge
 * @author GGORG
 * @description Opens a localhost API to get your ping count. Best used with the badge-updater.py script to add the ping badge on Linux.
 * @version 0.0.1
 * @authorLink https://github.com/GGORG0
 * @updateUrl https://github.com/GGORG0/GnomeBadge/raw/master/GnomeBadge.plugin.js
 */

const http = require("http");

module.exports = class GnomeBadge {
    start() {
        this.createServer();
        this.hserver.listen(6968, () => {});
    }
    stop() {
        this.hserver.close();
    }
    get_pings() {
        const mentionCount = BdApi.findModuleByProps("getTotalMentionCount").getTotalMentionCount();
        return mentionCount
    }
    createServer() {
        this.hserver = http.createServer((req, res) => {
            let path = req.url.split("/")[1];
            if (path === "getpings") {
                res.writeHead(200, { "Content-Type": "text/plain" });
                res.end(this.get_pings().toString());
            }
            // TODO:
            // else if (path === "markread") {
                // res.writeHead(200, { "Content-Type": "text/plain" });
                // this.markread();
                // res.end('success');
            // }
        });
        this.hserver.on("error", (err) => {console.error(err)});
    }
};
