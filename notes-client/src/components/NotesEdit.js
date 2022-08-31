import React from "react";
import { Edit,SimpleForm,DateTimeInput,TextInput,NumberInput } from "react-admin";

const NotesEdit =(props) =>{
    return (
        <Edit {...props}>
            <SimpleForm>
                <TextInput disabled source="id"/>
                <NumberInput disabled source="csrID"/>
                <NumberInput required source="csrGroup"/>
                <TextInput required source="email" />
                <TextInput disabled source="CN"/>
                <TextInput required source="status"/>
                <TextInput required source="secret"/>
                <DateTimeInput required source="expiration_date"></DateTimeInput>
                <TextInput disabled source="pem"/>
            </SimpleForm>
        </Edit>

    );
};
export default NotesEdit;
