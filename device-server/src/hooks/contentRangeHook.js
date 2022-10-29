const Device = require('../models/Devices');

module.exports = (request, reply, done) => {
  Device.countDocuments({}, (err, count) => {
    if (err) {
      console.error(err);
      reply.code(500).send('Error!');
    }
    reply.header('Content-Range', `devices 0-10}/${count}`);
    done();
  });
};