import './App.css';
import React from "react";
import Game from './Components/Game';

function App() 
{
  console.log('App Component Rendered!!')
    return(
      <div className="app">
        <center>
        <h1> Flip Card Game</h1>
        </center>
        <Game/>
      </div>
    )
}
export default App;