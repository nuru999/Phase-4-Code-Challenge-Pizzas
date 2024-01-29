import Restaurant from "./Restaurant";

function Pizzas({ restaurants }) {
  const mapped = restaurants.map((res) => (
    <span key={res.id}>
      <Restaurant
        id={res.id}
        name={res.name}
        ingredients={res.ingredients}
        image={res.image}
        price={res.price}
      />
    </span>
  ));

  return <div className="home">{mapped}</div>;
}

export default Pizzas;
