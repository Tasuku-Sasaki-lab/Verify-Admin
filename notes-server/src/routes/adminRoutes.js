const adminsController = require('../controllers/adminsControllers');
//frontedから何で来るか
/*
module.exports = (app) => {
    fastify.get('/test', (req, reply) => {
        reply.send('Hello world');
      });
  //# get a single note
  app.post('/api/admins', adminsController.create);
  
  //#get the list of admins
  app.get('/api/admins', adminsController.fetch);
  
  //#get a single note
  app.get('/api/admins/:id', adminsController.get);
  
  //#update a note
  app.put('/api/admins/:id', adminsController.update);
  
  //#delete a note
  app.delete('/api/admins/:id', adminsController.delete);
};*/
/*
  module.exports = (app) => {
    // all our routes will appear here
  
    app.post('/authenticate', (req, reply) => {
      console.log(req);
        reply.send('Hello world');
      });
  };
  */


  module.exports = (app) => {
   app.post('/authenticate',adminsController.auth);
  };
  
  