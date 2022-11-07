const Device = require('../models/Devices');

const command = process.env.COMMAND;
var expiration_term_se = process.env.EXPIRATION_TERM_SE;
var expiration_term_system = process.env.EXPIRATION_TERM_SYSTEM;

function genCsrID(){
  //
  return 1;
}
function genCsrGroup(){
  return 1;
}

function genExpiration(type)
{    
  const date = new Date() ;
  //3年　の期限　利用者３年　システム6年
  if (type == "SE"){
    if (expiration_term_se == null) {
      expiration_term_se = "3"
    }
    date.setYear(date.getFullYear() +  Number(expiration_term_se)); 
  }
  
  if(type == "System"){
    if (expiration_term_system == null) {
      expiration_term_system = "6"
    }
    date.setYear(date.getFullYear() +  Number(expiration_term_system));
  }
	return date;
}

module.exports = {
  //# create a device
  create: async (request, reply) => {
    try {
      const device = request.body;
      const deviceCN = device.CN;
      //validationが実装されたらやめると思う
      if(device.email.length==0){
        reply.code(406).send(Error("Email should not be empty"));
        return ;
      }
      if (await Device.findOne({"CN" :deviceCN})){
        reply.code(409).send(Error("This CN is already used"));
        return ;
      }

      device["csrID"]=genCsrID();
      device["csrGroup"]=genCsrGroup();
      device["expiration_date"]=  genExpiration(device["type"]);
      device["status"]="Waiting";
      device["command"] =command +" -cn "+ deviceCN +" -secret " +   device["secret"];

      const newDevice = await Device.create(device);
      reply.code(201).send(newDevice);
    } catch (e) {
      reply.code(500).send(e);
    }
  },
  
  //#get the list of devices
  //#get the list of devices
  fetch: async (request, reply) => {
    try {
      const useremail = request.headers.from;
      let deviceToFetch=[];
      const devices = await Device.find({});
      for (const device of devices) {
       email = device["email"];
       for (const email_children of email){
        if(email_children["email-children"] == useremail){
          deviceToFetch.push(device);
        }
       }
      }
      reply.code(200).send(deviceToFetch);
    } catch (e) {
      reply.code(500).send(e);
    }
  },
  //ここから下はいらない
  // parame　の意味を調べると　EMAILと IDどっちも取れたりするかもよ
  //#get a single device
//#get a single device
get: async (request, reply) => {
    try {
      const deviceId = request.params.id;
      const device = await Device.findById(deviceId);
      reply.code(200).send(device);
    } catch (e) {
      reply.code(500).send(e);
    }
  },
  
  //#update a device
//#update a device
//　変更できないものの　セキュリティ対策　
update: async (request, reply) => {
    try {
      const deviceId = request.params.id;
      const updates = request.body;
      //validationが実装されたらやめると思う
      if(updates.email.length==0){
        reply.code(406).send(Error("Email should not be empty"));
        return ;
      }
      const deviceCN = updates.CN;
      const deviceCSRID = updates.csrID
      const deviceByCN = await Device.findOne({"CN" :deviceCN});
      //データが一つしかないときのことかな
      if (deviceByCN != null && deviceId != deviceByCN.id){
        reply.code(409).send(Error("This CN is already used"));
        return ;
      }
      const deviceByCSRID =await Device.findOne({"csrID" :deviceCSRID});
      if (deviceByCSRID != null && deviceId != deviceByCSRID.id){
        reply.code(409).send(Error("This csrID is already used"))
        return ;
      }
      await Device.findByIdAndUpdate(deviceId, updates);
      const deviceToUpdate = await Device.findById(deviceId);
      reply.code(200).send({ data: deviceToUpdate });
    } catch (e) {
      reply.code(500).send(e);
    }
  },

  //#delete a device
//#delete a device
delete: async (request, reply) => {
    try {
      const deviceId = request.params.id;
      const deviceToDelete = await Device.findById(deviceId);
      await Device.findByIdAndDelete(deviceId);
      reply.code(200).send({ data: deviceToDelete });
    } catch (e) {
      reply.code(500).send(e);
    }
  },

  //#delete devices
  deleteMany: async (request, reply) => {
  try {
    const deviceIds = request.body;
    let deviceToDeletes=[];
    for (const deviceId of deviceIds){
      const deviceToDelete = await Device.findById(deviceId);
      await Device.findByIdAndDelete(deviceId);
      deviceToDeletes.push(deviceToDelete);
    }
    reply.code(200).send(deviceToDeletes);
    
  } catch (e) {
    reply.code(500).send(e);
  }
}
};
