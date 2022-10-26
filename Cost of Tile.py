print('What is the dimention of Floor?')
fh = int(input('Height (m): '))
fw = int(input('Width (m): '))
print()
print('What is the dimention of Tile?')
th = int(input('Height (m): '))
tw = int(input('Width (m): '))
print()
cost_per_tile = int(input('What is cost of a Tile? (₹ per m) '))

dimention_of_floor = fh * fw
dimention_of_tile = th * tw

tiles_required = dimention_of_floor/dimention_of_tile
total_cost = tiles_required * cost_per_tile
print(f'This will cost you ₹{total_cost} per tile')