import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Dashboard from "./pages/Dashboard";
import JobForm from "./components/JobForm";
import EditJob from "./pages/EditJob";

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/add" element={<JobForm />} />
        <Route path="/edit/:id" element={<EditJob />} />
        {/* Future edit route: */}
        {/* <Route path="/edit/:id" element={<EditForm />} /> */}
      </Routes>
    </Router>
  );
};

export default App;
