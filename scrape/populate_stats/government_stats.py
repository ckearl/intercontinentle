def government_stats(government_div):
	try:
		government_type = government_div.find("a", string="Government type").parent.parent.find("p").text
	except:
		government_type = None

	government_stats_dict = {
			"government_type": government_type
	}
	return government_stats_dict
