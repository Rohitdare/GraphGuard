import React, { useState } from "react";
import GraphView from "./GraphView";

function App() {

  const [account, setAccount] = useState("");
  const [elements, setElements] = useState([]);

const traceAccount = async () => {

  try {

    const res = await fetch(`http://127.0.0.1:8000/trace/${account}`);

    const data = await res.json();

    console.log(data);

    const nodes = data.nodes.map(node => ({
      data: { id: node }
    }));

    const edges = data.edges.map(edge => ({
      data: { source: edge.source, target: edge.target }
    }));

    setElements([...nodes, ...edges]);

  } catch (error) {
    console.error("API Error:", error);
  }

};

  return (

    <div style={{ padding: "20px" }}>

      <h2>GraphGuard Investigation Dashboard</h2>

      <input
        placeholder="Enter Account ID"
        value={account}
        onChange={(e) => setAccount(e.target.value)}
      />

      <button onClick={traceAccount}>
        Trace
      </button>

      <GraphView elements={elements} />

    </div>

  );
}

export default App;