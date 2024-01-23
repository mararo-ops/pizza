// RestaurantList.js
import React, { useEffect, useState } from 'react';

const RestaurantList = () => {
  const [restaurants, setRestaurants] = useState([]);

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
      <h2>Restaurant List</h2>
      <ul>
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
