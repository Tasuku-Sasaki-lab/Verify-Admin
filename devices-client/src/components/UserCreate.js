import React  from "react";
import { 
    Create,
    SimpleForm,
    NumberInput,
    DateTimeInput, 
    TextInput,
    SelectInput, 
    ArrayInput,
    SimpleFormIterator,
    FieldTitle ,
    usePermissions,
} from "react-admin";
import validateEmail from "./selfMade/validateEmail";

const UserCreate = (props) => {
    return (
        <Create {...props}>
            <SimpleForm>
                <TextInput required source="email" type="Email" validate={validateEmail} ></TextInput>
                <TextInput required source="pass" label="Password"></TextInput>
                < SelectInput required source="role"  choices={[
                                    { id: 'user', name: 'user' },
                                    { id: 'administrator', name: 'administrator' },
                                    ]} />
            </SimpleForm>
        </Create>
    )
};
export default UserCreate;