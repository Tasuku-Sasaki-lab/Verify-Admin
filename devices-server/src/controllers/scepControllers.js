const Device = require('../models/Devices');

module.exports = {
    //verify
    verify: async(request,reply) =>{
        try {
            const CN = request.body.Cn;
            const device = await Device.findOne({"CN":CN});
            const date = new Date() ;
            const miriSecondNow = date.getTime() ;
            if (device == null){
                reply.code(400).send({message:"The common name is not mathched"})
            }
            else if (request.body.Secret != device.secret){
                reply.code(401).send({message:"The challenge password is wrong"})
                return;
            }else if(miriSecondNow > device.expiration_date){
                reply.code(401).send({message:"The csr has been expired"})
                return;
            }
            else{
                reply.code(200).send();
            }
        
        } catch (e){
            reply.code(500).send(e);
        }
    }
};