import React from "react";
import "./Card.css";

const Card = ({ symbol, flipped, matched, onClick }) => {
    return (
      <div className={`card ${flipped ? "flipped" : ""} ${matched ? "matched" : ""}`} onClick={onClick}>
        <div className="card-inner">
          <div className="card-back">{symbol}</div>
          <div className="card-front">🎭</div>
        </div>
      </div>
    );
  };
  

export default Card;
