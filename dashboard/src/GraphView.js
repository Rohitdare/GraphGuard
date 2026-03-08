import React, { useEffect } from "react";
import cytoscape from "cytoscape";

const GraphView = ({ elements }) => {
  useEffect(() => {
    // 1. Assign to 'cy' inside the effect
    const cy = cytoscape({
      container: document.getElementById("graph"),
      elements: elements,
      style: [
        {
          selector: "node",
          style: {
            label: "data(id)",
            "background-color": "#0074D9",
            color: "#fff",
          },
        },
        {
          selector: ".fraud",
          style: {
            "background-color": "red",
          },
        },
      ],
      layout: {
        name: "cose", // Note: 'cose-bilkent' requires an extra plugin; using 'cose' for now
        animate: true,
      },
    });

    // 2. Attach the listener INSIDE the effect where 'cy' is defined
    cy.on("tap", "node", function (evt) {
      const node = evt.target;
      alert("Account: " + node.id());
    });

    // Clean up on unmount
    return () => {
      cy.destroy();
    };
  }, [elements]);

  return <div id="graph" style={{ width: "100%", height: "600px" }} />;
};

export default GraphView;