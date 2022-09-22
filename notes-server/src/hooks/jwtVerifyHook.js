const jwt = require('jsonwebtoken');
require('dotenv').config();
const jwtSecret = process.env.JWT_KEY;

module.exports = async (request, reply)=>{
    try {
        if (request.url ==  '/authenticate'){
            return;
        }
        var res = /Bearer /;
        var authorizationHeader = request.headers.authorization;
        if(res.test(authorizationHeader)){
            var token = authorizationHeader.split(' ');
            var decoded = jwt.verify(token[1], jwtSecret);
            console.log( `OK: decoded.username=[${decoded.iss}]` )

        } else{
          reply.code(401).send('');
        }
      } catch(err) {
        console.log( `ERROR: err.message=[${err.message}]` );
        reply.code(401).send(err.message);
      }
};
