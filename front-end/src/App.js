import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import MainMenuPage from './pages/MainMenuPage';

const App = () => {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<MainMenuPage />} />
            </Routes>
        </Router>
    );
};

export default App;
