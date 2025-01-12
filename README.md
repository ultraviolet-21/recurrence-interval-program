# recurrence-interval-program

# Overview:

The Recurrence Interval Program analyzes time-series data for event occurrences. It reads data points from a user-specified file, calculates the intervals between events, and provides a statistical analysis of these intervals. The user also enters a time frame, and the program outputs the probability of the next event occurring within that time frame. The program assumes a log-normal distribution to calculate the probability of future events within a given time frame.


# Key features:

1. Data Input and Interval Calculation: The program reads data from a user-specified file containing timestamps of past events. The timestamps are in the form of “years ago” (or months, days, etc.). The user is required to enter the time of the last event, from which the rest of the times will be determined. The program will compute the intervals between consecutive points and store these intervals in a list.
2. Statistical Analysis:
    a. Mean Calculation: Determines the average interval between events.
    b. Standard Deviation: Calculates the standard deviation of the intervals to understand the variability in event 
       occurrences.
    c. Other calculations, such as logarithmic transformations, are required for lognormal distributions.
    d. The onevar_stats.py file contains other functions like range, median, and percent error if the user wishes to 
       calculate these too. The program will not automatically run these functions.
4. Probability Calculation: A lognormal distribution is assumed since the duration of an interval cannot be negative. The program computes the lognorm.cdf (cumulative distribution function) value for both user-specified endpoints. The lognorm_diff function divides the difference between these values by 1 minus the “start” value. This result is the probability of the next event occurring within the user-specified time frame.
5. Graph: Finally, the program shows a distribution plot of the interval lengths.


# Tools Used:

I made this entire project using Python 3.11, including third-party libraries such as numpy, scipy, matplotlib, and seaborn. I set these up in a virtual environment, which is needed to run the program. This project is split into several modules.


# Example Workflow:

1. User Input:
    a. The user provides the file path of the data containing event timestamps.
    b. The user specifies the reference point and the time frame for probability estimation.
    c. The user has the option to filter the data by values greater than or less than a given amount. The user can also   
       choose to use the latest x% of data. This is handled by a list of options displayed to the user. 
2. Output:
    a. The program outputs the probability of the next event occurring within the specified time range for a lognormal   
       distribution.
    b. The program displays a graph of the distribution.


# Practical Applications:

1. Financial Market Analysis: Predicting the probability of market events based on historical trading data (stock values, 
   recessions, etc.)
2. Earthquake Prediction: Estimating the probability of the next earthquake within a specific time frame based on 
   historical data.
3. Bridge and Infrastructure Maintenance: Determining the probability of structural failures or required maintenance 
   activities based on historical maintenance records.
4. Pipeline Leaks: Predicting the likelihood of future pipeline leaks or bursts using data on past incidents.
5. System Failures and Power Outages: Estimating the probability of future system downtimes or failures based on historical 
   performance data.


# Conclusion:

The Recurrence Interval Program is a powerful and versatile tool designed to analyze time-series data. By calculating the mean and standard deviation of intervals between events, the program provides robust probability estimates for future occurrences within specified time frames. This capacity is essential for risk assessment in various fields. As data-driven strategies become increasingly crucial, the Recurrence Interval Program stands out as a critical asset for anticipating and mitigating potential future events.

