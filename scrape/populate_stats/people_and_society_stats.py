
def people_and_society_stats(people_and_society_div):
	try:
		population = people_and_society_div.find("a", string="Population").parent.parent.find("p").text.split(" (")[0]
	except:
		population = None

	try:
		most_popular_religion = people_and_society_div.find("a", string="Religions").parent.parent.find("p").text.split(", ")[0]
	except:
		most_popular_religion = None

	try:
		languages = people_and_society_div.find("a", string="Languages").parent.parent.find("p").text.split(", ")
		for lang in languages:
			if "(official)" in lang:
				languages.remove(lang)
			languages = languages.remove('English')
			most_pop_language_outside_native_and_english = languages[0]
			if "major" in most_pop_language_outside_native_and_english:
				most_pop_language_outside_native_and_english = most_pop_language_outside_native_and_english.split("major")[0]

	except:
		most_pop_language_outside_native_and_english = None

	try:
		median_age = people_and_society_div.find("a", string="Median age").parent.parent.find("strong").parent.text.split("total: ")[1].split("male:")[0]
	except:
		median_age = None

	try:
		population_growth_rate = people_and_society_div.find("a", string="Population growth rate").parent.parent.find("p").text.split(" (")[0]
	except:
		population_growth_rate = None

	try:
		birth_rate = people_and_society_div.find("a", string="Birth rate").parent.parent.find("p").text.split(" (")[0]
		if birth_rate == 'NA':
			birth_rate = None
	except:
		birth_rate = None

	try:
		death_rate = people_and_society_div.find("a", string="Death rate").parent.parent.find("p").text.split(" (")[0]
		if death_rate == 'NA':
			death_rate = None
	except:
		death_rate = None

	try:
		sex_ratio = people_and_society_div.find("a", string="Sex ratio").parent.parent.find("strong").parent.text.split("total population: ")[1].split(" (")[0]
		if sex_ratio == 'NA':
			sex_ratio = None
	except:
		sex_ratio = None

	try:
		infant_mortality_rate = people_and_society_div.find("a", string="Infant mortality rate").parent.parent.find("strong").parent.text.split("total: ")[1].split("male:")[0]
		if infant_mortality_rate == 'NA':
			infant_mortality_rate = None
	except:
		infant_mortality_rate = None

	try:
		life_expectancy_at_birth = people_and_society_div.find("a", string="Life expectancy at birth").parent.parent.find("strong").parent.text.split("total population: ")[1].split("male:")[0]
		if life_expectancy_at_birth == 'NA':
			life_expectancy_at_birth = None
	except:
		life_expectancy_at_birth = None

	try:
		drinking_water_access_pct = people_and_society_div.find("a", string="Drinking water source").parent.parent.find("strong").parent.text.split("urban: ")[1].split(" of population")[0]
		if "NAtotal:" in drinking_water_access_pct:
			if drinking_water_access_pct.split("NAtotal: ")[1] == 'NAunimproved: ':
				drinking_water_access_pct = None
			else:
				drinking_water_access_pct = drinking_water_access_pct.split("NAtotal: ")[1]
	except:
		drinking_water_access_pct = None

	try:
		obesity = people_and_society_div.find("a", string="Obesity - adult prevalence rate").parent.parent.find("p").text.split(" (")[0]
	except:
		obesity = None

	try:
		literacy = people_and_society_div.find("a", string="Literacy").parent.parent.find("strong").parent.text.split("total population: ")[1].split("male")[0]
		if literacy == 'NA':
			literacy = None
	except:
		literacy = None

	people_and_society_stats_dict = {
		"population": population,
		"most_popular_religion": most_popular_religion,
		"most_pop_language_outside_native_and_english": most_pop_language_outside_native_and_english,
		"median_age": median_age,
		"population_growth_rate": population_growth_rate,
		"birth_rate": birth_rate,
		"death_rate": death_rate,
		"sex_ratio": sex_ratio,
		"infant_mortality_rate": infant_mortality_rate,
		"life_expectancy_at_birth": life_expectancy_at_birth,
		"drinking_water_access_pct": drinking_water_access_pct,
		"obesity": obesity,
		"literacy": literacy
	}
	return people_and_society_stats_dict
