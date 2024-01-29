import React from "react";

export default function Restaurant({ id, name, ingredients, image, price }) {
  // console.log(id,name,address);
  return (
    <div className="card">
      <img src={image} class="card-img" alt="" />
      <div className="card-body">
        <div className="pizza_name">
          <h1 className="card-title">{name}</h1>
          <h1 className="card-price">{price}</h1>
        </div>
        <p className="card-sub-title">{}</p>
        <p className="card-info">{ingredients}</p>
        <div className="btn-div">
          <button className="card-btn">order</button>
        </div>
      </div>
    </div>
  );
}
