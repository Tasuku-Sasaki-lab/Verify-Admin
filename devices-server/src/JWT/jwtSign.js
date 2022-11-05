const jwt = require('jsonwebtoken');
require('dotenv').config();
const jwtSecretAdmin = process.env.JWT_KEY_ADMIN;
const jwtSecretUser = process.env.JWT_KEY_USER;
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
    };
    const jwtOptions = {
        algorithm: 'HS256',
    };
    if (role == 0){
        return jwt.sign(jwtPayload, jwtSecretAdmin, jwtOptions);
    }else{
        return jwt.sign(jwtPayload, jwtSecretUser, jwtOptions);
    }
};