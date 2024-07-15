import React from 'react';
import './MainMenu.css';

const MainMenu = () => {
    return (
        <div className="mainmenu-container">
            <div className="mainmenu-image left">
                <img src="https://via.placeholder.com/300x600" alt="Left" />
            </div>
            <div className="mainmenu-center">
                <div className="leaderboard-box">
                    <h2>Leaderboard</h2>
                </div>
            </div>
            <div className="mainmenu-image right">
                <button className="signin-button">Sign In</button>
                <img src="https://via.placeholder.com/300x600" alt="Right" />
            </div>
        </div>
    );
};

export default MainMenu;
