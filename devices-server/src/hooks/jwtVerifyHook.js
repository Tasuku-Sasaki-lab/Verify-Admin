const jwt = require('jsonwebtoken');
require('dotenv').config();
const jwtSecretAdmin = process.env.JWT_KEY_ADMIN;
const jwtSecretUser = process.env.JWT_KEY_USER;
const jwtSecretScep = process.env.JWT_KEY_SCEP;

//About error in JWT :https://github.com/auth0/node-jsonwebtoken#errors--codes

module.exports = async (request, reply)=>{
    try {
        if (request.url ==  '/authenticate'){
            return;
        }
        if (request.url ==  '/scep'){
          const res = /(?<=^Bearer(\s)+)[a-zA-Z\d\-._~+/]+=*$/;
          const token = request.headers.authorization.match(res);
          const decoded = jwt.verify(token[0], jwtSecretScep);
          //console.log( `SCEP OK: decoded.username=[${decoded.iss}]` )
          return;
        }else if(request.url ==  '/admin'){
          const res = /(?<=^Bearer(\s)+)[a-zA-Z\d\-._~+/]+=*$/;
          const token = request.headers.authorization.match(res);
          const decoded = jwt.verify(token[0], jwtSecretAdmin);
          //console.log( `Verify_Admin OK: decoded.username=[${decoded.iss}]` )
        }else{
          const res = /(?<=^Bearer(\s)+)[a-zA-Z\d\-._~+/]+=*$/;
          const token = request.headers.authorization.match(res);
          const decoded = jwt.verify(token[0], jwtSecretUser);
        }
      } catch(err) {
        console.log( `ERROR: err.message=[${err.message}]` );
        reply.code(401).send(err);
      }
};