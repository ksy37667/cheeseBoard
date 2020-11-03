import React from 'react'
import axios from 'axios';




export const BoardDetail = () => {
    const BoardsDetail = async (id) => {
        const response = await axios.get('http://127.0.0.1:8000/boards/brd/' + id);
        console.log(response.data);
        return response.data;
    }

    return (
        <div>
            {BoardDetail(1)}
        </div>
    )
}

