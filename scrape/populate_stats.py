import random

ALL_STATS = ["total_area", "land_area", "water_area", "boundaries_distance", "random_border_country", "highest_elevation", "mean_elevation", "coastline_distance", "landlocked", "latitude", "longitude", "population", "most_popular_religion", "most_pop_language_outside_native_and_english", "median_age", "population_growth_rate", "birth_rate", "death_rate", "sex_ratio", "infant_mortality_rate", "life_expectancy_at_birth",
             "drinking_water_access_pct", "obesity", "literacy", "government_type", "GDP", "GDP_growth_rate", "GDP_per_capita", "labor_force", "unemployment_rate", "population_below_poverty_line", "total_exports", "export_partners", "export_commodities", "total_imports", "import_partners", "electricity_access", "mobile_phone_subscriptions", "internet_users_total", "internet_users_pct", "internet_country_code"]


def geography_stats(geography_div):
    total_area, land_area, water_area = find_total_land_water_area(
        geography_div)
    boundaries_distance, random_border_country = boundary_distance_and_random_border_country(
        geography_div)
    highest_elevation, mean_elevation = highest_and_mean_elevation(
        geography_div)
    coastline_distance, landlocked = coastline(geography_div)
    latitude, longitude = geographic_coordinates(geography_div)
    geography_stats_dict = {
        "total_area": total_area,
        "land_area": land_area,
        "water_area": water_area,
        "boundaries_distance": boundaries_distance,
        "random_border_country": random_border_country,
        "highest_elevation": highest_elevation,
        "mean_elevation": mean_elevation,
        "coastline_distance": coastline_distance,
        "landlocked": landlocked,
        "latitude": latitude,
        "longitude": longitude
    }
    return geography_stats_dict


def find_total_land_water_area(geography_div):
    try:
        print(geography_div.find("a", string="Area").parent.parent)
        area_div = geography_div.find("a", string="Area").parent.parent
    except:
        area_div = None

    try:
        area_text = area_div.find("strong", string="total:").parent.text
    except:
        area_text = None

    try:
        total_area = area_text.split("total: ")[1].split("land")[0]
    except:
        total_area = None
    try:
        if "note" in total_area:
            total_area = total_area.split("note")[0]
        elif " (" in total_area:
            total_area = total_area.split(" (")[0]
    except:
        pass

    try:
        land_area = area_text.split("kmland: ")[1].split("water")[0]
    except:
        land_area = None
    try:
        if "note" in land_area:
            land_area = land_area.split("note")[0]
        elif " (" in land_area:
            land_area = land_area.split(" (")[0]
    except:
        pass

    try:
        water_area = area_text.split("kmwater: ")[1]
    except:
        water_area = None
    try:
        if "note" in water_area:
            water_area = water_area.split("note")[0]
    except:
        pass
    return total_area, land_area, water_area


def boundary_distance_and_random_border_country(geography_div):
    try:
        boundaries_distance_div = geography_div.find(
            "a", string="Land boundaries").parent.parent.find("strong", string="total:").parent.text
    except:
        boundaries_distance_div = None

    try:
        boundaries_distance = boundaries_distance_div.split("total: ")[
            1].split("border")[0]
    except:
        boundaries_distance = None
    try:
        if "note" in boundaries_distance:
            boundaries_distance = boundaries_distance.split("note")[0]
        elif "regional" in boundaries_distance:
            boundaries_distance = boundaries_distance.split("regional")[0]
    except:
        pass

    try:
        random_border_country = random.choice(boundaries_distance_div.split(
            "border countries (")[1].split("): ")[1].split("; "))
    except:
        random_border_country = None
    try:
        if "note" in random_border_country:
            random_border_country = random_border_country.split("note")[0]
    except:
        pass

    return boundaries_distance, random_border_country


def highest_and_mean_elevation(geography_div):
    try:
        elevation_div = geography_div.find(
            "a", string="Elevation").parent.parent
    except:
        elevation_div = None

    try:
        highest_elevation = elevation_div.find(
            "strong", string="highest point:").parent.text.split("lowest")[0]
    except:
        highest_elevation = None

    try:
        highest_elevation = highest_elevation[-10:].split(" ")[1] + " m"
    except:
        highest_elevation = None

    try:
        mean_elevation = elevation_div.find(
            "strong", string="mean elevation:").parent.text.split("mean elevation: ")[1]
    except:
        mean_elevation = None
    try:
        if "note" in mean_elevation:
            mean_elevation = mean_elevation.split("note")[0]
        elif "top" in mean_elevation:
            mean_elevation = mean_elevation.split("top")[0]
    except:
        pass

    return highest_elevation, mean_elevation


