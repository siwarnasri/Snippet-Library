# Define a function that will check for missing data

def analyze_missing_data(data):
     total_missing = data.isnull().sum().sort_values(ascending=False)
     percent_missing = data.isnull().sum() / data.isnull().count() * 100
     percent_missing.sort_values(ascending=False, inplace=True)
     missing_data_analysis = pd.concat(
         [total_missing, percent_missing],
         axis=1,
         keys=['Total', 'Percentage']
     )

     return missing_data_analysis

# And let's use that function to analyze missing data in our dataframe

analyze_missing_data(churn_data)
