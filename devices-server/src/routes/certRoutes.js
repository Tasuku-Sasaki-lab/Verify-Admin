const certController = require('../controllers/certControllers');

module.exports = async (app) =>{
    app.post('/cert',certController.distribute);
};