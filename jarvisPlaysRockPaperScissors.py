# introduce
# random from rock,paper,scissors
# take input
# win lose

import speech_recognition as sr
import pyttsx3
import random


def recognise_voice():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak something...")
        
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        if "rock" in text.lower():
            text = "rock"
        elif "paper" in text.lower():
            text = "paper"
        elif "scissors" in text.lower():
            text = "scissors"  
    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError:
        print("Sorry, I couldn't reach the recognition service.")

    return text

def output_voice(text):
    engine = pyttsx3.init()
    # setup
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)  # bigger number slower
    engine.setProperty('volume', 1)  
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    # work
    engine.say(text)
    engine.runAndWait()

def random_move():
    moves = ["rock", "paper", "scissors"]
    choice = random.randint(0,2)

    return moves[choice]

def find_winner(user_move, machine_move):
    win = True
    if user_move == "paper" and machine_move == "scissors":
        win = False
    if user_move == "rock" and machine_move == "paper":
        win = False
    if user_move == "scissors" and machine_move == "rock":
        win = False
    if user_move == machine_move:
        return "tie"
    return win
        
def play_again_option(text):
    if "yes" in text.lower():
        return True
    if "no" in text.lower():
        return False

def play_game(jarvis_move, user_move):
    find_winner(user_move, jarvis_move)


    
def main():

    # intro
    intro_msg = "Hello, I am Jarvis your personal rock paper scissors nemisis." 
    output_voice(intro_msg)

    # jarvis voice lines
    play_msg = "You say your choice and lets see who wins! 3, 2, 1 go!"
    lose_msg = "AAAHHHHHH I cant belive I lost. Good Game."
    win_msg = "Yes i win HAHA. Good Game."
    tie_msg = "Looks like we had the same idea."
    player_win_msg = "The player won!"
    jarvis_win_msg = "Jarvis won!"


    # game info
    game_number = 0
    jarvis_score = 0
    player_score = 0
    play_game = True
    # game loop
    while(play_game):
        if jarvis_score == 3:
            output_voice(jarvis_win_msg)
        elif player_score ==3:
            output_voice(player_win_msg)

        # ask play msg
        output_voice(play_msg)

        # jarvis chooses his move
        jarvis_move = random_move()
        jarvis_move_msg = "I went " + jarvis_move

        # player choice is taken in
        user_move = recognise_voice()

        # method to decide who won base doff each move
        output_voice(jarvis_move_msg)
        if find_winner(user_move, jarvis_move) == True:
            output_voice(lose_msg)
            player_score += 1
            game_number += 1
        elif find_winner(user_move, jarvis_move) == False:
            output_voice(win_msg)
            jarvis_score += 1
            game_number += 1
        else:
            output_voice(tie_msg)
            game_number += 1

        # current game and score outputed and play again asked
        play_again_msg = "Would you like to play again. We are playing first to 3," \
        " this is game " + str(game_number) + "and the score is, Jarvis " + str(jarvis_score) + " , You " + str(player_score)
        output_voice(play_again_msg)

        user_choice = recognise_voice()
        play_game = play_again_option(user_choice)

        



if __name__ == "__main__":
    main()

