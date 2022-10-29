import React from "react";
import { Edit,SimpleForm,DateTimeInput,TextInput,NumberInput ,SelectInput,ArrayInput,SimpleFormIterator} from "react-admin";
import {Box} from '@mui/material';
import validateInteger from "./selfMade/validateInteger";
import validateEmail from "./selfMade/validateEmail";


const devicesEdit =(props) =>{
    return (
        <Edit {...props}>
            <SimpleForm>
                <TextInput source="id" disabled></TextInput>
                <Box display={{ xs: 'block', sm: 'flex' }} sx={{ width: 1 }}>
                    <Box flex={2}  mr={{ xs: 0, sm: '0.5em' }}>
                        <NumberInput disabled source="csrID" fullWidth/>
                    </Box>
                    <Box flex={2} mr={{ xs: 0, sm: '0.5em' }}>
                        <NumberInput required source="csrGroup" fullWidth min ={1} validate={validateInteger}/>
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
                <TextInput required source="CN" label="Format as RFC4514 Distinguished Name string" defaultValue="CN=TEST1,OU=MDM,O=scep-client,C=US" fullWidth/>
                <TextInput required source="secret" fullWidth/>
                <TextInput disabled source="pem" fullWidth multiline/>
            </SimpleForm>
        </Edit>

    );
};
export default devicesEdit;
