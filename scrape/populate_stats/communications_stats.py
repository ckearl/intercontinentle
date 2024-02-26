def communications_stats(communications_div):
  try:
    mobile_phone_subscriptions = communications_div.find("a", string="Telephones - mobile cellular").parent.parent.find("p").text.split("subscriptions: ")[1].split(" (")[0]
  except:
    mobile_phone_subscriptions = None

  try:
    internet_users_div = communications_div.find("a", string="Internet users").parent.parent
  except:
    internet_users_div = None

  try:
    internet_users_total = internet_users_div.find("p").text.split("total: ")[1].split(" (")[0]
    if "note" in internet_users_total:
      internet_users_total = internet_users_total.split("note")[0]
  except:
    internet_users_total = None

  try:
    internet_users_pct = internet_users_div.find("p").text.split("population: ")[1].split(" (")[0]
  except:
    internet_users_pct = None

  try:
    internet_country_code = communications_div.find("a", string="Internet country code").parent.parent.find("p").text
  except:
    internet_country_code = None

  communications_stats_dict = {
    "mobile_phone_subscriptions": mobile_phone_subscriptions,
    "internet_users_total": internet_users_total,
    "internet_users_pct": internet_users_pct,
    "internet_country_code": internet_country_code
  }
  return communications_stats_dict
