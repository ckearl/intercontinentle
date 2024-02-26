import random
import communications_stats as comm_stats
import economy_stats as econ_stats
import energy_stats as ener_stats
import geography_stats as geo_stats
import government_stats as gov_stats
import people_and_society_stats as people_stats


ALL_STATS = ["total_area", "land_area", "water_area", "boundaries_distance", "random_border_country", "highest_elevation", "mean_elevation", "coastline_distance", "landlocked", "latitude", "longitude", "population", "most_popular_religion", "most_pop_language_outside_native_and_english", "median_age", "population_growth_rate", "birth_rate", "death_rate", "sex_ratio", "infant_mortality_rate", "life_expectancy_at_birth",
             "drinking_water_access_pct", "obesity", "literacy", "government_type", "GDP", "GDP_growth_rate", "GDP_per_capita", "labor_force", "unemployment_rate", "population_below_poverty_line", "total_exports", "export_partners", "export_commodities", "total_imports", "import_partners", "electricity_access", "mobile_phone_subscriptions", "internet_users_total", "internet_users_pct", "internet_country_code"]

def populate_countries_dict(countries, current_country, official_country_names, geography_stats_dict, people_and_society_stats_dict, government_stats_dict, economy_stats_dict, energy_stats_dict, communications_stats_dict):
	countries[current_country] = {
		"official_country_name": official_country_names[current_country],
		"total_area": geography_stats_dict["total_area"],
		"land_area": geography_stats_dict["land_area"],
		"water_area": geography_stats_dict["water_area"],
		"boundaries_distance": geography_stats_dict["boundaries_distance"],
		"random_border_country": geography_stats_dict["random_border_country"],
		"highest_elevation": geography_stats_dict["highest_elevation"],
		"mean_elevation": geography_stats_dict["mean_elevation"],
		"coastline_distance": geography_stats_dict["coastline_distance"],
		"landlocked": geography_stats_dict["landlocked"],
		"latitude": geography_stats_dict["latitude"],
		"longitude": geography_stats_dict["longitude"],
		"population": people_and_society_stats_dict["population"],
		"most_popular_religion": people_and_society_stats_dict["most_popular_religion"],
		"most_pop_language_outside_native_and_english": people_and_society_stats_dict["most_pop_language_outside_native_and_english"],
		"median_age": people_and_society_stats_dict["median_age"],
		"population_growth_rate": people_and_society_stats_dict["population_growth_rate"],
		"birth_rate": people_and_society_stats_dict["birth_rate"],
		"death_rate": people_and_society_stats_dict["death_rate"],
		"sex_ratio": people_and_society_stats_dict["sex_ratio"],
		"infant_mortality_rate": people_and_society_stats_dict["infant_mortality_rate"],
		"life_expectancy_at_birth": people_and_society_stats_dict["life_expectancy_at_birth"],
		"drinking_water_access_pct": people_and_society_stats_dict["drinking_water_access_pct"],
		"obesity": people_and_society_stats_dict["obesity"],
		"literacy": people_and_society_stats_dict["literacy"],
		"government_type": government_stats_dict["government_type"],
		"GDP": economy_stats_dict["GDP"],
		"GDP_growth_rate": economy_stats_dict["GDP_growth_rate"],
		"GDP_per_capita": economy_stats_dict["GDP_per_capita"],
		"labor_force": economy_stats_dict["labor_force"],
		"unemployment_rate": economy_stats_dict["unemployment_rate"],
		"population_below_poverty_line": economy_stats_dict["population_below_poverty_line"],
		"total_exports": economy_stats_dict["total_exports"],
		"export_partners": economy_stats_dict["export_partners"],
		"export_commodities": economy_stats_dict["export_commodities"],
		"total_imports": economy_stats_dict["total_imports"],
		"import_partners": economy_stats_dict["import_partners"],
		"electricity_access": energy_stats_dict["electricity_access"],
		"mobile_phone_subscriptions": communications_stats_dict["mobile_phone_subscriptions"],
		"internet_users_total": communications_stats_dict["internet_users_total"],
		"internet_users_pct": communications_stats_dict["internet_users_pct"],
		"internet_country_code": communications_stats_dict["internet_country_code"]
	}
	return countries
