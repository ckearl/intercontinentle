/**
 * Christopher Kearl
 */
import React from "react";
import setColorScheme from "utils/setColorScheme";

type THeaderProps = {
  showMap: boolean;
  setShowMap: (showMap: boolean) => void;
  setShowCountryList: (showCountryList: boolean) => void;
  showCountryList: boolean;
};

function Header({ showMap, setShowMap, setShowCountryList, showCountryList }: THeaderProps) {
  function handleDarkModeClick() {
    setColorScheme();
  }

  function handleMapInputMode() {
    setShowMap(!showMap);
  }

  function handleShowCountryList() {
    setShowCountryList(!showCountryList);
  }
  return (
    <>
      <header className="App-header saira">
        <div className="app-settings">
          <button id="color-setting" onClick={handleDarkModeClick} className="setting-button">
            Dark Mode
          </button>
          <button onClick={handleMapInputMode} className="setting-button">
            Toggle Map Mode
          </button>
          <button onClick={handleShowCountryList} className="setting-button">
            Show Country List
          </button>
        </div>
        <div>
          <h1>intercontinentle</h1>
          <div style={{ textAlign: "center" }}>How well do you know your neighbors?</div>
        </div>

        <div className="header-spacer">Spacer</div>
      </header>
    </>
  );
}

export default Header;
