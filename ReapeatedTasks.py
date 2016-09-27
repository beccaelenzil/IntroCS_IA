artists = []

for i in [0, 1, 2]:
    next_artist = raw_input('Enter an artist that you like:')
    artists.append(next_artist)

print ('Thank you!  We''ll work on your recommendations now.')

def factorial(n):
    answerSoFar = 1
    for factor in range(1, n+1):
        answerSoFar = answerSoFar * factor
    return answerSoFar

print factorial (5)

def listDoubler(aList):
    doubledList = []
    for elem in aList:
        # append the value 2*elem to doubledList
        doubledList.append(2*elem)
    return doubledList


print (listDoubler([20, 21, 22]))

userPrefs = ['Maroon 5', 'Lady Gaga', 'Justin Bieber']
# storedUserPrefs = ['Maroon 5', 'Kelly Clarkson', 'Lady Gaga', 'Bruno Mars']
storedUserPrefs = [['Maroon 5', 'The Rolling Stones', 'The Beatles'],

['Lady Gaga', 'Adele', 'Kelly Clarkson', 'The Dixie Chicks', 'Lady Antebellum'],

['Kelly Clarkson', 'Lady Gaga', 'Katy Perry', 'Justin Bieber', 'Lady Antebellum'],

['The Beatles', 'Maroon 5', 'Eli Young Band', 'Scotty McCreery'],

['Adele', 'Maroon 5', 'Katy Perry', 'Bruno Mars']]

def numMatches(listA, listB):
    ''' return the number of elements that match between
        the lists userPrefs and storedUserPrefs '''
    count = 0
    for item in listA:
        if item in listB:
            count += 1
    return count

def findBestUser(userPrefs, allUsersPrefs):
    ''' Given a list of user artist preferences and a
        list of lists represented all stored users'
        preferences, return the index of the stored
        user with the most matches to the current user. '''
    max_matches = 0
    best_index = 0
    for i in range(len(allUsersPrefs)):
        curr_matches = countMatches(userPrefs,
                                    allPrefs[i])
        if curr_matches > max_matches:
            best_index = i
            max_matches = curr_matches
    return best_index


newPref = raw_input("Please enter the name of an \
artist or band that you like: " )
prefs = []

while newPref != '':
    prefs.append(newPref)
    newPref = raw_input("Please enter an artist or band \
that you like, or just press enter to see recommendations: ")

print('Thanks for your input!')

def factorial(n):
    answer = 1
    while n > 0:
        answer = answer * n
        n = n-1
    return answer

print factorial(6)

numCorrect = 0

while True:      # run forever -- or at least as long as needed...
    newPref = raw_input("Please enter an artist or band that you like, \
                 or just press enter to see recommendations: ")
    if newPref:
        prefs.append(newPref)
    else:
        break

print('Thanks for your input!')

counter = 0
while counter < 10000:
    counter = counter + 1


