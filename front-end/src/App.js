import React, { useState ,useEffect } from 'react';
import axios from 'axios';
import TableRow from '@material-ui/core/TableRow';
import TableCell from '@material-ui/core/TableCell';




const App = (props) => {
  const [test, setTest] = useState('')

  const apiCall = async () => {
    let email = "test1@naver.com";
    let password = "testuser1";
    const response = await axios.post('http://127.0.0.1:8000/accounts/login/', {
      email,
      password
    }).then(response => {
      if (response.data.token) {
        console.log(response.data);
        localStorage.setItem("access_token", JSON.stringify(response.data));
      }
      console.log(localStorage)
    })
  };

  const logout = () =>{
    localStorage.removeItem('user');
  }

  
  useEffect(() => {
    logout();
    apiCall();
  }, []);

  return (
    <div>
    <TableRow>
      <TableCell>test</TableCell>
      <TableCell>test</TableCell>
      <TableCell>test</TableCell>
      <TableCell>test</TableCell>
    </TableRow>
    </div>

  )
};

export default App;

// import React, { Component } from "react";
// import axiosInstance from "./axiosApi";

// class App extends Component {
//     constructor(props) {
//         super(props);
//         this.state = {email: "", password: ""};

//         this.handleChange = this.handleChange.bind(this);
//         this.handleSubmit = this.handleSubmit.bind(this);
//     }

//     handleChange(event) {
//         this.setState({[event.target.name]: event.target.value});
//     }

//     handleSubmit(event) {
//         event.preventDefault();
//         try {
//             const response = axiosInstance.post('/accounts/login/', {
//                 email: this.state.email,
//                 passwrod: this.state.password
//             });
//             axiosInstance.defaults.headers['Authorization'] = "JWT " + response.data.access;
//             localStorage.setItem('access_token', response.data.access);
//             // localStorage.setItem('refresh_token', response.data.refresh);
//             return localStorage;
//         } catch (error) {
//             throw error;
//         }
//     }

//     render() {
//         return (
//             <div>
//                 Login
//                 <form onSubmit={this.handleSubmit}>
//                     <label>
//                         email:
//                         <input name="email" type="text" value={this.state.email} onChange={this.handleChange}/>
//                     </label>
//                     <label>
//                         Password:
//                         <input name="password" type="password" value={this.state.password} onChange={this.handleChange}/>
//                     </label>
//                     <input type="submit" value="Submit"/>
//                 </form>
//             </div>
//         )
//     }
// }
// export default App;