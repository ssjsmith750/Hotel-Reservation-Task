import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import matplotlib as plt
import seaborn as sns
from scipy import stats

df = pd.read_csv("/content/Hotel Reservations.csv")
df.head()

df_sample = pd.crosstab(df["no_of_adults"],df["avg_price_per_room"])
df_sample

observed_values = df_sample.values
observed_values

value=stats.chi2_contingency(df_sample)
value

chi_square = sum([((o-e)**2)/e for o,e in zip(observed_values,expected_values)])
chi_square

chi_square_value=0
for i in chi_square:
    chi_square_value=chi_square_value+i
print(chi_square_value)

critical_value=stats.chi2.ppf(q=0.95,df=2199794.088486155)
critical_value

if chi_square_value>=critical_value:
    print("Null Hypothisis H0 is Rejected,Ha is Accepted, There is some relationship between 2 categorical variables")
else:
    print("Null Hypothisis H0 is Accepted,Ha is Rejected,There is No relationship between 2 categorical variables")
    
    Null Hypothisis H0 is Accepted,Ha is Rejected,There is No relationship between 2 categorical variables
