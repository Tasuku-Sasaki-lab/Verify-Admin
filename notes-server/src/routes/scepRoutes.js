const scepController = require('../controllers/scepControllers');

module.exports = async (app) =>{
    app.post('/scep',scepController.verify);
};