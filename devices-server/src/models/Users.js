const mongoose = require('mongoose');
const { Schema } = mongoose;

const  deviceSchema = new Schema({
    email:{type:String,reqiured:true,unique: true},
    pass:{type:String,reqiured:true},
    role :{type:String,required:true} //0:admin 1:user
});
const User = mongoose.model('users',deviceSchema);//collection

module.exports = User;