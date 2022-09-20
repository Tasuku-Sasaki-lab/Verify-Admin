const jwt = require('jsonwebtoken');
require('dotenv').config();
const jwtSecret = process.env.JWT_KEY;

module.exports = async (username) => {
    //生成
    var date = new Date() ;
    var miriSecondNow = date.getTime() ;
    var nbf = Math.floor( miriSecondNow / 1000 ) ;
    var exp = nbf + 8*60*60; //exp = 8h

    const jwtPayload = {
        "iss": username,
        "sub": "mitsuru@procube.jp",
        "exp": exp,
        "nbf": nbf,
    };
    const jwtOptions = {
        algorithm: 'HS256',
    };

    try{ 
        const token = jwt.sign(jwtPayload, jwtSecret, jwtOptions);
        return token;
    }catch(err){
        return err.message();
    }
};