import logo from './logo.svg';
import './App.css';
import AddGroup from './cpmponents/AddGroup';
import FlashCardGroup from './cpmponents/FlashCardGroup';

function App() {
  return (
    <div className="App">
      <div style={{margin:"1rem",padding:"1rem"}}>
        <h1 style={{marginBottom:"1rem"}}>Flash Cards</h1>
        <AddGroup/>
        <FlashCardGroup/>

      </div>
      
     
    </div>
  );
}

export default App;
