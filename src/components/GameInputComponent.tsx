import React, { useCallback, useEffect, useRef, useState } from "react";
import "./GameInputComponent.css";
import { TClue, TCountries, TCountryData, TGuess } from "types/Country";
import CountryJsonData from "data/countryData.json";
import Map from "./Map/Map";
import { ToolTips } from "data/tooltips";
import CountryModal from "./CountryModal/CountryModal";
import { Transition } from "react-transition-group";
import Tooltip from "./Tooltip";

const CountryData: TCountries = CountryJsonData;

function CleanForComparison(str: string): string {
  return str.replaceAll("_", " ").toLowerCase().trim();
}

function ClueAlreadyUsed(clueCategory: string, existingClues: TClue[]): boolean {
  return existingClues.some((existingClue) => existingClue.category === clueCategory);
}

function GetRandomClueCategory(countryData: TCountryData, existingClues: TClue[]): string {
  const randNumber = Math.floor(Math.random() * 999999);
  const allClueCategories = Object.keys(countryData).filter(
    (clue) =>
      !["Country", "Abbreviation", "Paragraph", "Landlocked", "ExportPartners"]
      .includes(clue)
  );
  const randClueCategory = allClueCategories[randNumber % allClueCategories.length];

  if (
    ClueAlreadyUsed(randClueCategory, existingClues) ||
    countryData[randClueCategory].value === ""
  ) {
    return GetRandomClueCategory(countryData, existingClues);
  }
  return randClueCategory;
}

function GetRandomClue(correctCountryData: TCountryData, existingClues: TClue[]): TClue {
  const randClueCategory = GetRandomClueCategory(correctCountryData, existingClues);
  const randClueFact = correctCountryData[randClueCategory];
  return {
    category: randClueCategory,
    fact: randClueFact.value,
  };
}

function GetInitialClues(correctCountryData: TCountryData): TClue[] {
  const newClues: TClue[] = [];
  const numclues = 3;
  for (let i = 0; i < numclues; i++) {
    newClues.push(GetRandomClue(correctCountryData, newClues));
  }
  return newClues;
}

function GetRandomCountry(allCountryAbbrs: string[]): TCountryData {
  const randValidIndex = Math.floor((Math.random() * 99999999) % allCountryAbbrs.length);
  const randCountryName = allCountryAbbrs[randValidIndex];
  return CountryData[randCountryName];
}

