teams = {'CHE': 0, 'LIV': 0, 'MUN': 0, 'NEW': 0}

matches = [
  ('CHE', 'LIV'),
  ('CHE', 'MUN'),
  ('CHE', 'NEW'),
  ('LIV', 'MUN'),
  ('LIV', 'NEW'),
  ('MUN', 'NEW')
]

for i in range(6):
  score_a, score_b = map(int,input().split())
  team_a, team_b = matches[i]

  if score_a > score_b:
    teams[team_a] += 3
  elif score_a < score_b:
    teams[team_b] += 3
  else:
    teams[team_a] += 1
    teams[team_b] += 1

score_team = sorted(teams.items(), key=lambda x: (-x[1], x[0]))

for order, (team, score) in enumerate(score_team, 1):
  print(f'{order}. {team} {score}')