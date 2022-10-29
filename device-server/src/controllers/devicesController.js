const Device = require('../models/Devices');

module.exports = {
  //# create a device
  create: async (request, reply) => {
    try {
      const device = request.body;
      const deviceCN = device.CN;
      const deviceCSRID = device.csrID;
      //validationが実装されたらやめると思う
      if(device.email.length==0){
        reply.code(406).send(Error("Email should not be empty"));
        return ;
      }
      if (await Device.findOne({"CN" :deviceCN})){
        reply.code(409).send(Error("This CN is already used"));
        return ;
      }
      if (await Device.findOne({"csrID" :deviceCSRID})){
        reply.code(409).send(Error("This csrID is already used"));
        return ;
      }
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
      
      const devices = await Device.find({});
      reply.code(200).send(devices);
    } catch (e) {
      reply.code(500).send(e);
    }
  },
  
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
      if (deviceId != deviceByCN.id){
        reply.code(409).send(Error("This CN is already used"));
        return ;
      }
      const deviceByCSRID =await Device.findOne({"csrID" :deviceCSRID});
      if (deviceId != deviceByCSRID.id){
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
