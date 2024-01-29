import React, { useState, useEffect } from 'react';

const Pizzas = () => {
  const [pizzas, setPizzas] = useState([]);

  useEffect(() => {
    fetch('https://pizza-restaurant-domain.onrender.com/pizzas')
      .then(response => response.json())
      .then(data => setPizzas(data))
      .catch(error => console.error('Error fetching pizzas:', error));
  }, []);

  return  (
    <div className="pizzas" >
      <h2>Pizza List</h2>
      <ul>
        {pizzas.map(pizza => (
          <li key={pizza.id}>
            <strong>{pizza.name}</strong>: {pizza.ingredients}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Pizzas;
