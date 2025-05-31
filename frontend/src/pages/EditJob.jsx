import React, { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import { getJobs, updateJob } from "../api";

const EditJob = () => {
  const { id } = useParams(); // Get job ID from URL
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    company: "",
    role: "",
    status: "Applied",
    notes: "",
  });

  // Fetch job data when component mounts
  useEffect(() => {
    const fetchJob = async () => {
      try {
        const res = await getJobs(); // Assuming backend doesn't support GET /jobs/:id
        const job = res.data.find((j) => j.id === parseInt(id));
        if (job) setFormData(job);
      } catch (error) {
        console.error("Failed to load job:", error);
      }
    };

    fetchJob();
  }, [id]);

  // Handle input changes
  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  // Submit updated job
  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await updateJob(id, formData);
      navigate("/");
    } catch (error) {
      console.error("Failed to update job:", error);
    }
  };

  return (
    <div className="max-w-xl mx-auto p-6">
      <h2 className="text-2xl font-bold mb-4">Edit Job</h2>

      <form onSubmit={handleSubmit} className="space-y-4">
        <input
          type="text"
          name="company"
          value={formData.company}
          onChange={handleChange}
          placeholder="Company"
          className="w-full border p-2 rounded"
          required
        />

        <input
          type="text"
          name="role"
          value={formData.role}
          onChange={handleChange}
          placeholder="Role"
          className="w-full border p-2 rounded"
          required
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
          value={formData.notes}
          onChange={handleChange}
          placeholder="Interview notes..."
          className="w-full border p-2 rounded"
        />

        <button
          type="submit"
          className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
        >
          Update Job
        </button>
      </form>
    </div>
  );
};

export default EditJob;
