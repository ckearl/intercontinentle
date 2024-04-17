import React from "react";

export default function CountryList({ showCountryList }: { showCountryList: boolean }) {
  return <div>{showCountryList && <div>CountryList</div>}</div>;
}
