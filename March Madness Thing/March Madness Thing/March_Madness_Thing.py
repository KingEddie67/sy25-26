seeds = [1, 16, 8, 9, 5, 12, 4, 13, 6, 11, 3, 14, 7, 10, 2, 15]
winners = ['Purdue', 'FDU', 'FAU', 'Memphis', 'Duke', 'Oral Roberts', 'UVA', 'Furman', 'Kentucky', 'Pitt', 'Kansas', 'Howard', 'Texas', 'Penn St', 'UCLA', 'UNC Asheville']

cinderella_count = 0

for i in range(len(seeds)):
    if seeds[i] > 8 and winners[i] != 'FDU':
        cinderella_count += 1

print(f'The number of Cinderella teams in the first round is: {cinderella_count}')