const jwt = require('jsonwebtoken');
require('dotenv').config();
const jwtSecret = process.env.JWT_KEY;

module.exports = async (request, reply)=>{
    try {
        if (request.url ==  '/authenticate'){
            return;
        }
        var decoded = jwt.verify(request.headers.authorization, jwtSecret);
        console.log( `OK: decoded.username=[${decoded.iss}]` );
      } catch(err) {
        console.log( `ERROR: err.message=[${err.message}]` );
        reply.code(401).send(err.message);
      }
};
