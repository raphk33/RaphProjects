
import requests
from bs4 import BeautifulSoup
import pandas as pd
import io
import matplotlib.pyplot as plt
import seaborn as sns

# Fetch attacking data
URL_ATTACKING = 'https://fbref.com/en/comps/20/2019-2020/stats/2019-2020-Bundesliga-Stats'
response_attacking = requests.get(URL_ATTACKING)
soup_attacking = BeautifulSoup(response_attacking.content, 'html.parser')

# Extract the main table
table_attacking = soup_attacking.find('table')

# Convert the table to a DataFrame
df_attacking = pd.read_html(io.StringIO(str(table_attacking)))[0]

# Flatten multi-level columns
df_attacking.columns = [' '.join(col).strip() for col in df_attacking.columns.values]

# Extract necessary columns
subset_df_attacking = df_attacking[['Unnamed: 0_level_0 Squad', 'Performance Ast', 'Expected xAG', 'Progression PrgC']]

# Rename columns
subset_df_attacking.columns = ['Team', 'Assists', 'Expected Assists (xAG)', 'Progressive Carries']

# Calculate metrics and points
subset_df_attacking['Points'] = (subset_df_attacking['Assists'] * 10) + (subset_df_attacking['Expected Assists (xAG)'] * 5) + subset_df_attacking['Progressive Carries']

# Sort by Points
subset_df_attacking = subset_df_attacking.sort_values(by='Points', ascending=False)

# Fetch league standings data
URL_STANDINGS = 'https://fbref.com/en/comps/20/2019-2020/2019-2020-Bundesliga-Stats#all_league_summary'
response_standings = requests.get(URL_STANDINGS)
soup_standings = BeautifulSoup(response_standings.content, 'html.parser')

# Extract league standings table
table_standings = soup_standings.findAll('table')[0]  # Assuming the standings table is the first one on the page

# Convert the table to a DataFrame
df_standings = pd.read_html(io.StringIO(str(table_standings)))[0]

# Extract necessary columns
subset_df_standings = df_standings[['Rk', 'Squad']]

# Rename columns
subset_df_standings.columns = ['Final Position', 'Team']

# Merge the two dataframes
merged_df = subset_df_attacking.merge(subset_df_standings, on='Team')

# Sort by Points and assign an Attacking Rank
merged_df['Attacking Rank'] = merged_df['Points'].rank(ascending=False)
merged_df['Final Position'] = merged_df['Final Position'].astype(int)

# Print the merged dataframe
print(merged_df[['Team', 'Attacking Rank', 'Final Position', 'Points']])

# Calculate the correlation
correlation = merged_df['Attacking Rank'].corr(merged_df['Final Position'])
print(f"Correlation between Attacking Rank and Final Position: {correlation:.2f}")

# Scatter plot with a line of best fit
plt.figure(figsize=(10, 6))
sns.regplot(x='Attacking Rank', y='Final Position', data=merged_df, scatter_kws={'s': 100}, line_kws={'color': 'red'})
plt.title('Relationship between Attacking Rank and Final Position')
plt.gca().invert_yaxis()  # Because position 1 is better than position 20
plt.show()
