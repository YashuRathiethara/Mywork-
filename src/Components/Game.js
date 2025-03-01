import React, { useState, useEffect } from "react";
import Card from "./Card";
import "./Game.css";

const symbols = ["A", "B", "C", "D"]; 
const totalPairs = 16; 

const generateCards = () => {
  let cardList = [];
  for (let i = 0; i < totalPairs; i++) {
    let symbol = symbols[i % symbols.length]; 
    cardList.push({ id: i * 2, symbol, flipped: false, matched: false });
    cardList.push({ id: i * 2 + 1, symbol, flipped: false, matched: false });
  }
  return cardList.sort(() => Math.random() - 0.5);
};

const Game = () => {
  const [cards, setCards] = useState(generateCards());
  const [flippedCards, setFlippedCards] = useState([]); 
  const [player, setPlayer] = useState(1);
  const [score, setScore] = useState({ player1: 0, player2: 0 });

  const handleCardClick = (id) => {
    if (flippedCards.length === 2) return; 

    const updatedCards = cards.map((card) =>
      card.id === id ? { ...card, flipped: true } : card
    );

    setCards(updatedCards);
    setFlippedCards([...flippedCards, id]);
  };
  
  useEffect(() => {
    if (flippedCards.length === 2) {
      const [firstId, secondId] = flippedCards;
      const firstCard = cards.find((card) => card.id === firstId);
      const secondCard = cards.find((card) => card.id === secondId);

      if (firstCard.symbol === secondCard.symbol) {
        setTimeout(() => {
          setCards((prevCards) =>
            prevCards.map((card) =>
              card.id === firstId || card.id === secondId
                ? { ...card, matched: true }
                : card
            )
          );

          setScore((prevScore) => ({...prevScore,[`player${player}`]: prevScore[`player${player}`] + 1,}));
        }, 500);
      } else {
        setTimeout(() => {
          setCards((prevCards) =>
            prevCards.map((card) =>
              card.id === firstId || card.id === secondId
                ? { ...card, flipped: false }
                : card
            )
          );
          setPlayer(player === 1 ? 2 : 1); 
        }, 1000);
      }
      setFlippedCards([]);
    }
  }, [flippedCards]);

  const restartGame = () => {
    setCards(generateCards());
    setFlippedCards([]);
    setPlayer(1);
    setScore({ player1: 0, player2: 0 });
  };

  const allMatched = cards.every((card) => card.matched);
  return (
    <div className="game-container">
    <center>
      <p>Player 1: {score.player1} | Player 2: {score.player2}</p>
      <p>Current Turn: Player {player}</p>
      
    </center>

      <div className="card-grid">
        {cards.map((card) => (
          <Card
            key={card.id}
            symbol={card.symbol}
            flipped={card.flipped}
            matched={card.matched}
            onClick={() => !card.flipped && !card.matched && handleCardClick(card.id)}
          />
        ))}
      </div>

      {allMatched && (
        <div className="winner-message">
          <center>
            <h3>
            {score.player1 > score.player2
              ? " Player 1 Wins!"
              : score.player1 < score.player2
              ? " Player 2 Wins!"
              : " It's a Tie!"}
          </h3>
          
          <button onClick={restartGame}>Restart Game</button>
          </center>
        </div>
      )}
    </div>
  );
};

export default Game;
