import React, { useEffect, useState } from "react";
import { getJobs, deleteJob } from "../api";
import { Link } from "react-router-dom";

const Dashboard = () => {
  const [jobs, setJobs] = useState([]);
  const [searchQuery, setSearchQuery] = useState(""); // Text input for search
  const [statusFilter, setStatusFilter] = useState("All"); // Dropdown for status filter
  const [sortOrder, setSortOrder] = useState("newest"); // Dropdown for sort order

  // Fetch job data on initial render
  useEffect(() => {
    const fetchJobs = async () => {
      const data = await getJobs();
      setJobs(data);
    };

    fetchJobs();
  }, []);

  // Handle deleting a job by ID
  const handleDelete = async (id) => {
    if (window.confirm("Are you sure you want to delete this job?")) {
      await deleteJob(id);
      setJobs(jobs.filter((job) => job.id !== id)); // Update UI after delete
    }
  };

  // Filter, search and sort the jobs list
  const filteredJobs = jobs
    .filter((job) => {
      // Status filtering logic
      if (statusFilter !== "All" && job.status !== statusFilter) return false;

      // Search by company or role (case-insensitive)
      const query = searchQuery.toLowerCase();
      return (
        job.company.toLowerCase().includes(query) ||
        job.role.toLowerCase().includes(query)
      );
    })
    .sort((a, b) => {
      // Sort jobs by creation date
      const dateA = new Date(a.created_at);
      const dateB = new Date(b.created_at);
      return sortOrder === "newest" ? dateB - dateA : dateA - dateB;
    });

  return (
    <div className="p-6">
      <h1 className="text-3xl font-bold mb-6">Job Applications Dashboard</h1>

      {/* Controls for search, filter and sort */}
      <div className="flex flex-wrap gap-4 mb-6">
        {/* Search input */}
        <input
          type="text"
          placeholder="Search by company or role..."
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
          className="p-2 border rounded w-60"
        />

        {/* Filter by status dropdown */}
        <select
          value={statusFilter}
          onChange={(e) => setStatusFilter(e.target.value)}
          className="p-2 border rounded"
        >
          <option value="All">All</option>
          <option value="Applied">Applied</option>
          <option value="Interviewing">Interviewing</option>
          <option value="Offer">Offer</option>
          <option value="Rejected">Rejected</option>
        </select>

        {/* Sort order dropdown */}
        <select
          value={sortOrder}
          onChange={(e) => setSortOrder(e.target.value)}
          className="p-2 border rounded"
        >
          <option value="newest">Newest First</option>
          <option value="oldest">Oldest First</option>
        </select>
      </div>

      {/* Job Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {filteredJobs.map((job) => (
          <div
            key={job.id}
            className="bg-white shadow p-4 rounded-md flex flex-col justify-between"
          >
            <div>
              <h3 className="text-lg font-bold">{job.role}</h3>
              <p className="text-sm text-gray-500 mb-2">{job.company}</p>
              <span
                className={`inline-block px-2 py-1 text-xs font-semibold rounded-full ${
                  job.status === "Applied"
                    ? "bg-blue-100 text-blue-800"
                    : job.status === "Interviewing"
                    ? "bg-yellow-100 text-yellow-800"
                    : job.status === "Offer"
                    ? "bg-green-100 text-green-800"
                    : "bg-red-100 text-red-800"
                }`}
              >
                {job.status}
              </span>
              <p className="mt-2 text-sm text-gray-700">{job.notes}</p>
            </div>

            {/* Actions: Edit & Delete */}
            <div className="mt-4 flex justify-between items-center">
              <Link
                to={`/edit/${job.id}`}
                className="text-blue-500 hover:underline"
              >
                Edit
              </Link>
              <button
                onClick={() => handleDelete(job.id)}
                className="text-red-500 hover:underline"
              >
                Delete
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Dashboard;
