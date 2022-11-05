// in src/authProvider.js
const authProvider = {
    // called when the user attempts to log in
    login: ({ username, password }) =>  {
        const request = new Request('http://localhost:3000/authenticate', {
            method: 'POST',
            body: JSON.stringify({ username, password }),
            headers: new Headers({ 'Content-Type': 'application/json' }),
        });
        //判定はサーバー側でやって、こっちはステータスのみ受け取る
        return fetch(request)
            .then(response => {
                if (response.status < 200 || response.status >= 300) {
                    throw new Error(response.statusText);
                }
                //このreturn がauthに入る
                return response.json();
            })
            
            .then(auth => {
                //authにはtoken
                localStorage.setItem('auth', JSON.stringify(auth));
            })
            .catch((e) => {
               throw new Error(e);
            });
    },

    // called when the user clicks on the logout button
    logout: () => {
        localStorage.removeItem('auth');
        return Promise.resolve();
    },
    // called when the API returns an error
    checkError: (error) => {
        const status = error.status;
        if (status === 401 || status === 403) {
            localStorage.removeItem('auth');
            return Promise.reject({ message: 'Unauthorized user!' });
        }
        // other error code (404, 500, etc): no need to log out
        return Promise.resolve();
    },
    // called when the user navigates to a new location, to check for authentication
    checkAuth: () => {
        return localStorage.getItem('auth')
            ? Promise.resolve()
            : Promise.reject({ message: 'login.required' });
    },
    getIdentity: () => {
        try {
            //const { id, fullName, avatar } = JSON.parse(localStorage.getItem('auth'));
            //JWTのデコードJSONから名前subをとる
            const fullName = JSON.parse(localStorage.getItem('auth')).username;
            return Promise.resolve({ fullName});
        } catch (error) {
            return Promise.reject(error);
        }
    },
    // called when the user navigates to a new location, to check for permissions / roles
    getPermissions: () => Promise.resolve(),
};

export default authProvider;