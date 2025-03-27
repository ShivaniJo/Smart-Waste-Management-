import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav className="bg-blue-600 p-4 text-white flex justify-between">
      <h1 className="text-xl font-bold">Smart Waste Management</h1>
      <div>
        <Link to="/" className="mr-4">Dashboard</Link>
        <Link to="/login">Login</Link>
      </div>
    </nav>
  );
}
