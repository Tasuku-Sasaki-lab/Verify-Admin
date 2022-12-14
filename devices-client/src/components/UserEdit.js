import React from "react";
import { Edit,
    SimpleForm,
    DateTimeInput,
    TextInput,
    NumberInput,
    SelectInput,
    ArrayInput,
    SimpleFormIterator,
    Toolbar,
    SaveButton,
    usePermissions,
} from "react-admin"
import validateEmail from "./selfMade/validateEmail";

const UserEdit = (props) => {
    return (
        <Edit {...props}>
            <SimpleForm>
                <TextInput  source ="_id" disabled  />
                <TextInput required source="email" type="Email" validate={validateEmail} ></TextInput>
                <TextInput required source="pass" disabled></TextInput>
                < SelectInput required source="role"  choices={[
                                    { id: 'user', name: 'user' },
                                    { id: 'administrator', name: 'administrator' },
                                    ]} />
            </SimpleForm>
        </Edit>
    )
};
export default UserEdit;