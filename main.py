class Diver():
    def __init__(self, name, country, j1, j2, j3, j4 , j5):
        self.name = name
        self.country = country
        self.scores = [int(j1),int(j2),int(j3),int(j4),int(j5)]
        self.total = calc_total(self.scores)

def main():
    finalists = get_data('results.csv')
    find_winner(finalists)
   
def calc_total(scores):
    total = scores[0] + scores[1] + scores[2] + scores[3] + scores[4]

    maximum = scores[0]
    for x in range(1,len(scores)):
        if scores[x] > maximum:
            maximum = scores[x]

    minimum = scores[0]
    for x in range(1,len(scores)):
        if scores[x] < minimum:
            minimum = scores[x]

    total -= maximum + minimum
    
    return total

def find_winner(records):
  winner = records[0].total
  for x in range(len(records)):
    if records[x].total > winner:
      winner = records[x].total
  print (winner)
  

def get_data(file_name):
    records = []

    file = open(file_name)

    for line in file:
        data = line.strip().split(',')

        records.append(Diver(*data))

    return records



main()