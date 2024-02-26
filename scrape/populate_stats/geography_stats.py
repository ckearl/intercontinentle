
def geography_stats(geography_div):
  total_area, land_area, water_area = find_total_land_water_area(geography_div)
  boundaries_distance, random_border_country = boundary_distance_and_random_border_country(geography_div)
  highest_elevation, mean_elevation = highest_and_mean_elevation(geography_div)
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
    boundaries_distance_div = geography_div.find("a", string="Land boundaries").parent.parent.find("strong", string="total:").parent.text
  except:
    boundaries_distance_div = None

  try:
    boundaries_distance = boundaries_distance_div.split("total: ")[1].split("border")[0]
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
    random_border_country = random.choice(boundaries_distance_div.split("border countries (")[1].split("): ")[1].split("; "))
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
    elevation_div = geography_div.find("a", string="Elevation").parent.parent
  except:
    elevation_div = None

  try:
    highest_elevation = elevation_div.find("strong", string="highest point:").parent.text.split("lowest")[0]
  except:
    highest_elevation = None

  try:
    highest_elevation = highest_elevation[-10:].split(" ")[1] + " m"
  except:
    highest_elevation = None

  try:
    mean_elevation = elevation_div.find("strong", string="mean elevation:").parent.text.split("mean elevation: ")[1]
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
    coastline_div = geography_div.find("a", string="Coastline").parent.parent
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
    geographic_coordinates = geography_div.find("a", string="Geographic coordinates").parent.parent.find("p").text
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
