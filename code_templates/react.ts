 
import React, { Component } from "react";
 
class Sentiment extends Component {
  state = {
    data: []
  };
 
  // Code is invoked after the component is mounted/inserted into the DOM tree.
  componentDidMount() {
    const word = 'im a developer';
    const URL ="https://sentiment-analytics-api.herokuapp.com/?text="+word;
 
    fetch(URL)
      .then(result => result.json())
      .then(result => {
        this.setState({
          data: result
        });
      });
  }
 
  render() {
    const { data } = this.state;
 
    const result = data.map((entry, index) => {
      return <li key={index}>{entry}</li>;
    });
 
    return <ul>{result}</ul>;
  }
}
 
export default Sentiment;