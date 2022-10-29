const mongoose = require('mongoose');
const { Schema } = mongoose;

const  deviceSchema = new Schema({
    email:{type:String,reqiured:true},
    pass:{type:String,reqiured:true}
});
const Admin = mongoose.model('admins',deviceSchema);//collection

module.exports = Admin;