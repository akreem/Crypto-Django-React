import { useState, useEffect } from "react";
import CoinsList from "./CoinsList";
import "./App.css";
import CoinForm from "./CoinForm";
//import ContactForm from "./ContactForm";

function App() {
  const [coins, setCoins] = useState([]);
  const [isModalOpen, setIsModalOpen] = useState(false)
  const [currentCoin, setCurrentCoin] = useState({})

  useEffect(() => {
    fetchCoins()
  }, []);

  const fetchCoins = async () => {
    const response = await fetch("http://localhost:8002/api/coins/all/");
    const data = await response.json();
    setCoins(data.coins);
    console.log(data.coins);
  };

  const closeModal = () => {
    setIsModalOpen(false)
    setCurrentCoin({})
  }

  const openCreateModal = () => {
    if (!isModalOpen) setIsModalOpen(true)
  }

  const openEditModal = (coin) => {
    if (isModalOpen) return
      setCurrentCoin(coin)
      setIsModalOpen(true)
    }

  const onUpdate = () => {
    closeModal()
    fetchCoins()
  }

  return <>
  <CoinsList coins={coins} updateCoin={openEditModal} updateCallback={onUpdate}/>
  <button onClick={openCreateModal}>Create New Coin</button>
    {
      isModalOpen && <div className="modal">
        <div className="modal-content">
          <span className="close" onClick={closeModal}>&times;</span>
        <CoinForm existingCoin={currentCoin} updateCallback={onUpdate}/>
        </div>
      </div>
    }
    </>
}

export default App;
