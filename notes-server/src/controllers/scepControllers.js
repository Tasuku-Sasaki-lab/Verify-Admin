const Note = require('../models/Notes');

module.exports = {
    //verify
    verify: async(request,reply) =>{
        try {
            const CN = request.body.Cn;
            const note = await Note.findOne({"CN":CN});
            const date = new Date() ;
            const miriSecondNow = date.getTime() ;
            if (note == null){
                reply.code(400).send({message:"The common name (RFC4514 Distinguished Name string) is not mathched"})
            }
            else if (request.body.Secret != note.secret){
                reply.code(401).send({message:"The challenge password is wrong"})
                return;
            }else if(miriSecondNow > note.expiration_date){
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