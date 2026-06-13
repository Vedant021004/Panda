import pandas as pd
ipl = pd.read_csv("deliveries.csv")
virat = ipl[ipl['batsman'] == "V Kohli"]
print(virat.groupby('bowling_team')['batsman_runs'].sum())