# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    ''' given two lists (m and n), I want to find out if
    every element in n is contained within m.
    Print 'Yes' if it is, and 'No' if not.
    Case sensitivity means I can leave the text as is
    '''

    # convert magazine into a dictionary
    magaDict = {}

    for i in range(len(magazine)):
        if magazine[i] in magaDict.keys():
            magaDict[magazine[i]] += 1
        else:
            magaDict[magazine[i]] = 1

    # now check if magazine contains every element in note
    count = 0
    
    for i in range(len(note)):
        if note[i] in magaDict.keys():
            # the word shows up in magazine
            if magaDict[note[i]] < 1:
                # this means there weren't enough occurences of the word
                print('No')
                break
            else:
                magaDict[note[i]] -= 1
                count += 1
        else:
            # the word doesn't show up in magazine
            print('No')
            break

    if count == len(note):
        print('Yes')

def main():
    # setup for solution

    m = 'Hello World'
    n = 'Hello world'

    magazine = m.split()
    note = n.split()

    checkMagazine(magazine, note)

main()