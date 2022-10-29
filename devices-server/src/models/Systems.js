const mongoose = require('mongoose');
const { Schema } = mongoose;

const  deviceSchema = new Schema({
    email:{type:String,reqiured:true,unique: true},
    pass:{type:String,reqiured:true},
    role :{type:String,required:true}
});
const System = mongoose.model('systems',deviceSchema);//collection

module.exports = System;