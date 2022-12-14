const usersController = require('../controllers/usersControllers');

module.exports = (app) => {
  //# create a device
  app.post('/api/users', usersController.create);
  
  //#get the list of users
  app.get('/api/users', usersController.fetch);
  
  //#get a single device
  app.get('/api/users/:id', usersController.get);
  
  //#update a device
  app.put('/api/users/:id', usersController.update);
  
  //#delete a device
  app.delete('/api/users/:id', usersController.delete);

  //#delete a device
  app.delete('/api/users', usersController.deleteMany);
};