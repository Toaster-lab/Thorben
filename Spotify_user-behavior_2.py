import pandas as pd

sp = pd.read_excel("d:\Python-Workspace\Spotify_data.xlsx") #Opens and reads excel file
period_sorted = ["More than 2 years",
                 "1 year to 2 years",
                 "6 months to 1 year",
                 "Less than 6 months"
                 ]
#It makes a list for the order of the periods, used later

def s0(x):
    return sp.loc[
    (sp["spotify_usage_period"] == x) &
    (sp["spotify_subscription_plan"] == "Free (ad-supported)") &
    (sp["premium_sub_willingness"] == "Yes" )
    ]
#Returns every row with a free sub_plan that wants to buy premium
# after an x amout of period with conditions to filter
def s1(x):
    return sp.loc[
    (sp["spotify_usage_period"] == x) &
    (sp["spotify_subscription_plan"] == "Free (ad-supported)") &
    (sp["premium_sub_willingness"] == "No" )
    ]
#Returns every row with a free sub_plan that DOESN'T want to buy premium 
# after an x amout of period with conditions to filter
result = [] #empty lists

for period in sp["spotify_usage_period"].unique():
    yes_count = len(s0(period))
    no_count = len(s1(period))
    total = yes_count + no_count
    no_percentage = round((no_count / total) * 100, 2)
    yes_percentage = round((yes_count / total) * 100, 2)
    result.append((period, yes_count, no_count, yes_count > no_count, yes_percentage, no_percentage))
#going through every unique answer in the Data from the collumn "spotify_usage_period"

sp_results = pd.DataFrame(result, columns=["Period", "Yes_count", "No_count", "Yes_greater", "Yes_Percentage", "No_Percentage"]) #making Dataframe, results are the data and costum index
sp_results["Period"] = pd.Categorical(sp_results["Period"], categories=period_sorted, ordered=True) #Makes Categories sortet
sp_results.sort_values("Period", inplace=True) #Updates the dataframe while not making a new one
sp_results.reset_index(drop=True, inplace=True) #resets Index
print(sp_results) 
#returns Dataframe with filtered Data
