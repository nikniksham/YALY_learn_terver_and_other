from functions_for_dict import beautiful_print, make_new_dict, generate_new_dict

dict_for_analysis = make_new_dict("titanic.csv")
statistics = generate_new_dict([["people", "adult", "child"], ["sex", "male", "female"], ["class", "First", "Second", "Third"], ["company", "alone", "with_pair"], {"average_fare": 0, "count_known_fares": 0, "survived": 0, "died": 0, "average_age": 0, "count_known_ages": 0, "survival_rate": 0, "count": 0}], {})
statistics["general"] = {"count_people": 0}
for people in dict_for_analysis.keys():

    statistics["general"]["count_people"] += 1

    age_key = "child" if dict_for_analysis[people]["who"] == "child" else "adult"
    sex = dict_for_analysis[people]["sex"]
    rank = dict_for_analysis[people]["class"]
    survived = True if dict_for_analysis[people]["survived"] == "1" else False
    fare = float(dict_for_analysis[people]["fare"])
    company = "alone" if dict_for_analysis[people]["alone"] == "True" else "with_pair"
    age = float(dict_for_analysis[people]["age"]) if dict_for_analysis[people]["age"] != "" else None

    statistics["people"][age_key]["sex"][sex]["class"][rank]["company"][company]["average_fare"] += fare
    statistics["people"][age_key]["sex"][sex]["class"][rank]["company"][company]["count_known_fares"] += 1
    statistics["people"][age_key]["sex"][sex]["class"][rank]["company"][company]["survived"] += int(survived)
    statistics["people"][age_key]["sex"][sex]["class"][rank]["company"][company]["died"] += 1 - int(survived)
    statistics["people"][age_key]["sex"][sex]["class"][rank]["company"][company]["average_age"] += age if age else 0
    statistics["people"][age_key]["sex"][sex]["class"][rank]["company"][company]["count_known_ages"] += 1 if age else 0
    statistics["people"][age_key]["sex"][sex]["class"][rank]["company"][company]["count"] += 1

for age_key in ["child", "adult"]:
    for sex_key in ["male", "female"]:
        for rank_key in ["First", "Second", "Third"]:
            for company_key in ["alone", "with_pair"]:
                statistics["people"][age_key]["sex"][sex_key]["class"][rank_key]["company"][company_key]["average_fare"] /= max(1, statistics["people"][age_key]["sex"][sex_key]["class"][rank_key]["company"][company_key]["count_known_fares"])
                statistics["people"][age_key]["sex"][sex_key]["class"][rank_key]["company"][company_key]["average_age"] /= max(1, statistics["people"][age_key]["sex"][sex_key]["class"][rank_key]["company"][company_key]["count_known_ages"])
                statistics["people"][age_key]["sex"][sex_key]["class"][rank_key]["company"][company_key]["survival_rate"] = statistics["people"][age_key]["sex"][sex_key]["class"][rank_key]["company"][company_key]["survived"] / max(1, statistics["people"][age_key]["sex"][sex_key]["class"][rank_key]["company"][company_key]["count"])


# statistics["adult"]["male"]["survival_rate"] = statistics["adult"]["male"]["survived"] / statistics["adult"]["male"]["count"]
# statistics["adult"]["female"]["survival_rate"] = statistics["adult"]["female"]["survived"] / statistics["adult"]["female"]["count"]
# statistics["child"]["male"]["survival_rate"] = statistics["child"]["male"]["survived"] / statistics["child"]["male"]["count"]
# statistics["child"]["female"]["survival_rate"] = statistics["child"]["female"]["survived"] / statistics["child"]["female"]["count"]
beautiful_print(statistics)