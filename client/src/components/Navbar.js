import React from "react";
import { NavLink, Outlet } from "react-router-dom";

function Navbar() {
  //NavLink by default has an object and it has a  property called isActive
  //which is set to true or false  depending on whether the NavLink components
  // are styled or not  so we destructure it to use
  function navStyle({ isActive }) {
    return {
      fontWeight: isActive ? "bold" : "normal",
    };
  }
  return (
    <div>
      <header>
        <nav>
          <h1>PIZZARIA</h1>
          <NavLink style={navStyle} to="/Pizzas">
            Pizzas
          </NavLink>
        </nav>
      </header>
      <main>
        <Outlet />
      </main>
    </div>
  );
}

export default Navbar;
