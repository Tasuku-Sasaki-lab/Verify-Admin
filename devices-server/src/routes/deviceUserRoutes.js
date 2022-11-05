const devicesUserController = require('../controllers/devicesUserControllers');

module.exports = (app) => {
    // ユーザーのできることに応じて　できることを変えよ
  //# create a device
  app.post('/user/devices', devicesUserController.create);
  
  //#get the list of devices
  app.get('/user/devices', devicesUserController.fetch);
  
  //#get a single device
  app.get('/user/devices/:id', devicesUserController.get);
  
  //#update a device
  //app.put('/user/devices/:id', devicesController.update);
  
  //#delete a device
  //app.delete('/user/devices/:id', devicesUserController.delete);

  //#delete a device
  //app.delete('/user/devices', devicesUserController.deleteMany);
};