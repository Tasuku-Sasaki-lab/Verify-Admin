const User = require('../models/Users');
const jwtSign = require('../JWT/jwtSign');

module.exports = {
    //login
    auth: async(request,reply)=>{
      try{
        const email = request.body.username;
        const users = await User.findOne({"email":email});
        if(users == null){
          reply.code(400).send(Error("User doesn't exit"));   
          return;       
        }
        const role = users.role;
        if(request.body.password == users.pass){
          //JWTの生成
          const token =  jwtSign(email,role);
          reply.code(200).send({'username':email,'Token' :token});
          return;
        }else{
          reply.code(401).send(Error("The password is wrong"));
        }
      }catch (e) {
        reply.code(500).send(e);
      }
    }
  };
  
