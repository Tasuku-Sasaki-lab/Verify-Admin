import { fetchUtils } from 'react-admin';
import { stringify } from 'query-string';

/*
const role = JSON.parse(localStorage.getItem('auth')).role;
const apiUrl = role==0 ?'http://localhost:3000/admin':"http://localhost:3000/user";
*/
/*
impleRestProvider のコンストラクタの引数に httpClient を渡すことができる。 
これにヘッダをいじる処理を実装して使うことでローカルで持っているクレデンシャルをAPIに
ヘッダとして送ることができるようになる。
*/
const httpClient = (url, options = {}) => {
  if (!options.headers) {
      options.headers = new Headers({ Accept: 'application/json' });
  }
  const  token = JSON.parse(localStorage.getItem('auth')).Token;
  options.headers.set('authorization', 'Bearer' + ' ' +token);
  const email = JSON.parse(localStorage.getItem('auth')).username;
  options.headers.set('From',email);
  return fetchUtils.fetchJson(url, options);
};

export default {
  getList: (resource, params) => {
    const { page, perPage } = params.pagination;
    const { field, order } = params.sort;
    const query = {
      sort: JSON.stringify([field, order]),
      range: JSON.stringify([(page - 1) * perPage, page * perPage - 1]),
      filter: JSON.stringify(params.filter),
    };
    const role = JSON.parse(localStorage.getItem('auth')).role;
    const apiUrl = role==0 ?'http://localhost:3000/admin':"http://localhost:3000/user";

    const url = `${apiUrl}/${resource}?${stringify(query)}`;

    return httpClient(url).then(({ headers, json }) => ({
      data: json.map((resource) => ({ ...resource, id: resource._id })),
      total: parseInt(headers.get('content-range').split('/').pop(), 10),
    }));
  },
  getOne: (resource, params) =>{
    const role = JSON.parse(localStorage.getItem('auth')).role;
    const apiUrl = role==0 ?'http://localhost:3000/admin':"http://localhost:3000/user";

    return httpClient(`${apiUrl}/${resource}/${params.id}`).then(({ json }) => ({
      data: { ...json, id: json._id }, //!
    }));},

  getMany: (resource, params) => {
    const query = {
      filter: JSON.stringify({ id: params.ids }),
    };
    const role = JSON.parse(localStorage.getItem('auth')).role;
    const apiUrl = role==0 ?'http://localhost:3000/admin':"http://localhost:3000/user";

    const url = `${apiUrl}/${resource}?${stringify(query)}`;
    return httpClient(url).then(({ json }) => ({
      data: json.map((resource) => ({ ...resource, id: resource._id })),
    }));
  },

  getManyReference: (resource, params) => {
    const { page, perPage } = params.pagination;
    const { field, order } = params.sort;
    const query = {
      sort: JSON.stringify([field, order]),
      range: JSON.stringify([(page - 1) * perPage, page * perPage - 1]),
      filter: JSON.stringify({
        ...params.filter,
        [params.target]: params.id,
      }),
    };
    const role = JSON.parse(localStorage.getItem('auth')).role;
    const apiUrl = role==0 ?'http://localhost:3000/admin':"http://localhost:3000/user";    
    const url = `${apiUrl}/${resource}?${stringify(query)}`;

    return httpClient(url).then(({ headers, json }) => ({
      data: json.map((resource) => ({ ...resource, id: resource._id })),
      total: parseInt(headers.get('content-range').split('/').pop(), 10),
    }));
  },

  update: (resource, params) =>{
    const role = JSON.parse(localStorage.getItem('auth')).role;
    const apiUrl = role==0 ?'http://localhost:3000/admin':"http://localhost:3000/user";
    return httpClient(`${apiUrl}/${resource}/${params.id}`, {
      method: 'PUT',
      body: JSON.stringify(params.data),
    }).then(({ json }) => ({
      data: { ...params.data, id: json._id },
    }));},

  updateMany: (resource, params) => {
    const query = {
      filter: JSON.stringify({ id: params.ids }),
    };
    const role = JSON.parse(localStorage.getItem('auth')).role;
    const apiUrl = role==0 ?'http://localhost:3000/admin':"http://localhost:3000/user";
    return httpClient(`${apiUrl}/${resource}?${stringify(query)}`, {
      method: 'PUT',
      body: JSON.stringify(params.data),
    }).then(({ json }) => ({ data: json }));
  },

  create: (resource, params) =>{
    const role = JSON.parse(localStorage.getItem('auth')).role;
    const apiUrl = role==0 ?'http://localhost:3000/admin':"http://localhost:3000/user";
    return httpClient(`${apiUrl}/${resource}`, {
      method: 'POST',
      body: JSON.stringify(params.data),
    }).then(({ json }) => ({
      data: { ...params.data, id: json._id },
    }));},

  delete: (resource, params) =>{
    const role = JSON.parse(localStorage.getItem('auth')).role;
    const apiUrl = role==0 ?'http://localhost:3000/admin':"http://localhost:3000/user";
    return httpClient(`${apiUrl}/${resource}/${params.id}`, {
      method: 'DELETE',
      body: JSON.stringify(params.id),
    }).then(({ json }) => ({
      ...json,
      id: json._id,
    }));},

    deleteMany: (resource, params) => {
      const role = JSON.parse(localStorage.getItem('auth')).role;
      const apiUrl = role==0 ?'http://localhost:3000/admin':"http://localhost:3000/user";      
      return httpClient(`${apiUrl}/${resource}`, {
        method: 'DELETE',
        body: JSON.stringify(params.ids),
      }).then(({ json }) => ({ data: json }));
    },
    //URLやと文字列制限あり
};