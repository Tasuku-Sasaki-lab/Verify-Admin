const User = require('../models/Users');

module.exports ={
    create: async (request, reply) => {
        try {
            const decorded = request.decorded;
            if(!(decorded.role== "administrator" )){
                reply.code(401).send(Error("You cannot access to users")); 
                return;
            }
            const user = request.body;
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
                reply.code(401).send(Error("You cannot access to users")); 
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
                reply.code(401).send(Error("You cannot access to users")); 
                return;
            }
            const userId = request.params.id;
            const user = await User.findById(userId);
            reply.code(200).send(user);
        }catch (e){
            reply.code(500).send(e);
        }
    },
    update: async (request, reply) => {
        try {
            const decorded = request.decorded;
            if(!(decorded.role== "administrator" )){
                reply.code(401).send(Error("You cannot access to users")); 
                return;
            }
            const userId = request.params.id;
            const updates = request.body;
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
                reply.code(401).send(Error("You cannot access to users")); 
                return;
            }
            const userId = request.params.id;
            const userToDelete = await User.findById(userId);
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
                reply.code(401).send(Error("You cannot access to users")); 
                return;
            }
            const userIds = request.body;
            let userToDeletes=[];
            for (const userId in  userIds){
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