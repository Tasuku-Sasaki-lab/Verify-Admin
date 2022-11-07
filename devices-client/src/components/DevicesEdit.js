import React from "react";
import { Edit,SimpleForm,DateTimeInput,TextInput,NumberInput ,SelectInput,ArrayInput,SimpleFormIterator} from "react-admin";
import {Box} from '@mui/material';
import validateInteger from "./selfMade/validateInteger";
import validateEmail from "./selfMade/validateEmail";


const devicesEdit =(props) =>{
    const token = JSON.parse(localStorage.getItem('auth')).Token;
    const base64 = token.split('.')[1]; 
    const role = JSON.parse(window.atob(base64)).role;    
    const AdminEdit = (
        <Edit {...props}>
            <SimpleForm>
                <Box display={{ xs: 'block', sm: 'flex' }} sx={{ width: 1 }}>
                    <Box flex={2}  mr={{ xs: 0, sm: '0.5em' }}>
                        <TextInput  source ="_id" disabled fullWidth />
                    </Box>
                    <Box flex={2} mr={{ xs: 0, sm: '0.5em' }}>
                        <NumberInput required source="csrGroup" fullWidth min ={1} validate={validateInteger}/>
                    </Box>
                </Box>
                <ArrayInput source="email" required validate={validateEmail} label="Emails">
                    <SimpleFormIterator inline >
                        <TextInput required source ="email-children" type="email" label="Email" fullWidth/>
                    </SimpleFormIterator>
                </ArrayInput>
                <Box display={{ xs: 'block', sm: 'flex' }} sx={{ width: 1 }}>
                    <Box flex={3} mr={{ xs: 0, sm: '0.5em' }}>
                        < SelectInput required source="type" fullWidth choices={[
                            { id: 'SE', name: 'SE' },
                            { id: 'System', name: 'System' },
                            ]} />
                    </Box>                                            
                    <Box flex={3}  mr={{ xs: 0, sm: '0.5em' }}>
                        < SelectInput required source="status" fullWidth choices={[
                        { id: 'Waiting', name: 'Waiting' },
                        { id: 'Expired', name: 'Expired' },
                        { id: 'Completed', name: 'Completed' },
                        { id: 'Canceled', name: 'Canceled'}
                        ]} />
                    </Box>
                    <Box flex={3} mr={{ xs: 0, sm: '0.5em' }}>
                       <DateTimeInput required source="expiration_date" fullWidth></DateTimeInput>
                    </Box>
                </Box>
                <TextInput required source="CN"  fullWidth/>
                <TextInput required source="secret" fullWidth/>
                <TextInput disabled source="pem" fullWidth multiline/>
                <TextInput source="command" disabled fullWidth></TextInput>
            </SimpleForm>
        </Edit>

    );
    const UserEdit =(
        <Edit {...props}>
            <SimpleForm>
                <Box display={{ xs: 'block', sm: 'flex' }} sx={{ width: 1 }}>
                    <Box flex={2}  mr={{ xs: 0, sm: '0.5em' }}>
                        <TextInput  source="_id" disabled fullWidth/>
                    </Box>
                    <Box flex={2} mr={{ xs: 0, sm: '0.5em' }}>
                        <NumberInput required disabled source="csrGroup" fullWidth min ={1} validate={validateInteger}/>
                    </Box>
                </Box>
                <ArrayInput source="email" required validate={validateEmail} label="Emails">
                    <SimpleFormIterator inline >
                        <TextInput required source ="email-children" type="email" label="Email" fullWidth/>
                    </SimpleFormIterator>
                </ArrayInput>
                <Box display={{ xs: 'block', sm: 'flex' }} sx={{ width: 1 }}>
                    <Box flex={3} mr={{ xs: 0, sm: '0.5em' }}>
                        < SelectInput required source="type" fullWidth disabled choices={[
                            { id: 'SE', name: 'SE' },
                            { id: 'System', name: 'System' },
                            ]} />
                    </Box>                                            
                    <Box flex={3}  mr={{ xs: 0, sm: '0.5em' }}>
                        < SelectInput required source="status" fullWidth disabled choices={[
                        { id: 'Waiting', name: 'Waiting' },
                        { id: 'Expired', name: 'Expired' },
                        { id: 'Completed', name: 'Completed' },
                        { id: 'Canceled', name: 'Canceled'}
                        ]} />
                    </Box>
                    <Box flex={3} mr={{ xs: 0, sm: '0.5em' }}>
                       <DateTimeInput required source="expiration_date" disabled fullWidth></DateTimeInput>
                    </Box>
                </Box>
                <TextInput required source="CN" disabled fullWidth/>
                <TextInput required source="secret" disabled fullWidth/>
                <TextInput disabled source="pem" fullWidth multiline/>
                <TextInput source="command" disabled fullWidth></TextInput>
            </SimpleForm>
        </Edit>

    );

    return role == "administrator" ? AdminEdit : UserEdit;
};
export default devicesEdit;