def coastline(geography_div):
    try:
        coastline_div = geography_div.find(
            "a", string="Coastline").parent.parent
    except:
        coastline_div = None

    try:
        coastline_distance = coastline_div.find("p").text
    except:
        coastline_distance = None

    try:
        if "landlocked" in coastline_distance:
            coastline_distance = coastline_distance.split(" (landlocked")[0]
            landlocked = True
        elif "note" in coastline_distance:
            coastline_distance = coastline_distance.split("note")[0]
        elif "metropolitan" in coastline_distance:
            coastline_distance = coastline_distance.split("metropolitan")[0]
        elif "metropolitan" in coastline_distance:
            coastline_distance = coastline_distance.split("metropolitan")[0]
        elif " (" in coastline_distance:
            coastline_distance = coastline_distance.split(" (")[0]
        elif ("Saint Helena" in coastline_distance) or ("Baker Island" in coastline_distance):
            coastline_distance = None
    except:
        pass

    try:
        if "0 km" in coastline_distance:
            landlocked = True
        else:
            landlocked = False
    except:
        landlocked = None

    return coastline_distance, landlocked


def geographic_coordinates(geography_div):
    try:
        geographic_coordinates = geography_div.find(
            "a", string="Geographic coordinates").parent.parent.find("p").text
    except:
        geographic_coordinates = None

    try:
        latitude = geographic_coordinates.split(", ")[0]
        if ("metropolitan" in latitude) or ("Amsterdam" in latitude) or ("Saint Helena" in latitude) or ("Baker Island" in latitude):
            latitude = latitude.split(": ")[1]
    except:
        latitude = None

    try:
        longitude = geographic_coordinates.split(", ")[1]
        if ";" in longitude:
            longitude = longitude.split(";")[0]
        elif "note" in longitude:
            longitude = longitude.split("note")[0]
    except:
        longitude = None

    return latitude, longitude


def people_and_society_stats(people_and_society_div):
    try:
        population = people_and_society_div.find(
            "a", string="Population").parent.parent.find("p").text.split(" (")[0]
    except:
        population = None

    try:
        most_popular_religion = people_and_society_div.find(
            "a", string="Religions").parent.parent.find("p").text.split(", ")[0]
    except:
        most_popular_religion = None

    try:
        languages = people_and_society_div.find(
            "a", string="Languages").parent.parent.find("p").text.split(", ")
        for lang in languages:
            if "(official)" in lang:
                languages.remove(lang)
        languages = languages.remove('English')
        most_pop_language_outside_native_and_english = languages[0]
        if "major" in most_pop_language_outside_native_and_english:
            most_pop_language_outside_native_and_english = most_pop_language_outside_native_and_english.split("major")[
                0]

    except:
        most_pop_language_outside_native_and_english = None

    try:
        median_age = people_and_society_div.find("a", string="Median age").parent.parent.find(
            "strong").parent.text.split("total: ")[1].split("male:")[0]
    except:
        median_age = None

    try:
        population_growth_rate = people_and_society_div.find(
            "a", string="Population growth rate").parent.parent.find("p").text.split(" (")[0]
    except:
        population_growth_rate = None

    try:
        birth_rate = people_and_society_div.find(
            "a", string="Birth rate").parent.parent.find("p").text.split(" (")[0]
        if birth_rate == 'NA':
            birth_rate = None
    except:
        birth_rate = None

    try:
        death_rate = people_and_society_div.find(
            "a", string="Death rate").parent.parent.find("p").text.split(" (")[0]
        if death_rate == 'NA':
            death_rate = None
    except:
        death_rate = None

    try:
        sex_ratio = people_and_society_div.find("a", string="Sex ratio").parent.parent.find(
            "strong").parent.text.split("total population: ")[1].split(" (")[0]
        if sex_ratio == 'NA':
            sex_ratio = None
    except:
        sex_ratio = None

    try:
        infant_mortality_rate = people_and_society_div.find("a", string="Infant mortality rate").parent.parent.find(
            "strong").parent.text.split("total: ")[1].split("male:")[0]
        if infant_mortality_rate == 'NA':
            infant_mortality_rate = None
    except:
        infant_mortality_rate = None

    try:
        life_expectancy_at_birth = people_and_society_div.find("a", string="Life expectancy at birth").parent.parent.find(
            "strong").parent.text.split("total population: ")[1].split("male:")[0]
        if life_expectancy_at_birth == 'NA':
            life_expectancy_at_birth = None
    except:
        life_expectancy_at_birth = None

    try:
        drinking_water_access_pct = people_and_society_div.find("a", string="Drinking water source").parent.parent.find(
            "strong").parent.text.split("urban: ")[1].split(" of population")[0]
        if "NAtotal:" in drinking_water_access_pct:
            if drinking_water_access_pct.split("NAtotal: ")[1] == 'NAunimproved: ':
                drinking_water_access_pct = None
            else:
                drinking_water_access_pct = drinking_water_access_pct.split("NAtotal: ")[
                    1]
    except:
        drinking_water_access_pct = None

    try:
        obesity = people_and_society_div.find(
            "a", string="Obesity - adult prevalence rate").parent.parent.find("p").text.split(" (")[0]
    except:
        obesity = None

    try:
        literacy = people_and_society_div.find("a", string="Literacy").parent.parent.find(
            "strong").parent.text.split("total population: ")[1].split("male")[0]
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


