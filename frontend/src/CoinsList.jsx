import React from "react"

const CoinsList = ({ coins, updateCoin, updateCallback }) => {
    const onDelete = async (id) => {
        try {
            const options = {
                method: "DELETE"
            }
            const response = await fetch(`http://localhost:8002/api/coins/${id}/delete/`, options)
            if (response.status === 202) {
                updateCallback()
            } else {
                console.error("Failed to delete")
            }
        } catch (error) {
            alert(error)
        }
    }

    return <div>
        <h2>Coins</h2>
        <table>
            <thead>
                <tr>
                    <th>Id</th>
                    <th>Name</th>
                    <th>Symbol</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                {coins.map((coin) => (
                    <tr key={coin.id}>
                        <td>{coin.id}</td>
                        <td>{coin.name}</td>
                        <td>{coin.symbol}</td>
                        <td>
                            <button onClick={() => updateCoin(coin)}>Update</button>
                            <button onClick={() => onDelete(coin.id)}>Delete</button>
                        </td>
                    </tr>
                ))}
            </tbody>
        </table>
    </div>
}

export default CoinsList