const Device = require('../models/Devices');

module.exports = {
    //distribute
    distribute: async(request,reply) =>{
        try{
            const cert = request.body.Cert;
            const deviceCN = request.body.Name;
            const allowRenewalDays = request.body.AllowTime;
            const serialNumber = cert.SerialNumber;
            const notBefore = cert.NotBefore;
            const dateNotBefore = new Date(notBefore);
            const notAfter = cert.NotAfter;
            const dateNotAfter = new Date(notAfter);
            const pem = request.body.Pem;

            if (deviceCN!=cert.Subject.CommonName){
                reply.code(400).send({message:"The common name is not valid"});
                return;
            }
            const device = await Device.findOne({"CN" :deviceCN});
            if (device == null){
                reply.code(400).send({message:"The common name is not mathched on DB"});
                return;
            }
            //初回の発行
            if (device["status"] === 'Waiting'){
                // serial SerialNumber  status pem:raw  NotBefore, NotAfter
                device.serial = serialNumber;
                device.pem = pem;
                device.cert_not_before = dateNotBefore;
                device.cert_not_after = dateNotAfter;
                device.status="Completed";
                await device.save();
                reply.code(200).send(true);
                return;
            }else if(device["status"] === 'Completed'){
            //２回目以降の発行
                const date = new Date();
                dateNotAfter.setDate( dateNotAfter.getDate() - allowRenewalDays);
                if (date < dateNotAfter){
                    reply.code(401).send(Error('This cert cannot be redistributed until ' + dateNotAfter.toString()));
                    return;
                }
                //再発行
                device.serial = serialNumber;
                device.cert_not_before = dateNotBefore;
                dateNotAfter.setDate( dateNotAfter.getDate() + allowRenewalDays);
                device.cert_not_after = dateNotAfter;
                await device.save();
                reply.code(200).send(true);
                return;
            }else {
                reply.code(401).send(Error("Your csr might not be varified."));
                return;
            }
            }catch(e){
                console.log(e);
                reply.code(500).send(e);
                return;
            }
        }

};