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
import {Box} from '@mui/material'
import validateInteger from "./selfMade/validateInteger";
import validateEmail from "./selfMade/validateEmail";

const DevicesCreate = (props) =>{
    const  { isLoading, permissions }  = usePermissions();
    const emailLabelMessage ="Other Emails (" + JSON.parse(localStorage.getItem('auth')).username +" will be automatically registerd)";
    const emailLabel =(<FieldTitle label={emailLabelMessage} />);
    return   (
            <Create {...props}>
                {permissions === 'administrator' &&
                    <SimpleForm>
                        <NumberInput fullWidth  required source="csrGroup" min ={1} validate={validateInteger}/>
                        <ArrayInput source="email" required validate={validateEmail} label="Emails">
                            <SimpleFormIterator inline >
                                <TextInput required source ="email-children" label="email" type="Email" fullWidth/>
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
                                    ]} />
                                </Box>
                            <Box flex={3} mr={{ xs: 0, sm: '0.5em' }}>
                            <DateTimeInput required source="expiration_date" fullWidth></DateTimeInput>
                            </Box>
                        </Box>
                        <TextInput required source="CN"  fullWidth/>
                        <TextInput required source="secret" fullWidth/>
                    </SimpleForm>
                }  

                {permissions === 'user' &&
                    <SimpleForm>
                    <ArrayInput source="email" required validate={validateEmail} label={emailLabel}>
                        <SimpleFormIterator inline >
                            <TextInput required source ="email-children" type="email" label="Email" fullWidth/>
                        </SimpleFormIterator>
                    </ArrayInput>
                    < SelectInput required source="type" fullWidth choices={[
                                { id: 'SE', name: 'SE' },
                                { id: 'System', name: 'System' },
                                ]} />
                    <TextInput required source="CN"  fullWidth/>
                    <TextInput required source="secret" fullWidth/>
                </SimpleForm>
                }     
            </Create>
        )                   
};
export default DevicesCreate;
