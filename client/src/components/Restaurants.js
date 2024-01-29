import React, { useState, useEffect } from "react";

const Restaurants = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const response = await fetch(
        "https://pizza-restaurant-domain.onrender.com/restaurants"
      );
      const result = await response.json();
      setData(result);
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  const handleDelete = async (id) => {
    try {
      const response = await fetch(
        `https://pizza-restaurant-domain.onrender.com/restaurants/${id}`,
        {
          method: "DELETE",
        }
      );

      if (response.status === 204) {
        setData((prevData) =>
          prevData.filter((restaurant) => restaurant.id !== id)
        );
      } else {
        console.error("Error deleting data. Status:", response.status);
      }
    } catch (error) {
      console.error("Error deleting data:", error);
    }
  };

  return (
    <div className=" restaurants " >
      <h2>Our Restaurants</h2>
      <ul>
        {data.map((restaurant) => (
          <li key={restaurant.id}>
            <strong>{restaurant.name}</strong>: {restaurant.address}
            <button onClick={() => handleDelete(restaurant.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Restaurants;
