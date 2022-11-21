const jwt = require('jsonwebtoken');
require('dotenv').config();
const jwtSecret = process.env.JWT_KEY;
const signer = process.env.SIGNER;
var expTerm = process.env.JWT_EXPIRATION;

module.exports = (username,role) => {
    //生成
    var date = new Date() ;
    var miriSecondNow = date.getTime() ;
    var nbf = Math.floor( miriSecondNow / 1000 ) ;
    if(expTerm == null){
        expTerm = "28800";
    }
    var exp = nbf + Number(expTerm); 

    const jwtPayload = {
        "iss": signer,
        "sub": username,
        "exp": exp,
        "nbf": nbf,
        "role":role,
    };
    const jwtOptions = {
        algorithm: 'HS256',
    };
    return jwt.sign(jwtPayload, jwtSecret, jwtOptions);
};