const ocsp = require("ocsp")
const fs = require('fs');

let cert = fs.readFileSync("/home/sasakitasuku/React-Admin/scep/depot/ca.pem");
let key = fs.readFileSync("/home/sasakitasuku/React-Admin/scep/depot/ca.key")
var server = ocsp.Server.create({
    cert: cert,
    key: key
});

module.exports = {
    //
        add: async(request,reply) =>{
            try{
                server.addCert(43, 'good');
            }catch (e){
                console.log(e)
            }
    }
};