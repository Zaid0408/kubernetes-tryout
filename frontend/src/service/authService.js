import axios from "axios";

// const BASE_URL = "http://localhost:8000"; local setup
const BASE_URL = 'http://login-app.local/api'; // kubernetes set up


export const loginUser= async(username, password) =>{
    try {
        const response= await axios.post(`${BASE_URL}/auth/login`,{
            username,
            password
        })

        if (response.token) {
            localStorage.setItem('token', response.data.token);
        }
          
        return response.data;
    } catch (error) {
        if (error.response) {
            // Server responded with error
            throw new Error(error.response.data.detail || 'Login failed');
            } 
            else if (error.request) {
            // Request made but no response
            throw new Error('Cannot connect to server. Make sure backend is running.');
            } 
            else {
            // Something else happened
            throw new Error('An error occurred');
        }
        
    }
}

export const logout = ()=>{
    localStorage.removeItem('token');
}

export const getToken = () => localStorage.getItem('token');

export const isAuthenticated = () => {
    return !!getToken();
  };