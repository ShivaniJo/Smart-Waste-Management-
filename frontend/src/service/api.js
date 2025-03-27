import axios from "axios";

const API_URL = "http://127.0.0.1:8000";

export const fetchSensors = async () => {
  const response = await axios.get(`${API_URL}/sensors/`);
  return response.data;
};

export const loginUser = async (email, password) => {
  const response = await axios.post(`${API_URL}/users/login`, { email, password });
  return response.data;
};

export const fetchOptimizedRoutes = async () => {
  const response = await axios.get(`${API_URL}/api/optimize-routes`);
  return response.data.routes;
};
