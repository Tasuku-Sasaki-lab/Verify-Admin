//import { stringify } from 'query-string';

const Admin = require('../models/Admins');

module.exports = {
    //login
    auth: async(request,reply)=>{
      try {
        const Adminemail = request.body.username;
        const admins = await Admin.findOne({"email":Adminemail});
        if(admins == null){
          reply.code(400).send("User don't exit")
        }

        if(request.body.password == admins.pass){
          reply.code(200);
        }else{
          reply.code(401);
        }
      } catch (e) {
        reply.code(500).send(e);
      }
    },
    //# create a admin
    create: async (request, reply) => {
      try {
        const admin = request.body;
        const newAdmin = await Admin.create(admin);
        reply.code(201).send(newAdmin);
      } catch (e) {
        reply.code(500).send(e);
      }
    },
    
    //#get the list of Admins
    //#get the list of Admins
    fetch: async (request, reply) => {
      try {
        const Admins = await Admin.find({});
        reply.code(200).send(Admins);
      } catch (e) {
        reply.code(500).send(e);
      }
    },
    
    //#get a single Admin by email
  get: async (request, reply) => {
    try {
      const noteId = request.params.id;
      const note = await Admin.findById(noteId);
      reply.code(200).send(note);
    } catch (e) {
      reply.code(500).send(e);
    }
    },
    
    //#update a Admin
  //#update a Admin
  update: async (request, reply) => {
      try {
        const AdminId = request.params.id;
        const updates = request.body;
        await Admin.findByIdAndUpdate(AdminId, updates);
        const AdminToUpdate = await Admin.findById(AdminId);
        reply.code(200).send({ data: AdminToUpdate });
      } catch (e) {
        reply.code(500).send(e);
      }
    },
  
    //#delete a Admin
  //#delete a Admin
  delete: async (request, reply) => {
      try {
        const AdminId = request.params.id;
        const AdminToDelete = await Admin.findById(AdminId);
        await Admin.findByIdAndDelete(AdminId);
        reply.code(200).send({ data: AdminToDelete });
      } catch (e) {
        reply.code(500).send(e);
      }
    }
  };
  