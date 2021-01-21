# to get more comfortable with hashtables in python

ratingList = {'Sleepy' : 7, 'Cringe Katalyst' : 5, 'Langeweile' : 9, 'Baroness Boredom' : 2, 'SecantTheta' : 6}

print(ratingList)

name = 'Langeweile'

slate = '2ndSlate'

print('The best one so far is ' + name + ' with a score of ' + str(ratingList[name]))

if slate in ratingList.keys():
    print(ratingList[slate])

else:
    ratingList[slate] = 6
    print(slate + ' was added to the dictionary')