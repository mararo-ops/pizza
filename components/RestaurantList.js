// RestaurantList.js
import React, { useEffect, useState } from 'react';

const RestaurantList = () => {
  const [restaurants, setRestaurants] = useState([]);

  useEffect(() => {
    // Fetch data from /restaurants API endpoint
    // Update the state with the fetched restaurants
  }, []);

  return (
    <div>
      <h2>Restaurant List</h2>
      <ul>
        {/* Map through the restaurants and display each one */}
        {restaurants.map((restaurant) => (
          <li key={restaurant.id}>
            {restaurant.name} - {restaurant.address}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default RestaurantList;
