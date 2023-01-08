const jwt = require('jsonwebtoken');
require('dotenv').config();
const jwtSecret = process.env.JWT_KEY;

//About error in JWT :https://github.com/auth0/node-jsonwebtoken#errors--codes

module.exports = async (request, reply)=>{
    try {
        if (request.url ==  '/authenticate'){
            return;
        }
        const res = /(?<=^Bearer(\s)+)[a-zA-Z\d\-._~+/]+=*$/;
        const token = request.headers.authorization.match(res);
        const decorded = jwt.verify(token[0], jwtSecret);
        request.decorded = decorded;
        const role = decorded.role;
        const roles = ["administrator","user","scepserver"];
        if (roles.indexOf(role) == -1){
          reply.code(401).send(new Error('You do not have any roles'));
          return;
        }
      } catch(err) {
        console.log( `ERROR: err.message=[${err.message}]` );
        reply.code(401).send(err);
        return;
      }
};