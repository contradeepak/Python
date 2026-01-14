import React from "react";

class ServicesComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      listofusers: props.listofusers || []
    }
    console.log("list of users in services component ", this.state.listofusers);
  }

  render() {
    return (
      <div>
        <h2>Service Component</h2>
        <p>This is a simple Service component.</p>

        <ul>
          {this.state.listofusers.map((user) => (
            <li key={user.id}>Id: {user.id} -Name: {user.name} -Website: {user.website}</li>
          ))}
        </ul>

      </div>
    );
  }
}

export default ServicesComponent;