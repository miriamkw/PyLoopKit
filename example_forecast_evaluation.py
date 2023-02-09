from pyloopkit.forecast_evaluation import (
    get_ideal_treatment,
    get_average_glucose_penalty
)
from pyloopkit.tidepool_api_parser import (
    parse_report_and_run
)
from datetime import datetime
import json
import matplotlib.pyplot as plt
import numpy as np



blood_glucose_value = 90
interval = 1
target = 105

# UNDERSTAND THE CODE IN DAMONS REPO!!! How did he create prediction vs ..?




ideal_glucose_values = get_ideal_treatment(blood_glucose_value, interval, target)

print(" ")
print(get_average_glucose_penalty(ideal_glucose_values))
#print(ideal_glucose_values)
#print(len(ideal_glucose_values))

derived_glucose_values = get_ideal_treatment(blood_glucose_value, interval, 55)

print(" ")
print(derived_glucose_values)
#print(len(derived_glucose_values))
print(get_average_glucose_penalty(derived_glucose_values))


# Plot the treatment decisions made using derived vs true values
t = np.arange(0.0, 361.0, 1.0)
fig, ax = plt.subplots()
ax.plot(t, derived_glucose_values, label='Derived')
ax.plot(t, ideal_glucose_values, label='True')

ax.set(xlabel='Time (minutes)', ylabel='Simulated Blood Glucose (mg/dL)',
       title='Treatment Decisions')
ax.grid()

plt.show()

# To do:
# Get the current glucose value
# Get the final prediction
# use this to calculate loss

"""
with open('json.json', 'r') as f:
    user_data = json.load(f)

time_to_run = None

recommendations = parse_report_and_run(user_data, time_to_run=time_to_run)

measured_blood_glucose = recommendations.get("input_data").get("glucose_values")[-1] # Should be 171 
predicted_blood_glucose = recommendations.get("predicted_glucose_values")[-1] # Should be 99

#print(measured_blood_glucose)
#print(predicted_blood_glucose)

ideal_glucose_values = get_ideal_treatment(measured_blood_glucose, interval, target)
end_value = measured_blood_glucose + target - predicted_blood_glucose
derived_glucose_values = get_ideal_treatment(measured_blood_glucose, interval, end_value)

#print(get_average_glucose_penalty(ideal_glucose_values))
#print(get_average_glucose_penalty(derived_glucose_values))
"""





# You definitely misunderstood. Find a way to fetch the measured value after 6h 
#(remember, a part of the script will probably eventually be to use a glucose value date as the input in the function)
# so you will have to use the measured values here anyway
# check first with values from Tidepool API, by using a date where you know there are measured values after. Simply hard code values!

# To do when internet:
# Push this script with damons example values
# Push this script with example values tidepool
# Ask him again, the thing is, i am not sure i have understood correctly because I get some different numbers from you in my script
    # As the starting point in the graph was 90 mg/dL I was confused to whether your "true glucose" was the 
        # "measured after 6h" or the "now" measurement...
    # My understanding is that you first look at ONLY the CGM value that represents "now" and calculate "ideal treatment"
    # Second you ONLY look at the value predicted 6 hours from now and calculate the "ideal treatment" based on that?
    # or is the 90 mg/dL in your example _both_ from "now" and from 6 hours later?
    # maybe you could add a third curve in the graph that represents the measured values, and not just the simulated traces?
    # we need THREE values, not TWO in these functions: "now glucose", "predicted/derived glucose after 6h" and "measured glucose after 6h"
    # my confusion is towards whether you are using actual CGM measurement trajectory or not. But the more I think, the more it makes sense that you would have to do that...







# Steps to complete for this repo (should be separated into the following scripts):
# 1) Calculate one predictions (done) given a date and plot the ideal treatments based on this (recreate the plots in the document)
# 2) Given a start date and an end date, calculate the penalty for the data (which means, we need data from extended period before and after)
    # You don't have to think about missing data scenario to start with
    # Plot the measured values and which value that is predicted 6 hours later 
        # it wont be a great visualization for the prediction accuracy
        # the rationale is that these are the values we use to calculate the penalty, hence the plot will be helpful to evaluate whether the penalty functions work as intended
    # Plot the average penalty in the period (could be merged together with the last one?)
        # indicate the average penalty for all the predictions
# 3) Find the settings that minizes the loss (ISF, carb ratio and basal)
    # Assume that we only use one value for each
    # Plot the loss in 3D
    # Good algorithm for finding global minimum?
    # (EXTRA!) Then, adjust the ISF and basal using the following assumptions
        # we have a pattern that it should be highest in the morining, and in the evening, and maybe mid day. Scale with only 1-3 constants
        # settings are split into 2-hour intervals
        # ISF and basal are correlated (although scewed, effect of ISF is instant while basal is before effect kicks in)
        # link to the videos by the clinisian 







