import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import RestaurantList from './RestaurantList';
import RestaurantDetail from './RestaurantDetail';
import PizzaList from './PizzaList';

const App = () => {
  return (
    <Router>
      <div>
        <Switch>
          <Route path="/restaurants/:id" component={RestaurantDetail} />
          <Route path="/restaurants" component={RestaurantList} />
          <Route path="/pizzas" component={PizzaList} />
        </Switch>
      </div>
    </Router>
  );
};

export default App;
