const Device = require('../models/Devices');
const scep_server =process.env.SCEP_SERVER;
var command = process.env.COMMAND;
var expiration_term_se = process.env.EXPIRATION_TERM_SE;
var expiration_term_system = process.env.EXPIRATION_TERM_SYSTEM;
var certificate = process.env.CERTIFICATE;
var private_key = process.env.PRIVAE_KEY;

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
      const decorded = request.decorded;
      if(!(decorded.role== "administrator" || decorded.role == "user")){
        reply.code(401).send(Error("You cannot access to the device")); 
        return;
      }
      const device = request.body;
      if (decorded.role == "user"){
        device["email"].push({"email-children":decorded.sub});
      }
      if(device.email.length==0){
        reply.code(406).send(Error("Email should not be empty"));
        return ;
      }
      const deviceCN = device.CN;
      if (await Device.findOne({"CN" :deviceCN})){
        reply.code(409).send(Error("This CN is already used"));
        return ;
      }
      if(device["csrGroup"]== null){
        device["csrGroup"]=genCsrGroup();
      }
      if(device["expiration_date"]==null){
        device["expiration_date"]=  genExpiration(device["type"]);
      }
      if(device["status"] == null){
        device["status"]="Waiting";
      }
      if(command == null){
        command ="./scepclient-linux-amd64";
      }
      if(certificate == null){
        certificate = "etc/pki/tls/certs/nssdc.crt";
      }
      if(private_key == null){
        private_key = "/etc/pki/tls/private/nssdc.key";
      }
      device["command"] =command + " -server-url="+ scep_server +" -cn "+ deviceCN +" -secret " +   device["secret"] + " -certificate " + certificate + " -private-key " + private_key;
      const newDevice = await Device.create(device);
      reply.code(201).send(newDevice);
    } catch (e) {
      reply.code(500).send(e);
    }
  },
  
  //#get the list of devices
  fetch: async (request, reply) => {
    try {
      const decorded = request.decorded;
      switch (decorded.role){
        case "administrator":
          const devices = await Device.find({});
          reply.code(200).send(devices); 
          return;
        case "user":
          const useremail = decorded.sub;
          let deviceToFetch=[];
          const devices_user = await Device.find({});
          for (const device of devices_user) {
            for (const email_children of device["email"]){
              if(email_children["email-children"] == useremail){
                deviceToFetch.push(device);
              }
            }
          }
          reply.code(200).send(deviceToFetch);
          return;
        default :
          reply.code(401).send(Error("You cannot access to the device"));
          return;     
      }
    } catch (e) {
      reply.code(500).send(e);
    }
  },
  
//#get a single device
get: async (request, reply) => {
    try {
      const deviceId = request.params.id;
      const decorded = request.decorded;
      const device = await Device.findById(deviceId);
      switch (request.decorded.role){
        case "administrator":
          reply.code(200).send(device);
          return;
        case "user":
          for (const email_children of device["email"]){
            if(email_children["email-children"]== decorded.sub){
              reply.code(200).send(device);
              return ;
            }
          }
          reply.code(401).send(Error("You cannot access to the device"));
          return ;
        default:
          reply.code(401).send(Error("You cannot access to the device"));
          return;
      }
    } catch (e) {
      reply.code(500).send(e);
    }
  },
  
//#update a device
update: async (request, reply) => {
    try {
      const deviceId = request.params.id;
      const updates = request.body;
      const decorded = request.decorded;
      var flag = false;
      const device = await Device.findById(deviceId);
      if(device == null){
        reply.code(500).send(Error("This id is wrong"));
      }
      if(updates.email.length==0){
        reply.code(406).send(Error("Email should not be empty"));
        return ;
      }
      const deviceCN = updates.CN;
      const deviceByCN = await Device.findOne({"CN" :deviceCN});
      if (deviceByCN != null && deviceId != deviceByCN.id){
        reply.code(409).send(Error("This CN is already used"));
        return ;
      }
      if(decorded.role == "administrator"){
        flag = true;
      }
      if(decorded.role == "user"){
        for (const email_children of device["email"]){
          if(email_children["email-children"]== decorded.sub){
            flag = true;
          }
        }
      }
      if(flag){
        await Device.findByIdAndUpdate(deviceId, updates);
        const deviceToUpdate = await Device.findById(deviceId);
        reply.code(200).send({ data: deviceToUpdate });
        return;
      }
      reply.code(401).send(Error("You cannot access to the device"));
    } catch (e) {
      reply.code(500).send(e);
    }
  },

//#delete a device
delete: async (request, reply) => {
    try {
      if(request.decorded.role == "administrator"){
        const deviceId = request.params.id;
        const deviceToDelete = await Device.findById(deviceId);
        await Device.findByIdAndDelete(deviceId);
        reply.code(200).send({ data: deviceToDelete });
        return;
      }
      reply.code(401).send(Error("You cannot access to the device")); 
    } catch (e) {
      reply.code(500).send(e);
    }
  },

  //#delete devices
  deleteMany: async (request, reply) => {
  try {
    if(request.decorded.role == "administrator"){
      const deviceIds = request.body;
      let deviceToDeletes=[];
      for (const deviceId of deviceIds){
        const deviceToDelete = await Device.findById(deviceId);
        await Device.findByIdAndDelete(deviceId);
        deviceToDeletes.push(deviceToDelete);
      }
      reply.code(200).send(deviceToDeletes);
      return ;
    }
    reply.code(401).send(Error("You cannot access to the device")); 
  } catch (e) {
    reply.code(500).send(e);
  }
}
};
