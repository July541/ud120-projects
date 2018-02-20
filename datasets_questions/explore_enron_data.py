#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

"""
    CEO: SKILLING JEFFREY K
	Chairman: LAY KENNETH L
	CFO: FASTOW ANDREW S
"""


import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print len(enron_data) # the number of people
# print enron_data["SKILLING JEFFREY K"]
print len(enron_data["SKILLING JEFFREY K"]) # the number of features for each people
print len([k for k, v in enron_data.items() if v.get("poi") == True]) # the number of poi in dataset
# print [k for k, v in enron_data.items() if 'FAST' in k]
print enron_data["PRENTICE JAMES"]["total_stock_value"] # total stock value of James Prentice
print enron_data["COLWELL WESLEY"]["from_this_person_to_poi"] # message count of this person send to poi
print enron_data["SKILLING JEFFREY K"]["exercised_stock_options"] # value of stock options exercised

# print "SKILLING JEFFREY K", enron_data["SKILLING JEFFREY K"]["total_payments"] if enron_data["SKILLING JEFFREY K"]["total_payments"] \
#	> enron_data["LAY KENNETH L"]["total_payments"] and enron_data["SKILLING JEFFREY K"]["total_payments"] > \
#	enron_data["FASTOW ANDREW S"]["total_payments"] else "LAY KENNETH L", enron_data["LAY KENNETH L"]["total_payments"] \
#	if enron_data["LAY KENNETH L"]["total_payments"] > enron_data["FASTOW ANDREW S"]["total_payments"] \
#	else "FASTOW ANDREW S", enron_data["FASTOW ANDREW S"]["total_payments"]

print enron_data["SKILLING JEFFREY K"]["total_payments"]
print enron_data["LAY KENNETH L"]["total_payments"]
print enron_data["FASTOW ANDREW S"]["total_payments"]

print len([k for k, v in enron_data.items() if v["salary"] != "NaN"]) # the number of folks with a quantified salary
print len([k for k, v in enron_data.items() if v["email_address"] != "NaN"]) # the number of folks with a known email address
print len([k for k, v in enron_data.items() if v["total_payments"] == "NaN"]) / float(len(enron_data)) # the percentage of people with NaN total_payments
print len([k for k, v in enron_data.items() if v["total_payments"] == "NaN" \
	and v["poi"] == True]) / float(len(enron_data)) # the percentage of poi with NaN total_payments

print len(enron_data) + 10 # the number of people alter added 10 pois
print len([k for k, v in enron_data.items() if v["total_payments"] == "NaN"]) + 10 # the number of people with NaN total_payments after added 10 pois
print len([k for k, v in enron_data.items() if v["poi"] == True]) + 10 # the number of pois alter added 10 pois
print len([k for k, v in enron_data.items() if v["total_payments"] == "NaN" \
	and v["poi"] == True]) + 10 # the number of pois with NaN total_payments after added 10 pois

