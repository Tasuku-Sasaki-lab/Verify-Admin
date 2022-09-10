const mongoose = require('mongoose');
const { Schema } = mongoose;

const  noteSchema = new Schema({
    email:{type:String,reqiured:true},
    pass:{type:String,reqiured:true}
});

const Admin = mongoose.model('admins',noteSchema);//collection

module.exports = Admin;