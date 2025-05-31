import React, { useState } from "react";
import { createJob } from "../api";
import { useNavigate } from "react-router-dom";

const JobForm = () => {
  // Local form state
  const [formData, setFormData] = useState({
    company: "",
    role: "",
    status: "Applied",
    notes: "",
  });

  const navigate = useNavigate();

  // Handle form input changes
  const handleChange = (e) => {
    setFormData({
      ...formData, // keep existing data
      [e.target.name]: e.target.value, // update changed field
    });
  };

  // Handle form submit
  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      await createJob(formData); // Call backend API
      navigate("/"); // Go back to dashboard
    } catch (error) {
      console.error("Error creating job:", error);
    }
  };

  return (
    <div className="max-w-xl mx-auto p-6">
      <h2 className="text-2xl font-bold mb-4">Add New Job</h2>

      <form onSubmit={handleSubmit} className="space-y-4">
        <input
          type="text"
          name="company"
          placeholder="Company"
          value={formData.company}
          onChange={handleChange}
          required
          className="w-full border p-2 rounded"
        />

        <input
          type="text"
          name="role"
          placeholder="Role"
          value={formData.role}
          onChange={handleChange}
          required
          className="w-full border p-2 rounded"
        />

        <select
          name="status"
          value={formData.status}
          onChange={handleChange}
          className="w-full border p-2 rounded"
        >
          <option>Applied</option>
          <option>Interviewing</option>
          <option>Offer</option>
          <option>Rejected</option>
        </select>

        <textarea
          name="notes"
          placeholder="Interview feedback, recruiter name, etc."
          value={formData.notes}
          onChange={handleChange}
          className="w-full border p-2 rounded"
        />

        <button
          type="submit"
          className="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700"
        >
          Submit
        </button>
      </form>
    </div>
  );
};

export default JobForm;
