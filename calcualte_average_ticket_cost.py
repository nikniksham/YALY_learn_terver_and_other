from functions_for_dict import beautiful_print, make_new_dict, generate_new_dict

dict_for_analysis = make_new_dict("titanic.csv")
statistics = generate_new_dict([["embarked", "Southampton", "Cherbourg", "Queenstown", "unknown"], ["class", "First", "Second", "Third"],
                                ["age", "adult", "child"], ["sex", "male", "female"], ["company", "alone", "with_pair"], {"fares": [], "count": 0, "ages": []}], {})

for people in dict_for_analysis.keys():

    age_key = "child" if dict_for_analysis[people]["who"] == "child" else "adult"
    sex_key = dict_for_analysis[people]["sex"]
    class_key = dict_for_analysis[people]["class"]
    # survived = True if dict_for_analysis[people]["survived"] == "1" else False
    fare = float(dict_for_analysis[people]["fare"])
    company_key = "alone" if dict_for_analysis[people]["alone"] == "True" else "with_pair"
    age = float(dict_for_analysis[people]["age"]) if dict_for_analysis[people]["age"] != "" else None
    deck_key = dict_for_analysis[people]["deck"] if dict_for_analysis[people]["deck"] != "" else "unknown"
    embarked_key = dict_for_analysis[people]["embark_town"] if dict_for_analysis[people]["embark_town"] != "" else "unknown"

    # print(embarked_key, class_key, age_key, sex_key, company_key)
    statistics["embarked"][embarked_key]["class"][class_key]["age"][age_key]["sex"][sex_key]["company"][company_key]["fares"].append(fare)
    statistics["embarked"][embarked_key]["class"][class_key]["age"][age_key]["sex"][sex_key]["company"][company_key]["count"] += 1
    if age:
        statistics["embarked"][embarked_key]["class"][class_key]["age"][age_key]["sex"][sex_key]["company"][company_key]["ages"].append(age)

for embarked_key in ["Southampton", "Cherbourg", "Queenstown", "unknown"]:
    for class_key in ["First", "Second", "Third"]:
        for age_key in ["adult", "child"]:
            gen_count = 0
            for sex_key in ["male", "female"]:
                for company_key in ["alone", "with_pair"]:

                    fares = statistics["embarked"][embarked_key]["class"][class_key]["age"][age_key]["sex"][sex_key]["company"][company_key]["fares"]
                    ages = statistics["embarked"][embarked_key]["class"][class_key]["age"][age_key]["sex"][sex_key]["company"][company_key]["ages"]
                    gen_count += statistics["embarked"][embarked_key]["class"][class_key]["age"][age_key]["sex"][sex_key]["company"][company_key]["count"]

                    if len(fares) > 0:
                        statistics["embarked"][embarked_key]["class"][class_key]["age"][age_key]["sex"][sex_key]["company"][company_key]["minimal_fare"] = min(fares)
                        statistics["embarked"][embarked_key]["class"][class_key]["age"][age_key]["sex"][sex_key]["company"][company_key]["maximal_fare"] = max(fares)
                        statistics["embarked"][embarked_key]["class"][class_key]["age"][age_key]["sex"][sex_key]["company"][company_key]["average_fare"] = sum(fares) / len(fares)

                    if len(ages) > 0:
                        statistics["embarked"][embarked_key]["class"][class_key]["age"][age_key]["sex"][sex_key]["company"][company_key]["minimal_age"] = min(ages)
                        statistics["embarked"][embarked_key]["class"][class_key]["age"][age_key]["sex"][sex_key]["company"][company_key]["maximal_age"] = max(ages)
                        statistics["embarked"][embarked_key]["class"][class_key]["age"][age_key]["sex"][sex_key]["company"][company_key]["average_age"] = sum(ages) / len(ages)
            statistics["embarked"][embarked_key]["class"][class_key]["age"][age_key]["count"] = gen_count

beautiful_print(statistics)