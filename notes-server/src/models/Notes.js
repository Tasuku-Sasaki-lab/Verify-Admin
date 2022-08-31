const mongoose = require('mongoose');
const { Schema } = mongoose;

const  noteSchema = new Schema({
    csrID:{type:Number,reqiured:true},
    csrGroup:{type:Number,reqiured:true},
    CN:{type:String,reqiured:true},
    CN:{type:String,reqiured:true},
    email:{type:String,reqiured:true},
    secret:{type:String,reqiured:true},
    status:{type:String,reqiured:true},
    expiration_date:{ type: Date, required:true},
    pem:{type:String}
});

const Note = mongoose.model('note',noteSchema);//collection

module.exports = Note;