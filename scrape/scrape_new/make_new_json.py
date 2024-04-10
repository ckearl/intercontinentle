import re
import json

clues_string = """
#### Administrative divisions - url: field/administrative-divisions/ - value: (";")[0] - comparitive_ranking: NA - category: geography - tooltip: This entry generally gives the numbers, designatory terms, and first-order administrative divisions as approved by the US Board on Geographic Names (BGN). - year_updated: NA - only_country_page_enabled: F
#### Male/Female population distribution - url: field/age-structure/ - value: combine three categories 0-14 years, 15-64 years, 65 years and over, by sex - comparitive_ranking: sort and rank - category: people and society - tooltip: This entry provides the distribution of the population between male and female. - year_updated: 2023 est. (found in the 65 years and over row) - only_country_page_enabled: F
#### Age distribution - url: field/age-structure/ - value: one string of three categories' percentages 0-14 years, 15-64 years, 65 years and over - comparitive_ranking: sort and rank the 15-64 years column - category: people and society - tooltip: This entry provides the distribution of the population according to age. Information is included by sex and age group as follows: 0-14 years (children), 15-64 years (working age), and 65 years and over (elderly) - year_updated: 2023 est. - only_country_page_enabled: F
#### Agricultural products - url: field/agricultural-products/ - value: make an array of strings, randomly select three - comparitive_ranking: NA - category: economy - tooltip: This entry provides a list of three of the country's ten most important agricultural products. - year_updated: NA - only_country_page_enabled: F
#### Airports, Number of  - url: field/airports/ - value: (";")[0] - comparitive_ranking: sort and rank - category: transportation - tooltip: This entry gives the total number of active airports or airfields and includes both civilian and military facilities. The runway(s) may be paved (concrete or asphalt surfaces) or unpaved (grass, earth, sand, or gravel surfaces) - year_updated: most are 2024 est., found in string - only_country_page_enabled: F
#### Area, Total - url: field/area/ - value: ("tal: ")[1] - comparitive_ranking: sort and rank - category: geography - tooltip: the sum of all land and water areas delimited by international boundaries and/or coastlines - year_updated: NA - only_country_page_enabled: F
#### Area, Land - url: field/area/ - value: ("and: ")[1] - comparitive_ranking: sort and rank - category: geography - tooltip: the aggregate of all surfaces delimited by international boundaries and/or coastlines, excluding inland water bodies (lakes, reservoirs, rivers) - year_updated: NA - only_country_page_enabled: F
#### Area, Water - url: field/area/ - value: ("ater: ")[1] - comparitive_ranking: sort and rank - category: geography - tooltip: the sum of the surfaces of all inland water bodies, such as lakes, reservoirs, or rivers, as delimited by international boundaries and/or coastlines. - year_updated: NA - only_country_page_enabled: F
#### Area, Comparative - url: field/area-comparative/ - value: full string - comparitive_ranking: NA - category: geography - tooltip: an area comparison based on total area equivalents. Most entities are compared with the entire US or one of the 50 states based on area measurements (1990 revised) provided by the US Bureau of the Census. The smaller entities are compared with Washington, DC (178 sq km, 69 sq mi) or The Mall in Washington, DC (0.59 sq km, 0.23 sq mi, 146 acres). - year_updated: NA - only_country_page_enabled: F
#### Birth rate - url: field/birth-rate/ - value: (" (2023")[1] full, includes (2023 est.) - comparitive_ranking: sort and rank - category: people and society - tooltip: This entry gives the average annual number of births during a year per 1,000 persons in the population at midyear; also known as crude birth rate. - year_updated: most 2023 est., check string - only_country_page_enabled: F
#### Budget, Revenues - url: field/budget/ - value: ("enues: ")[1], (" (")[0] - comparitive_ranking: sort and rank - category: economy - tooltip: This entry records total revenues received by the national government. The difference between revenues and expenditures is the budget balance. Sources of revenues are taxes, fees, and social contributions related to a specific government's activities. Revenues from the federal government are the individual and corporate income tax, Social Security contributions, excise taxes, and grants. State and local government revenues come from income, sales, and property taxes and various fees. - year_updated: (" (")[0][1:5] - only_country_page_enabled: F
#### Budget, Expenditures - url: field/budget/ - value: ("enditures: ")[1], (" (")[0] - comparitive_ranking: sort and rank - category: economy - tooltip: This entry records total spending on national environmental protection, education, health, public order and safety, and other social services, as well as the amount of additional spending on national defense. About two-thirds of the budget is funded by the sale of oil and natural gas. A series of massive government spending increases in 2011 and 2012 led to the growth of the budget deficit, which peaked at 16% of GDP in 2012. The government has largely scaled back public spending in the face of falling oil prices, but it has not reduced the budget deficit by a significant amount. - year_updated: (" (")[0][1:5] - only_country_page_enabled: F
#### Capital, Name - url: field/capital/ - value: ("ame: ")[1] - comparitive_ranking: NA - category: geography - tooltip: the name of the seat of government - year_updated: NA - only_country_page_enabled: F
#### Capital, Geographic Coordinates - url: field/capital/ - value: ("ates: ")[1] - comparitive_ranking: NA - category: geography - tooltip: the geographic coordinates that define the center of the country - year_updated: NA - only_country_page_enabled: F
#### Capital, Time Difference - url: field/capital/ - value: ("nce: ")[1] - comparitive_ranking: NA - category: geography - tooltip: the difference between Coordinated Universal Time (UTC) and the time observed in the capital - year_updated: NA - only_country_page_enabled: F
#### Carbon Dioxide emissions - url: field/carbon-dioxide-emissions/ - value: ("ions: ")[1] - comparitive_ranking: sort and rank - category: environment - tooltip: This entry is the total amount of carbon dioxide, measured in metric tons, released by burning fossil fuels in the process of producing and consuming energy. - year_updated: .split("(")[1:5] - only_country_page_enabled: F
#### Citizenship, By Birth - url: field/citizenship/ - value: ("irth: ")[1] - comparitive_ranking: NA - category: people and society - tooltip: This entry provides information related to the acquisition and exercise of citizenship; it includes four subfields: citizenship by birth describes the acquisition of citizenship based on place of birth, known as Jus soli, regardless of the citizenship of parents. - year_updated: NA - only_country_page_enabled: T
#### Citizenship, By Descent - url: field/citizenship/ - value: ("escent only: ")[1] - comparitive_ranking: NA - category: people and society - tooltip: This entry provides information related to the acquisition and exercise of citizenship; it includes four subfields: citizenship by descent describes the acquisition of citizenship based on the principle of Jus sanguinis, or by descent, where at least one parent is a citizen of the state and being born within the territorial limits of the state is not required. - year_updated: NA - only_country_page_enabled: T
#### Citizenship, Dual - url: field/citizenship/ - value: ("dual: ")[1] - comparitive_ranking: NA - category: people and society - tooltip: This entry provides information related to the acquisition and exercise of citizenship; it includes four subfields: dual citizenship recognizes the voluntary acquisition of citizenship and is enforced by the state, no matter where the person is located. - year_updated: NA - only_country_page_enabled: T
#### Climate - url: field/climate/ - value: just the string - comparitive_ranking: NA - category: geography - tooltip: This entry includes a brief description of typical weather regimes throughout the year. - year_updated: NA - only_country_page_enabled: F
#### Coastline - url: field/coastline/ - value: just the string - comparitive_ranking: sort and rank - category: geography - tooltip: This entry gives the total length of the boundary between the land area (including islands) and the sea. - year_updated: NA - only_country_page_enabled: F
#### Constitution - url: field/constitution/ - value: ("istory: ")[1] - comparitive_ranking: NA - category: government - tooltip: This entry provides information on a country's constitution and includes two subfields. The history subfield includes the dates of previous constitutions and the main steps and dates in formulating and implementing the latest constitution. For countries with 1-3 previous constitutions, the years are listed; for those with 4-9 previous, the entry is listed as "several previous," and for those with 10 or more, the entry is "many previous." The amendments subfield summarizes the process of amending a country's constitution, including the dates of the amendments and the main steps in the process. - year_updated: NA - only_country_page_enabled: T
#### Credit Ratings - url: field/credit-ratings/ - value: ("oors rating: ")[1] - comparitive_ranking: NA - category: economy - tooltip: This entry provides the current bond ratings for a country or territory from the three major credit bureau Standard & Poors. The year is the year that the rating was first obtained. - year_updated: ("(")[1:5] - only_country_page_enabled: F
#### Current Health Expenditure - url: field/current-health-expenditure/ - value: just the string - comparitive_ranking: sort and rank - category: health - tooltip: Current health expenditure (CHE) describes the share of spending on health in each country relative to the size of its economy. - year_updated: ("(")[1:5] - only_country_page_enabled: T
#### Death Rate - url: field/death-rate/ - value: (" (2023")[1] full, includes (2023 est.) - comparitive_ranking: sort and rank - category: people and society - tooltip: This entry gives the average annual number of deaths during a year per 1,000 population at midyear; also known as crude death rate. - year_updated: most 2023 est., check string - only_country_page_enabled: F
#### Debt, External - url: field/debt-external/ - value: (" (2023")[1] full, includes (2023 est.) - comparitive_ranking: sort and rank - category: economy - tooltip: This entry gives the total public and private debt owed to nonresidents repayable in internationally accepted currencies, goods, or services. These figures are calculated on an exchange rate basis, i.e., not in purchasing power parity (PPP) terms. - year_updated: most 2023 est., check string - only_country_page_enabled: F
#### Drinking water source - url: field/drinking-water-source/ - value: ("ed: urban: ")[1] - comparitive_ranking: sort and rank - category: people and society - tooltip: This entry provides information about access to improved or unimproved drinking water sources available to segments of the population of a country. - year_updated: grab from total row, ("(")[1:5] - only_country_page_enabled: F
#### Electricity, Consumption - url: field/electricity/ - value: ("ption: ")[1] - comparitive_ranking: sort and rank - category: energy - tooltip: This entry consists of total electricity generated annually plus imports and minus exports, expressed in kilowatt-hours. The discrepancy between the amount of electricity generated and/or imported and the amount consumed and/or exported is accounted for as loss in transmission and distribution. - year_updated: ("(")[1:5] - only_country_page_enabled: F
#### Electricity, Access - url: field/electricity-access/ - value: ("otal population: ")[1] - comparitive_ranking: sort and rank - category: energy - tooltip: This entry provides information on access to electricity for the entire country. - year_updated: ("(")[1:5] - only_country_page_enabled: F
#### Elevation, Highest Point - url: field/elevation/ - value: ("hest point: ")[1] - comparitive_ranking: sort and rank - category: geography - tooltip: This entry includes is the highest point of elevation in the country. - year_updated: NA - only_country_page_enabled: F
#### Elevation, Lowest Point - url: field/elevation/ - value: ("west point: ")[1] - comparitive_ranking: sort and rank - category: geography - tooltip: This entry includes is the lowest point of elevation in the country. - year_updated: NA - only_country_page_enabled: F
#### Elevation, Mean - url: field/elevation/ - value: ("an elevation: ")[1] - comparitive_ranking: sort and rank - category: geography - tooltip: This entry includes the mean elevation of the entire countries landscape. - year_updated: NA - only_country_page_enabled: F
#### Environment - international agreements - url: field/environment-international-agreements/ - value: ("rty to: ")[1] - comparitive_ranking: NA - category: environment - tooltip: This entry lists the most important national environmental agreements, international environmental issues, and the international agreements in which the country is involved. - year_updated: NA - only_country_page_enabled: T
#### Ethic Groups - url: field/ethnic-groups/ - value: just the string - comparitive_ranking: NA - category: people and society - tooltip: This entry provides an ordered listing of ethnic groups starting with the largest and normally includes the percent of total population. - year_updated: NA - only_country_page_enabled: T
#### Executive branch - url: field/executive-branch/ - value: ("f of state: ")[1] - comparitive_ranking: NA - category: government - tooltip: This entry includes the name, title, and beginning date in office of the titular leader of the country who represents the state at official and ceremonial functions but may not be involved with the day-to-day activities of the government. - year_updated: NA - only_country_page_enabled: T
#### Exchange rates - url: field/exchange-rates/ - value: a list of five strings, delimmited by "<br>" - comparitive_ranking: NA - category: economy - tooltip: This entry provides the average annual price of a country's monetary unit in terms of the US dollar. - year_updated: NA - only_country_page_enabled: F
#### Exports - url: field/exports/ - value: just the string, first entry in list of three - comparitive_ranking: sort and rank - category: economy - tooltip: This entry provides the total US dollar amount of merchandise exports on an f.o.b. (free on board) basis. These figures are calculated on an exchange rate basis, i.e., not in purchasing power parity (PPP) terms. - year_updated: ("(")[1:5] - only_country_page_enabled: F
#### Exports - commodities - url: field/exports-commodities/ - value: make an array of strings, randomly select three, delimmited by ", " - comparitive_ranking: NA - category: economy - tooltip: This entry provides a listing of the highest-valued exported products; it sometimes includes the percent of total dollar value. - year_updated: ("(")[1:5] - only_country_page_enabled: F
#### Exports - partners - url: field/exports-partners/ - value: make an array of strings, select first three, delimmited by ", " - comparitive_ranking: NA - category: economy - tooltip: This entry provides a rank ordering of trading partners starting with the most important; it sometimes includes the percent of total dollar value. - year_updated: ("(")[1:5] - only_country_page_enabled: F
#### GDP - url: field/gdp-official-exchange-rate/ - value: just the string - comparitive_ranking: sort and rank - category: economy - tooltip: This entry gives the gross domestic product (GDP) or value of all final goods and services produced within a nation in a given year. A nation's GDP at purchasing power parity (PPP) exchange rates is the sum value of all goods and services produced in the country valued at prices prevailing in the United States in the year noted. - year_updated: ("(")[1:5] - only_country_page_enabled: F
#### Geographic Coordinates, Latitude - url: field/geographic-coordinates/ - value: (", ")[0] - comparitive_ranking: NA - category: geography - tooltip: This entry includes the latitude and longitude of the country's geographic center in decimal degrees. - year_updated: NA - only_country_page_enabled: F
#### Geographic Coordinates, Longitude - url: field/geographic-coordinates/ - value: (", ")[1] - comparitive_ranking: NA - category: geography - tooltip: This entry includes the latitude and longitude of the country's geographic center in decimal degrees. - year_updated: NA - only_country_page_enabled: F
"""

