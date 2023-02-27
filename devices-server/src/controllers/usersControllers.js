const User = require('../models/Users');

module.exports ={
    create: async (request, reply) => {
        try {
            const decorded = request.decorded;
            if(!(decorded.role== "administrator" )){
                reply.code(401).send(Error("You cannot access to the users")); 
                return;
            }
            const user = request.body;
            if (user.email == null ){
                reply.code(406).send(Error("Email should not be empty"));
                return;
            }
            if (user.pass == null){
                reply.code(406).send(Error("Password should not be empty"));
                return;
            }
            if (user.role == null){
                reply.code(406).send(Error("Role should not be empty"));
                return;
            }
            if (!(user.role == "administrator" ||  user.role=="user")){
                reply.code(406).send(Error("Role malformed"));
                return;
              }
            const newUser = await User.create(user);
            reply.code(200).send(newUser);
        }catch (e){
            reply.code(500).send(e);
        }
    },
    fetch: async (request, reply) => {
        try {
            const decorded = request.decorded;
            if(!(decorded.role== "administrator" )){
                reply.code(401).send(Error("You cannot access to the users")); 
                return;
            }
            const users = await User.find();
            reply.code(200).send(users);
        }catch (e){
            reply.code(500).send(e);
        }
    },
    get: async (request, reply) => {
        try {
            const decorded = request.decorded;
            if(!(decorded.role== "administrator" )){
                reply.code(401).send(Error("You cannot access to the user")); 
                return;
            }
            const userId = request.params.id;
            const user = await User.findById(userId);
            if(user == null){
                reply.code(406).send(Error("This ID is wrong"));
                return;
              }
            reply.code(200).send(user);
        }catch (e){
            reply.code(500).send(e);
        }
    },
    update: async (request, reply) => {
        try {
            const decorded = request.decorded;
            if(!(decorded.role== "administrator" )){
                reply.code(401).send(Error("You cannot access to the users")); 
                return;
            }
            const userId = request.params.id;
            const updates = request.body;
            const user = await User.findById(userId);
            if(user == null){
              reply.code(500).send(Error("This id is wrong"));
              return;
            }
            if (updates.email == null ){
                reply.code(406).send(Error("Email should not be empty"));
                return;
            }
            if (updates.pass == null){
                reply.code(406).send(Error("Password should not be empty"));
                return;
            }
            if (updates.role == null){
                reply.code(406).send(Error("Role should not be empty"));
                return;
            }
            if (!(updates.role == "administrator" || updates.role=="user")){
                reply.code(406).send(Error("Role malformed"));
                return;
            }
            
            await User.findByIdAndUpdate(userId, updates);
            const userToUpdate = await User.findById(userId);
            reply.code(200).send(userToUpdate);
        }catch (e){
            reply.code(500).send(e);
        }
    },
    delete: async (request, reply) => {
        try {
            const decorded = request.decorded;
            if(!(decorded.role== "administrator" )){
                reply.code(401).send(Error("You cannot access to the user")); 
                return;
            }
            const userId = request.params.id;
            const userToDelete = await User.findById(userId);
            if (userToDelete == null){
                reply.code(500).send(Error("This id is wrong"));
                return;
            }
            await User.findByIdAndDelete(userId);
            reply.code(200).send({ data : userToDelete })
        }catch (e){
            reply.code(500).send(e);
        }
    },
    deleteMany: async (request, reply) => {
        try {
            const decorded = request.decorded;
            if(!(decorded.role== "administrator" )){
                reply.code(401).send(Error("You cannot access to the users")); 
                return;
            }
            const userIds = request.body;
            if (userIds.length == 0){
                reply.code(406).send(Error("IDs should not be empty"));
                return ;
              }
            let userToDeletes=[];
            for (const userId of  userIds){
                const userToDelete = await User.findById(userId);
                await User.findByIdAndDelete(userId);
                userToDeletes.push(userToDelete);
            }
            reply.code(200).send(userToDeletes);
        }catch (e){
            reply.code(500).send(e);
        }
    },
};