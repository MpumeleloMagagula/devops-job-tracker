import axios from "axios";

const BASE_URL = "http://localhost:8000"; // Will Adjust later for production

export const getJobs = () => axios.get(`${BASE_URL}/jobs`);
export const createJob = (data) => axios.post(`${BASE_URL}/jobs`, data);
export const updateJob = (id, data) => axios.put(`${BASE_URL}/jobs/${id}`, data);
export const deleteJob = (id) => axios.delete(`${BASE_URL}/jobs/${id}`);
