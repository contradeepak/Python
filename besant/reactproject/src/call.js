import React from "react";

class CallComponent extends React.Component {

    render() {
        const { listofusers = [] } = this.props;
        console.log("list of users in call component ", listofusers);
        return (
            <div>
                <h2>Call Component</h2>
                <p>This is a simple call component.</p>

            <ul>
                {listofusers.map((user) => (
                    <li key={user.id}>Id: {user.id} -Name: {user.name} -Phone: {user.phone}</li>
                ))}
            </ul>

            </div>
        );
    }
}

export default CallComponent;