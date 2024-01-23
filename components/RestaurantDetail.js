// RestaurantDetail.js
import React, { useEffect, useState } from 'react';

const RestaurantDetail = ({ match }) => {
  const restaurantId = match.params.id;
  const [restaurant, setRestaurant] = useState(null);

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
  }, [restaurantId]);

  return (
    <div>
      <h2>Restaurant Detail</h2>
      {restaurant ? (
        <div>
          <h3>{restaurant.name}</h3>
          <p>{restaurant.address}</p>
          <h4>Pizzas:</h4>
          <ul>
            {/* Map through the pizzas of the restaurant and display each one */}
            {restaurant.pizzas.map((pizza) => (
              <li key={pizza.id}>
                {pizza.name} - {pizza.ingredients}
              </li>
            ))}
          </ul>
        </div>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
};

export default RestaurantDetail;
