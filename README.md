# RaphProjects
The Relationship Between Attacking Football & League Position

Motivation:
It has always been said that statistics don't show the full picture of football. Certainly this is true; however, I believe that the extent to which statistics can paint a picture of football
lies far beyond what has already been discovered. Using the plethora of statistics available today, I believe that it is possible to understand the style of play that football teams employ, using simple statistics.

Objective:
To investigate whether playing a more attacking style of football positively impacts a team's league position in the Bundesliga for the 2019-2020 season.

Data Collection:
The data was sourced from FBref.com, specifically:

Attacking metrics (Assists, Expected Assists, Progressive Carries)
Final league standings for the 2019-2020 Bundesliga season.

What follows is the project's methodology.

Data Extraction & Preprocessing:

The attacking metrics and league standings tables were fetched from the website and converted to pandas dataframes.
Columns were renamed for clarity, and necessary metrics were isolated.

Point System for Attacking Nature:

In order to evaluate how attacking a team plays using statistics, a points system was created.
Productive Team Goals are Non-Penalty Goals that have a corresponding Assist. This removes part of the randomness that is the nature of football, and seeks to analyze how many 
goals came from a premeditated assist, and not just chance. Of course, randomness will still play a factor, but this was an attempt in reducing it.
Expected Productive Team Goals are calculated the same way, just using expected Goals that correspond to expected Assists. These "expected" stats are calculated match by match
by evaluating every single attacking touch of the ball and comparing it to other previous touches that have existed, and analyzing the times that these touches have become goals or assists in the past.
Thus, the "expected" stats seek to find how many times a goal SHOULD have been scored in a specific match, or how many times an assist SHOULD have happened.

A point system was established to rank teams based on their attacking play:
10 points for each Productive Team Goal.
5 points for each Expected Productive Team Goal.
1 point for each Progressive Carry.

Ranking Teams:

Based on the cumulative points from the above metrics, teams were ranked to gauge their attacking nature.
This 'Attacking Rank' was then compared with the 'Final Position' from the league standings.
Correlation Analysis:

A correlation coefficient was calculated to quantify the relationship between 'Attacking Rank' and 'Final Position'.
A scatter plot was generated with a line of best fit to visualize this relationship.
Findings:

Correlation Coefficient:
The correlation between the Attacking Rank and Final Position was found to be 0.80. This indicates a strong positive relationship, meaning teams that had a more attacking style (as per our metrics and point system) generally finished higher in the league standings.

Visual Insights:
The scatter plot showcases that teams with a lower (better) attacking rank tend to have a lower (better) league position. The red line of best fit supports this observation.

Conclusion:
For the 2019-2020 Bundesliga season, there is a strong indication that teams playing more attacking football, as defined by our metrics (Assists, Expected Assists, and Progressive Carries), tend to finish higher in the league. Of course, this does not imply causation, as football is a multifaceted sport. In future attempts, I would like to explore how to come up with a better rating system for how attacking teams play. As of right now, however, the results seem to line up. Bayern Munich, arguably the most attacking team in the world, tops the charts, closely followed by BVB Dortmund & RB Leipzig, who sport similar schools of football. At the bottom of the rankings lies Union Berlin, a team known for their hardcore counteroffensive play. In terms of thier comparison to how they finished - Bayern, Dortmund & Leipzig all finished top 3 in the league. However, Union, although last in attacking rankings, finished 11th in the table. Moreover, in the last year, they have finished in the top 4 of the league, while still maintaining their defensive, counterattacking identity. 
Overall, this was a very interesting study, and I am curious to see what the future holds for analyzing styles of football using statistics.