def government_stats(government_div):
    try:
        government_type = government_div.find(
            "a", string="Government type").parent.parent.find("p").text
    except:
        government_type = None

    government_stats_dict = {
        "government_type": government_type
    }
    return government_stats_dict


def economy_stats(economy_div):
    try:
        GDP = economy_div.find("a", string="Real GDP (purchasing power parity)").parent.parent.find(
            "p").text.split(" (")[0]
    except:
        GDP = None

    try:
        GDP_growth_rate = economy_div.find(
            "a", string="Real GDP growth rate").parent.parent.find("p").text.split(" (")[0]
    except:
        GDP_growth_rate = None

    try:
        GDP_per_capita = economy_div.find(
            "a", string="Real GDP per capita").parent.parent.find("p").text.split(" (")[0]
    except:
        GDP_per_capita = None

    try:
        labor_force = economy_div.find(
            "a", string="Labor force").parent.parent.find("p").text.split(" (")[0]
    except:
        labor_force = None

    try:
        unemployment_rate = economy_div.find(
            "a", string="Unemployment rate").parent.parent.find("p").text.split(" (")[0]
    except:
        unemployment_rate = None

    try:
        population_below_poverty_line = economy_div.find(
            "a", string="Population below poverty line").parent.parent.find("p").text.split(" (")[0]
    except:
        population_below_poverty_line = None

    try:
        total_exports = economy_div.find(
            "a", string="Exports").parent.parent.find("p").text.split(" (")[0]
    except:
        total_exports = None

    try:
        export_partners = economy_div.find(
            "a", string="Exports - partners").parent.parent.find("p").text.split(" (")[0].split(", ")[:3]
    except:
        export_partners = None

    try:
        export_commodities = economy_div.find(
            "a", string="Exports - commodities").parent.parent.find("p").text.split(" (")[0].split(", ")[:3]
    except:
        export_commodities = None

    try:
        total_imports = economy_div.find(
            "a", string="Imports").parent.parent.find("p").text.split(" (")[0]
    except:
        total_imports = None

    try:
        import_partners = economy_div.find(
            "a", string="Imports - partners").parent.parent.find("p").text.split(" (")[0].split(", ")[:3]
    except:
        import_partners = None

    economy_stats_dict = {
        "GDP": GDP,
        "GDP_growth_rate": GDP_growth_rate,
        "GDP_per_capita": GDP_per_capita,
        "labor_force": labor_force,
        "unemployment_rate": unemployment_rate,
        "population_below_poverty_line": population_below_poverty_line,
        "total_exports": total_exports,
        "export_partners": export_partners,
        "export_commodities": export_commodities,
        "total_imports": total_imports,
        "import_partners": import_partners
    }
    return economy_stats_dict


def energy_stats(energy_div):
    try:
        electricity_access = energy_div.find("a", string="Electricity access").parent.parent.find(
            "strong").parent.text.split("population: ")[1].split(" (")[0]
    except:
        electricity_access = None
    energy_stats_dict = {
        "electricity_access": electricity_access
    }
    return energy_stats_dict


def communications_stats(communications_div):
    try:
        mobile_phone_subscriptions = communications_div.find(
            "a", string="Telephones - mobile cellular").parent.parent.find("p").text.split("subscriptions: ")[1].split(" (")[0]
    except:
        mobile_phone_subscriptions = None

    try:
        internet_users_div = communications_div.find(
            "a", string="Internet users").parent.parent
    except:
        internet_users_div = None

    try:
        internet_users_total = internet_users_div.find(
            "p").text.split("total: ")[1].split(" (")[0]
        if "note" in internet_users_total:
            internet_users_total = internet_users_total.split("note")[0]
    except:
        internet_users_total = None

    try:
        internet_users_pct = internet_users_div.find(
            "p").text.split("population: ")[1].split(" (")[0]
    except:
        internet_users_pct = None

    try:
        internet_country_code = communications_div.find(
            "a", string="Internet country code").parent.parent.find("p").text
    except:
        internet_country_code = None

    communications_stats_dict = {
        "mobile_phone_subscriptions": mobile_phone_subscriptions,
        "internet_users_total": internet_users_total,
        "internet_users_pct": internet_users_pct,
        "internet_country_code": internet_country_code
    }
    return communications_stats_dict


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
