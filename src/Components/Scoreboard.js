import React from 'react';

const Scoreboard = ({ score, currentPlayer }) => {
  return (
    <div className="scoreboard">
      <div className="scoreboard-player">
        <span>Player 1:</span>
        <span className="scoreboard-score">{score.player1}</span>
      </div>
      <div className="scoreboard-player">
        <span>Player 2:</span>
        <span className="scoreboard-score">{score.player2}</span>
      </div>
      <div className="scoreboard-player">
        <span>Current Player:</span>
        <span className={`scoreboard-score ${currentPlayer === 1 ? 'current-player' : ''}`}>1</span>
        <span className={`scoreboard-score ${currentPlayer === 2 ? 'current-player' : ''}`}>2</span>
      </div>
    </div>
  );
};

export default Scoreboard;
