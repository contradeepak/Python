import UsersComponent from "./users";
import ServicesComponent from "./services";
import CallComponent from "./call";
import EmailComponent from "./email";
import { Route, Routes, Link } from "react-router-dom";
import { useState, useEffect } from "react";

function HeaderComponent() {

    const [users, setUsers] = useState([]);

    useEffect(() => {
        fetch("https://jsonplaceholder.typicode.com/users")
            .then((response) => response.json())
            .then((data) => setUsers(data))
            .catch((error) => console.error("Error fetching users:", error));
    }, []);

    console.log("Fetched users in Header Component:", users);
    return (
        <header>
            <nav className="navbar navbar-expand-lg navbar-light bg-light">
                <div className="container-fluid">
                    <Link className="navbar-brand" to={"/"}>Brand</Link>
                    <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                        <span className="navbar-toggler-icon"></span>
                    </button>
                    <div className="collapse navbar-collapse" id="navbarSupportedContent">
                        <ul className="navbar-nav me-auto mb-2 mb-lg-0">
                            <li className="nav-item">
                                <Link className="nav-link" to={"/users"}>Users</Link>
                            </li>
                            <li className="nav-item">
                                <Link className="nav-link" to={"/services"}>Services</Link>
                            </li>
                            <li className="nav-item dropdown">
                                <Link className="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                                    Contacts
                                </Link>
                                <ul className="dropdown-menu" aria-labelledby="navbarDropdown">
                                    <li><Link className="dropdown-item" to={"/call"}>Call</Link></li>
                                    <li><Link className="dropdown-item" to={"/email"}>Email</Link></li>
                                </ul>
                            </li>
                        </ul>
                        <form className="d-flex">
                            <input className="form-control me-2" type="search" placeholder="Search" aria-label="Search" />
                            <button className="btn btn-outline-success" type="submit">Search</button>
                        </form>
                    </div>
                </div>
            </nav>
            <Routes>
                <Route path="/" />
                <Route path="/users" element={<UsersComponent usersdata={users} />} />
                <Route path="/services" element={<ServicesComponent listofusers={users} />} />
                <Route path="/call" element={<CallComponent listofusers={users} />} />
                <Route path="/email" element={<EmailComponent />} />
            </Routes>
        </header>

    )
}

export default HeaderComponent;