import csv

def longest_songs(songs):
    #longest list
    maxList = []
    maxList.append(songs[0])

    for songData in songs:
        #If there is one song end
        if len(songs) == 1:
            maxList = songs
            break
        
        #skips first row
        elif songData["Time"] == '' or maxList[0]["Time"] == '':
            continue

        #if the time is greater delete the current list and add song
        elif int(songData["Time"]) > int(maxList[0]["Time"]):
            maxList.clear()
            maxList.append(songData)
        #if the song time is equal to the current time add the song  
        elif int(songData["Time"]) == int(maxList[0]["Time"]) and songData not in maxList:
            maxList.append(songData)

    #print with exceptions for no name
    for song in maxList:
        if song["Artist"] == '':
            print(f'{song["Name"]} by unknown at {song["Time"]} seconds')
        else:
            print(f'{song["Name"]} by {song["Artist"]} at {song["Time"]} seconds')


def shortest_songs(songs):
    #short list
    minList = []
    minList.append(songs[0])
    
    #If there is one song end
    for songData in songs:
        #If there is one song end
        if len(songs) == 1:
            minList = songs
            break

        #skips first row
        elif songData["Time"] == '' or minList[0]["Time"] == '':
            continue
        
        #if the time is less delete the current list and add song
        elif int(songData["Time"]) < int(minList[0]["Time"]):
            minList.clear()
            minList.append(songData)

        #if the song time is equal to the current time add the song  
        elif int(songData["Time"]) == int(minList[0]["Time"]) and songData not in minList:
            minList.append(songData)

    #print with exceptions for no name 
    for song in minList:
        if song["Artist"] == '':
            print(f'{song["Name"]} by unknown at {song["Time"]} seconds')
        else:
            print(f'{song["Name"]} by {song["Artist"]} at {song["Time"]} seconds')

def songs_released_each_year(songs):

    #making a dictionary
    dict = {}

    #loops through the years and adds the total
    for song in songs:
        if song["Year"] not in dict:
            dict[song["Year"]] = 1
        else:
            dict[song["Year"]] += 1

    #loops through the dictionary and prints the key and the value
    for key in dict:
        if key == "":
            continue
        print(f'{key}: {dict[key]}')

def songs_in_genre(songs):
    #dictionary
    genres = {}
    
    for song in songs:
        #if genre not in dictionary add an array and song else add song
        if song["Genre"] not in genres:
            genres[song["Genre"]] = []
            genres[song["Genre"]].append(song)
        else:
            genres[song["Genre"]].append(song)

    return genres

def longest_songs_genre(genres):
    print("The longest songs and their genres: ")
    print()
    
    for genre in genres:
        print(f'Longest song(s) in {genre}:')
        longest_songs(genres[genre])
        print()

def shortest_songs_genre(genres):
    print("The shortest songs and their genres: ")
    print()

    for genre in genres:
        print(f'Longest song(s) in {genre}')
        shortest_songs(genres[genre])
        print()


def num_played_songs(songs):
    counter = 0
    for song in songs:
        #if the song has been played add to counter
        if song["Plays"] != '':
            counter += 1

    print(f'{counter} songs have been played')
    print()
    print(f'{len(songs) - counter} songs have not been played')

def read_lines_from_file(filepath):
    with open(filepath, "r", encoding="utf-16") as file:
        lines = file.readlines()
        return lines

while True:
    #obtain file from user
    file = input("Enter the name of a playlist data file: ")

    #read and output songs in playlist
    array = read_lines_from_file(file)
    songs_in_playlist = len(array) - 2
    print(f'Number of songs in the playlist: {songs_in_playlist}')
    print()
    
    #number of songs that were relased each year
    print('Number of songs that were releasead each year: ')

    #making the song dictionary while using encoding and delimiter
    songDict = []
    with open(file, "r", encoding="utf-16") as songs:
        reader = csv.DictReader(songs, delimiter="\t")
        for song in reader:
            songDict.append(dict(song))

    songs_released_each_year(songDict)
    print()
    
    print("Longest Song:")
    longest_songs(songDict)
    print()
    
    print("Shortest Song:")
    shortest_songs(songDict)
    print()

    #sorts the songs into genres
    genres = songs_in_genre(songDict)
    
    longest_songs_genre(genres)
    print()

    shortest_songs_genre(genres)
    print()

    num_played_songs(songDict)
    print()

    again = input("Do you want to analyze another file? y/n ")
    if again == "y":
        continue
    else:
        break
