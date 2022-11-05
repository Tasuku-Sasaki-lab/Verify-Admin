import React  from "react";
import { Create,SimpleForm,NumberInput,DateTimeInput, TextInput,SelectInput, ArrayInput,SimpleFormIterator} from "react-admin";
import {Box} from '@mui/material'
import validateInteger from "./selfMade/validateInteger";
import validateEmail from "./selfMade/validateEmail";

const devicesCreate = (props) =>{
    const role = JSON.parse(localStorage.getItem('auth')).role;
        const AdminCreate =  (
            <Create {...props}>
                <SimpleForm>
                    <Box display={{ xs: 'block', sm: 'flex' }} sx={{ width: 1 }}>
                        <Box flex={2}  mr={{ xs: 0, sm: '0.5em' }}>
                            <NumberInput required fullWidth source="csrID" min ={1} validate={validateInteger}/>
                        </Box>
                        <Box flex={2} mr={{ xs: 0, sm: '0.5em' }}>
                            <NumberInput fullWidth  required source="csrGroup" min ={1} validate={validateInteger}/>
                        </Box>
                    </Box>
                    <ArrayInput source="email" required validate={validateEmail}>
                        <SimpleFormIterator inline >
                            <TextInput required source ="email-children" type="email" fullWidth/>
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
                    <TextInput required source="pem" fullWidth multiline/>
                </SimpleForm>
            </Create>
        );

        const Usercreate =(
            <Create {...props}>
            <SimpleForm>
                <ArrayInput source="email" required validate={validateEmail}>
                    <SimpleFormIterator inline >
                        <TextInput required source ="email-children" type="email" fullWidth/>
                    </SimpleFormIterator>
                </ArrayInput>
                < SelectInput required source="type" fullWidth choices={[
                            { id: 'SE', name: 'SE' },
                            { id: 'System', name: 'System' },
                            ]} />
                <TextInput required source="CN"  fullWidth/>
                <TextInput required source="secret" fullWidth/>
            </SimpleForm>
        </Create>
        );

        return role == 0 ? AdminCreate : Usercreate;                            
};
export default devicesCreate;