clues = re.split(r'(?=####)', clues_string.strip())

countries = ['Afghanistan', 'Akrotiri', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antarctica', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Ashmore and Cartier Islands', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas, The', 'Bahrain', 'Baker Island', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Bouvet Island', 'Brazil', 'British Indian Ocean Territory', 'British Virgin Islands', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burma', 'Burundi', 'Cabo Verde', 'Cambodia', 'Cameroon', 'Canada', 'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Christmas Island', 'Clipperton Island', 'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo, Democratic Republic of the', 'Congo, Republic of the', 'Cook Islands', 'Coral Sea Islands', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Curacao', 'Cyprus', 'Czechia', 'Denmark', 'Dhekelia', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Falkland Islands (Islas Malvinas)', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Polynesia', 'French Southern and Antarctic Lands', 'Gabon', 'Gambia, The', 'Gaza Strip', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Heard Island and McDonald Islands', 'Holy See (Vatican City)', 'Honduras', 'Hong Kong', 'Howland Island', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Jan Mayen', 'Japan', 'Jarvis Island', 'Jersey', 'Johnston Atoll', 'Jordan', 'Kazakhstan', 'Kenya', 'Kingman Reef', 'Kiribati', 'Korea, North', 'Korea, South', 'Kosovo',
 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macau', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', 'Mexico', 'Micronesia, Federated States of', 'Midway Islands', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique', 'Namibia', 'Nauru', 'Navassa Island', 'Nepal', 'Netherlands', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Island', 'North Macedonia', 'Northern Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palmyra Atoll', 'Panama', 'Papua New Guinea', 'Paracel Islands', 'Paraguay', 'Peru', 'Philippines', 'Pitcairn Islands', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Romania', 'Russia', 'Rwanda', 'Saint Barthelemy', 'Saint Helena, Ascension, and Tristan da Cunha', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Martin', 'Saint Pierre and Miquelon', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Georgia and South Sandwich Islands', 'South Sudan', 'Spain', 'Spratly Islands', 'Sri Lanka', 'Sudan', 'Suriname', 'Svalbard', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Timor-Leste', 'Togo', 'Tokelau', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey (Turkiye)', 'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela', 'Vietnam', 'Virgin Islands', 'Wake Island', 'Wallis and Futuna', 'West Bank', 'World', 'Yemen', 'Zambia', 'Zimbabwe']
# print(clues)
countries_data = {}
category_data = {}

for country in countries:
  countries_data[country] = {}
  for clue in clues:
    clue_name = clue.split((" - "))[0].strip('#').strip()
    countries_data[country][clue_name] = {}
    lines = clue.split(' - ')[1:-1]
    
    for line in lines[1:]:
      category_data = {}
      # print(line)
      key, value = line.split(': ', 1)
      category_data[key.strip()] = value.strip()
    
    countries_data[country][clue_name] = category_data

print(json.dumps(countries_data, indent=2))

# write out json to .json file
with open('countries_data.json', 'w') as f:
  json.dump(countries_data, f, indent=2)