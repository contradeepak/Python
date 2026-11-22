function UsersComponent({ usersdata = [] }) {

    console.log("Users data in Users Component:", usersdata);

    return (
        <table className="table">
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Email</th>
                    <th>Phone</th>
                </tr>
            </thead>
            <tbody>
                {usersdata.map((user) => (
                    <tr key={user.id}>
                        <td>{user.name}</td>
                        <td>{user.email}</td>
                        <td>{user.phone}</td>
                    </tr>
                ))}
            </tbody>
        </table>

    );
}

export default UsersComponent;