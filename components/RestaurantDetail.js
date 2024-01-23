// RestaurantDetail.js
import React, { useEffect, useState } from 'react';

const RestaurantDetail = ({ match }) => {
  const restaurantId = match.params.id;
  const [restaurant, setRestaurant] = useState(null);

  useEffect(() => {
    // Fetch data from /restaurants/:id API endpoint using restaurantId
    // Update the state with the fetched restaurant details
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
