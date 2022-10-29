const devicesController = require('../controllers/devicesController');

module.exports = (app) => {
  //# create a device
  app.post('/api/devices', devicesController.create);
  
  //#get the list of devices
  app.get('/api/devices', devicesController.fetch);
  
  //#get a single device
  app.get('/api/devices/:id', devicesController.get);
  
  //#update a device
  app.put('/api/devices/:id', devicesController.update);
  
  //#delete a device
  app.delete('/api/devices/:id', devicesController.delete);

  //#delete a device
  app.delete('/api/devices', devicesController.deleteMany);
};