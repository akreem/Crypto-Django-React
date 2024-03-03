import { useState } from "react";

const CoinForm = ({ existingCoin = {}, updateCallback}) => {
    const [name, setName] = useState(existingCoin.name || "");
    const [symbol, setSymbol] = useState(existingCoin.symbol || "");

    const updating = Object.entries(existingCoin).length !== 0

    const onSubmit = async (e) => {
        e.preventDefault()

        const data = {
            name,
            symbol
        }
        const url = "http://localhost:8002/api/coins/" + (updating ? `${existingCoin.id}/update/` : "create/")
        const options = {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        }
        const response = await fetch(url, options)

        if (response.status !== 201 && response.status !== 200) {
            const data = await response.json()
            alert(data.message)
        } else {
            updateCallback()
        }
    }

    return (
        <form onSubmit={onSubmit}>
            <div>
                <label htmlFor="name">Name:</label>
                <input
                    type="text"
                    id="name"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                />
            </div>
            <div>
                <label htmlFor="symbol">Symbol:</label>
                <input
                    type="text"
                    id="symbol"
                    value={symbol}
                    onChange={(e) => setSymbol(e.target.value)}
                />
            </div>
            <button type="submit">{updating ? "update" : "Create"}</button>
        </form>
    );
};

export default CoinForm