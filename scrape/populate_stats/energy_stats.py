def energy_stats(energy_div):
  try:
    electricity_access = energy_div.find("a", string="Electricity access").parent.parent.find("strong").parent.text.split("population: ")[1].split(" (")[0]
  except:
    electricity_access = None
  energy_stats_dict = {
    "electricity_access": electricity_access
  }
  return energy_stats_dict
