const mongoose = require('mongoose');
const { Schema } = mongoose;

const  devicesSchema = new Schema({
    csrGroup:{type:Number,reqiured:true},
    CN:{type:String,reqiured:true},
    email:{type:Array,reqiured:true},
    type:{type:String,reqiured:true},
    secret:{type:String,reqiured:true},
    status:{type:String,reqiured:true},
    expiration_date:{ type: Date, required:true},
    pem:{type:String},
    command:{type:String}
});
const Device = mongoose.model('devices',devicesSchema);//collection


module.exports = Device;