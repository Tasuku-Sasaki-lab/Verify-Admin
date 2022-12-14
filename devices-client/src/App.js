import React from 'react';
import dataProvider from './dataProvider';
import authProvider from './authProvider';
import { Admin, Resource,UserMenu,AppBar,Layout} from 'react-admin';
import DevicesList from './components/DevicesList';
import DevicesEdit from './components/DevicesEdit';
import DevicesCreate from './components/DevicesCreate';
import MyLogoutButton from './components/selfMade/MyLogoutButton';
import UserList from './components/UserList';
import UserEdit from './components/UserEdit';
import UserCreate from './components/UserCreate';
import UserIcon from "@mui/icons-material/Group";
import FeedIcon from '@mui/icons-material/Feed';

const MyUserMenu = () => <UserMenu><MyLogoutButton /></UserMenu>;

const MyAppBar = () => <AppBar userMenu={<MyUserMenu />} />;

const MyLayout = (props) => <Layout {...props} appBar={MyAppBar} />;


function App() {
  return (
    <Admin dataProvider={dataProvider} authProvider={authProvider} layout={MyLayout}>
      {permissions => (
        <>
            <Resource name="devices" list={DevicesList} edit={DevicesEdit} create={DevicesCreate} icon={FeedIcon}/>
            {permissions === 'administrator'
                ? <Resource name="users" list = {UserList} edit={UserEdit} create={UserCreate} icon={UserIcon}/>
                : null}
        </>
    )}
    </Admin>
  );
}
export default App;