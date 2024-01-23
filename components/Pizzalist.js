// PizzaList.js
import React, { useEffect, useState } from 'react';

const PizzaList = () => {
  const [pizzas, setPizzas] = useState([]);

  useEffect(() => {
    // Fetch data from /pizzas API endpoint
    // Update the state with the fetched pizzas
  }, []);

  return (
    <div>
      <h2>Pizza List</h2>
      <ul>
        {/* Map through the pizzas and display each one */}
        {pizzas.map((pizza) => (
          <li key={pizza.id}>
            {pizza.name} - {pizza.ingredients}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default PizzaList;
