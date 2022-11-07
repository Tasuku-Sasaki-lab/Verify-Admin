const jwt = require('jsonwebtoken');
require('dotenv').config();
const jwtSecret = process.env.JWT_KEY;
const signer = process.env.SIGNER;

module.exports = (username,role) => {
    //生成
    var date = new Date() ;
    var miriSecondNow = date.getTime() ;
    var nbf = Math.floor( miriSecondNow / 1000 ) ;
    var exp = nbf + 8*60*60; //exp = 8h

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