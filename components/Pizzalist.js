// PizzaList.js
import React, { useEffect, useState } from 'react';

const PizzaList = () => {
  const [pizzas, setPizzas] = useState([]);

  useEffect(() => {
    fetch(`https://pizza-e63i.onrender.com/${id}`).then((r) => {
        if (r.ok) {
          r.json().then((hero) =>
            setHero({ data: hero, error: null, status: "resolved" })
          );
        } else {
          r.json().then((err) =>
            setHero({ data: null, error: err.error, status: "rejected" })
          );
        }
      });
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
