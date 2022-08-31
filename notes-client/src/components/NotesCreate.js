import React  from "react";
import { Create,SimpleForm,NumberInput,DateTimeInput, TextInput } from "react-admin";

const NotesCreate = (props) =>{
    return (
        <Create {...props}>
            <SimpleForm>
                <NumberInput required source="csrID"/>
                <NumberInput required source="csrGroup"/>
                <TextInput required source="email" />
                <TextInput required source="CN"/>
                <TextInput required source="status"/>
                <TextInput required source="secret"/>
                <DateTimeInput required source="expiration_date"></DateTimeInput>
                <TextInput required source="pem"/>
            </SimpleForm>
        </Create>
    );
};
export default NotesCreate;
