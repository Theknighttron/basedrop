# declare variable song with a string sentence from any music you like
count = 0
def main():
    playAudio()


# Ask the user for an int input
# Play the song for number of times based on user input
def playAudio():
    global count
    length = int(input("How many times do you want to play the song? "))
    for i in range(length):
        print("Say my name if you love me!!")
        count = count + 1
    stopAudio(length)


def stopAudio(length):
    global count
    if count == length:
        response = input("Do you want to repeat the song? Yes or No: ")
        count = 0
        if response.lower() == "yes":
            playAudio()
        else:
            print("Quitting basedrop application")


# def nextSong():

# def prevSong():


main()




