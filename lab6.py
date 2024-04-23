import random
from rx import from_callable, operators as op


def get_user_choice():
    return from_callable(lambda: input("Таңдаңыз: тас, қайшы, қағаз: ").strip().lower())


def get_computer_choice():
    return from_callable(lambda: random.choice(['тас', 'қайшы', 'қағаз']))


def determine_winner(user_choice, computer_choice):
    return user_choice.pipe(
        op.combine_latest(computer_choice),
        op.map(lambda choices: determine_round_winner(choices[0], choices[1]))
    )


def determine_round_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Тенде-тен!"
    elif (user_choice == 'тас' and computer_choice == 'қайшы') or \
            (user_choice == 'қайшы' and computer_choice == 'қағаз') or \
            (user_choice == 'қағаз' and computer_choice == 'тас'):
        return "Сіз ұттыңыз!"
    else:
        return "Сіз жеңілдіңіз!"


def play_game():
    print("Сулифа ойының ойнайық!")

    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    winner_stream = determine_winner(user_choice, computer_choice)

    def on_next(winner):
        print(winner)
        play_again = input("Қайталап көремізбе? (ия/жоқ): ").strip().lower()
        if play_again == 'ия':
            play_game()

    winner_stream.subscribe(
        on_next=on_next
    )


if __name__ == "__main__":
    play_game()
