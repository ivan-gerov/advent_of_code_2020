
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open('data.txt') as f:
    tickets = [ticket for ticket in f.read().split('\n')]

def get_seat_id(ticket):
    row = int(ticket[:7].replace('F', '0').replace('B', '1'), 2)
    col = int(ticket[7:].replace('L', '0').replace('R', '1'), 2)
    return row * 8 + col

# part 1 - get max seat_id
seat_ids = [get_seat_id(ticket) for ticket in tickets]
print(max(seat_ids))

# part 2 - get own seat id 

all_possible_ids = list(range(max(seat_ids) + 1))
unseen_ids = [seat for seat in all_possible_ids
              if seat not in seat_ids]
print(unseen_ids[-1])




