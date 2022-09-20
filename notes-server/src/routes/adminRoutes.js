const adminsController = require('../controllers/adminsControllers');

  module.exports = async (app) => {
   app.post('/authenticate',adminsController.auth);
  };
  
  