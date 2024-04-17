/**
 * cowritten component
 */
import React, { useState } from "react";
import "components/App.css";
import Header from "components/Header";
import GameInputComponent from "components/GameInputComponent";
import CountryList from "./CountryList";

function App() {
  const [showMap, setShowMap] = useState(true);
  const [showCountryList, setShowCountryList] = useState(false);
  return (
    <div className="container-fluid d-flex ">
      <div className="w-100">
        <CountryList showCountryList={showCountryList} />
        <Header
          showMap={showMap}
          setShowMap={setShowMap}
          setShowCountryList={setShowCountryList}
          showCountryList={showCountryList}
        />
        <GameInputComponent showMap={showMap} />
      </div>
    </div>
  );
}

export default App;
