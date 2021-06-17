# mathesis.cup.gr
# Ν. Αβούρης: Εισαγωγή στην Python
# Μάθημα 16: Εργασία επανάληψης
# Άσκηση 16_1_template
import random
import time

marker = {'Παίκτης 1': 'X', 'Παίκτης 2': 'O', }

def display_board(board):
    #εμφάνισε την κατάσταση της τρίλιζας
    pass

def choose_first():
    #κλήρωση για το ποιος θα παίξει πρώτος
    # επιστρέφει είτε 'Παίκτης 1' είτε 'Παίκτης 2'
    pass

def display_score(score):
    #Τυπώνει το τελικό σκορ
    pass

def place_marker(board, marker, position):
    #Τοποθετεί στη θέση position του board τον marker
    pass

def win_check(board,mark):
    #επιστρέφει True αν το σύμβολο mark έχει σχηματίσει τρίλιζα
    pass


def board_check(board):
    #επιστρέφει True αν υπάρχουν ακόμη κενά τετράγωνα
    pass
 
def player_choice(board, turn):
    # Ο Παίκτης turn επιλέγει τετράγωνο
    # Επιστρέφει έναν ακέραιο στο διάστημα [1,9]
    pass

def replay():
    # Ρωτάει τον χρήστη αν θέλει να ξαναπαίξει και επιστρέφει True αν ναι.
    pass

def next_player(turn):
    #επιστρέφει τον επόμενο παίκτη που πρέπει να παίξει
    pass

def main():
    score = {} # λεξικό με το σκορ των παικτών
    print('Αρχίζουμε!\nΓίνεται κλήρωση ', end = '')
    for t in range(10):
        time.sleep(1)
        print(".", end =' ')
    print()
    turn = choose_first() # η μεταβλητή turn αναφέρεται στον παίκτη που παίζει
    print("\nΟ " + turn + ' παίζει πρώτος.')
    first = turn # η μεταβλητή first αναφέρεται στον παίκτη που έπαιξε πρώτος
    game_round = 1 # γύρος παιχνιδιού
    while True:
        # Καινούργιο παιχνίδι
        theBoard = [' '] * 10
        game_on = True  #ξεκινάει το παιχνίδι
        while game_on:
            display_board(theBoard) #Εμφάνισε την τρίλιζα
            position = player_choice(theBoard, turn) # ο παίκτης <turn> επιλέγει θέση
            place_marker(theBoard, marker[turn], position) # τοποθετείται η επιλογή του
            if win_check(theBoard, marker[turn]): # έλεγχος αν νίκησε
                display_board(theBoard)
                print('Νίκησε ο '+ turn)
                score[turn] = score.get(turn, 0) + 1
                game_on = False
            elif board_check(theBoard): # έλεγχος αν γέμισε το ταμπλό χωρίς νικητή
                display_board(theBoard)
                print('Ισοπαλία!')
                game_on = False
            else: # αλλιώς συνεχίζουμε με την κίνηση του επόμενου παίκτη
                turn = next_player(turn)
        if not replay():
            ending = ''
            if game_round>1 : ending = 'υς'
            print("Μετά {} γύρο{}".format(game_round, ending))
            display_score(score) # έξοδος ... τελικό σκορ
            break
        else :
            game_round += 1
            turn = next_player(first) # στο επόμενο παιχνίδι ξεκινάει ο άλλος παίκτης
            first = turn
main()

    
    
