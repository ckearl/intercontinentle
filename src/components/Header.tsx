/* Header.tsx */
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
      <header className="d-flex justify-content-around align-items-center mt-5 mb-3 syne-header">
        <div className="d-flex flex-column">
          <button id="color-setting" onClick={handleDarkModeClick} className="setting-button">
            Dark Mode
          </button>
          <button onClick={handleMapInputMode} className="setting-button">
            Map Input Mode
          </button>
          <button onClick={handleShowCountryList} className="setting-button">
            Show Country List
          </button>
        </div>
        <h1 className="" style={{ color: "#133c55", fontSize: "4.5rem" }}>
          intercontinentle
        </h1>
        <div className="header-spacer">Spacer</div>
      </header>
    </>
  );
}

export default Header;
