import "./App.css";
import Pizzas from "./components/Pizzas";
import Restaurants from "./components/Restaurants";

function App() {
  return (
    <div className="App">
      <Restaurants />
      <Pizzas />
    </div>
  );
}

export default App;
