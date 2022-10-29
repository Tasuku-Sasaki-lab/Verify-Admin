import React from 'react';
import dataProvider from './dataProvider';
import authProvider from './authProvider';
import { Admin, Resource } from 'react-admin';
import devicesList from './components/DevicesList';
import devicesEdit from './components/DevicesEdit';
import devicesCreate from './components/DevicesCreate';

function App() {
  return (
    <Admin dataProvider={dataProvider} authProvider={authProvider}>
      <Resource
        name="devices"
        list={devicesList}
        edit={devicesEdit}
        create={devicesCreate}
      />
    </Admin>
  );
}
export default App;