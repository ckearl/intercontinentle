
def economy_stats(economy_div):
	try:
		GDP = economy_div.find("a", string="Real GDP (purchasing power parity)").parent.parent.find("p").text.split(" (")[0]
	except:
		GDP = None

	try:
		GDP_growth_rate = economy_div.find("a", string="Real GDP growth rate").parent.parent.find("p").text.split(" (")[0]
	except:
		GDP_growth_rate = None

	try:
		GDP_per_capita = economy_div.find("a", string="Real GDP per capita").parent.parent.find("p").text.split(" (")[0]
	except:
		GDP_per_capita = None

	try:
		labor_force = economy_div.find("a", string="Labor force").parent.parent.find("p").text.split(" (")[0]
	except:
		labor_force = None

	try:
		unemployment_rate = economy_div.find("a", string="Unemployment rate").parent.parent.find("p").text.split(" (")[0]
	except:
		unemployment_rate = None

	try:
		population_below_poverty_line = economy_div.find("a", string="Population below poverty line").parent.parent.find("p").text.split(" (")[0]
	except:
		population_below_poverty_line = None

	try:
		total_exports = economy_div.find("a", string="Exports").parent.parent.find("p").text.split(" (")[0]
	except:
		total_exports = None

	try:
		export_partners = economy_div.find("a", string="Exports - partners").parent.parent.find("p").text.split(" (")[0].split(", ")[:3]
	except:
		export_partners = None

	try:
		export_commodities = economy_div.find("a", string="Exports - commodities").parent.parent.find("p").text.split(" (")[0].split(", ")[:3]
	except:
		export_commodities = None

	try:
		total_imports = economy_div.find("a", string="Imports").parent.parent.find("p").text.split(" (")[0]
	except:
		total_imports = None

	try:
		import_partners = economy_div.find("a", string="Imports - partners").parent.parent.find("p").text.split(" (")[0].split(", ")[:3]
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
