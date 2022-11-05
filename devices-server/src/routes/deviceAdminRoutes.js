const devicesController = require('../controllers/devicesController');

module.exports = (app) => {
  //# create a device
  app.post('/admin/devices', devicesController.create);
  
  //#get the list of devices
  app.get('/admin/devices', devicesController.fetch);
  
  //#get a single device
  app.get('/admin/devices/:id', devicesController.get);
  
  //#update a device
  app.put('/admin/devices/:id', devicesController.update);
  
  //#delete a device
  app.delete('/admin/devices/:id', devicesController.delete);

  //#delete a device
  app.delete('/admin/devices', devicesController.deleteMany);
};