card = input().upper()

score_part = card[:-1]
type_part = card[-1]

scores_dict = {'A': 'ace', 'J': 'jack', 'Q': 'queen', 'K': 'king'}
types_dict = {'C': 'clubs', 'D': 'diamonds', 'H': 'hearts', 'S': 'spades'}

scores = scores_dict.get(score_part, score_part)
types = types_dict.get(type_part, '')

print(f'{scores} of {types}'.lower())
