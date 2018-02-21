#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    cleaned_data = []

    ### your code goes here

    for i in range(len(predictions)):
        cleaned_data.append((ages[i], net_worths[i], net_worths[i] - predictions[i]))

    cleaned_data.sort(key=lambda x:x[2])
    return cleaned_data[8:]