function GameInputComponent({ showMap }: { showMap: boolean }) {
  const maxGuesses = 10;
  const allCountryAbbrs = Object.keys(CountryData);
  const initialCountryData = GetRandomCountry(allCountryAbbrs);

  const [correctCountryData, setCorrectCountryData] = useState<TCountryData>(initialCountryData);
  const [clues, setClues] = useState<TClue[]>(GetInitialClues(initialCountryData));
  const [inputValue, setInputValue] = useState<string>("");
  const [userGuesses, setGuesses] = useState<TGuess[]>([]);

  const [isModalOpen, setIsModalOpen] = useState(false);

  function submitGuessHandler(guess: string | undefined, e?: React.FormEvent<HTMLFormElement>) {
    if (e) e.preventDefault();
    console.log("submitting guess: ", guess);

    let isCorrect = false;
    if (guess) {
      isCorrect =
        CleanForComparison(guess) === CleanForComparison(correctCountryData.Country.value);
    }
    const userGuess = { value: guess ?? "", isCorrect };

    if (isCorrect || userGuesses.length >= maxGuesses) {
      setIsModalOpen(true);
      return;
    }

    setClues([...clues, GetRandomClue(correctCountryData, clues)]);
    setGuesses([...userGuesses, userGuess]);
    setInputValue("");
  }

  const restartGame = useCallback(() => {
    const newCountryData = GetRandomCountry(allCountryAbbrs);
    setGuesses([]);
    setClues([]);
    setCorrectCountryData(newCountryData);
    setClues(GetInitialClues(newCountryData));
    setInputValue("");
  }, [allCountryAbbrs]);

  const closeModal = () => {
    setIsModalOpen(false);
  };

  const allCountryNames = Object.values(CountryData).map((country) => country.Country.value);

  const filteredCountryNames = allCountryNames.filter((country) =>
    country?.toLowerCase()?.includes(inputValue?.toLowerCase())
  );
  const showFilteredCountries = inputValue !== "";

  useEffect(() => {
    console.log(correctCountryData.Country.value);
  }, [correctCountryData]);

  const nodeRef = useRef(null);
  const mapCluesContainer = useRef(null);

  return (
    <div className="game-container">
      <div className="game-input-component" data-testid="game-input-component">
        <form onSubmit={(e) => submitGuessHandler(inputValue, e)} className="form">
          <div className="form-container">
            <div className="input-box-wrapper">
              <input
                type="text"
                placeholder="Enter country"
                className="country-input"
                value={inputValue}
                onChange={(e) => setInputValue(e.target.value)}
              />
              <div className="country-suggestion-container">
                {showFilteredCountries &&
                  filteredCountryNames.map((country, i) => {
                    if (i > 10) return null;
                    return (
                      <button
                        key={i}
                        type="button"
                        className="country-suggestion"
                        onClick={() => setInputValue(country)}
                      >
                        {country}
                      </button>
                    );
                  })}
              </div>
            </div>
            <div className="country-submit-button">
              <input className="guess-submit pointer" type="submit" value="make a guess"></input>
            </div>
          </div>
        </form>
        <div className="map-clues-container" ref={mapCluesContainer}>
          <Transition in={showMap} timeout={300} mountOnEnter unmountOnExit>
            {(state) => {
              const defaultStyle = {
                transition: `all 300ms ease-in-out`,
                overflow: "hidden",
                flex: 1,
              };

              const transitionStyles: any = {
                entering: { flex: 1 },
                entered: { flex: 1 },
                exiting: { flex: 0 },
                exited: { flex: 0 },
              };
              return (
                <div
                  ref={nodeRef}
                  style={{
                    ...defaultStyle,
                    ...transitionStyles[state],
                  }}
                >
                  <Map submitGuessHandler={submitGuessHandler} />
                </div>
              );
            }}
          </Transition>

          <div className="game-logic-container">
            <div className="clues-wrapper">
              <h3>Clues</h3>
              <hr style={{ width: "100%" }} />
              {clues.map((clue, i) => {
                const percentile = Math.round(
                  ((195 - Number(correctCountryData[clue.category].ranking)) / 195) * 100
                );
                const suffix =
                  percentile % 10 === 1
                    ? "st"
                    : percentile % 10 === 2
                      ? "nd"
                      : percentile % 10 === 3
                        ? "rd"
                        : "th";
                const ranking =
                  correctCountryData[clue.category].ranking !== "NA"
                    ? `This country is in the ${percentile}${suffix} percentile.`
                    : "";
                const toolTipText = `${ToolTips[clue.category].ToolTip} ${ranking}`;
                return (
                  <Tooltip key={i} text={toolTipText}>
                    <div className="clue">
                      <div className="clue-category">{ToolTips[clue.category].Clue}</div>
                      <div className="">{clue.fact}</div>
                    </div>
                  </Tooltip>
                );
              })}
            </div>
            <div className="guess-wrapper">
              <h3>Guesses</h3>
              <hr />

              {userGuesses.map((entry, i) => (
                <div className="clue row-reverse">
                  <div key={i} className=" right-align clue-category">
                    {entry.value}
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
      {isModalOpen && (
        <CountryModal
          correctCountryData={correctCountryData}
          closeModal={closeModal}
          restartGame={restartGame}
          isModalOpen={isModalOpen}
        />
      )}
    </div>
  );
}

export default GameInputComponent;

