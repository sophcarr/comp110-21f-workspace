"""Which Disney Princess Are You?"""

__author__ = "730320301"

player: str = ""
points: int = 0
HAT: str = '\U0001F920'


def main() -> None:
    """Main program."""
    global player
    global points
    player = input("Hello, player! What is your name? ")
    greet()
    print(player + ", do you want to keep playing?")
    print("1) Yes")
    print("2) No.")
    keep_playing: int = int(input("Enter which number you choose: "))
    while keep_playing == 1:
        points = add_point(points)
        level1: int = start()
        if level1 == 1:
            kissing()
        elif level1 == 2:
            bow()
        elif level1 == 3:
            adventure()
        else:
            print("I'm sorry, that is not an option.")
        print(player + ", do you want play this game again?")
        print("1) Yes")
        print("2) No.")
        keep_playing = int(input("Enter which number you choose: "))
        points = points + 1
    print("The End!")
    print(f"Final adventure points: {points}")


def greet() -> None:
    """Greeting."""
    print("Hello, " + player + "! This game will ask you a series of questions in order to determine which Disney Princess you are. Choose wisely, and good luck! :)")


def add_point(x: int) -> int:
    """Just to add a point to globals."""
    x = x + 1
    return x


def start() -> int:
    """Pick a weekend activity."""
    global player
    global points
    print(player + ", pick a weekend activity.")
    print("1) Kissing.")
    print("2) Shooting a bow and arrow.")
    print("3) Leaving home in search of an adventure.")
    answer0: int = int(input("Enter which number you choose: "))
    return answer0


def kissing() -> None:
    """Would you ever smooch a frog?"""
    global player
    global points
    print(player + ", would you ever smooch a frog?")
    print("1) If the situation calls for it.")
    print("2) Definitely not, why are you asking me this you freak?")
    answer1: int = int(input("Enter which number you choose: "))
    if answer1 == 1:
        print("It is pretty obvious your princess soulmate is Tiana " + HAT)
    elif answer1 == 2:
        print("It is pretty obvious your princess soulmate is Aurora " + HAT)
    else:
        print("I'm sorry, that is not an option. Please pick again.")
    points = points + 1
    print(f"Adventure Points: {points}")


def bow() -> None:
    """Bow and arrow."""
    global player
    global points
    print(player + ", it is pretty obvious your princess soulmate is Merida " + HAT)
    points = points + 1
    print(f"Adventure Points: {points}")
    from random import randint
    fact: int = randint(1, 20)
    print(f"Fun fact, Merida's favorite number is {fact}.")


def adventure() -> None:
    """Land or sea?"""
    global player
    global points
    print(player + ", do you like the land or the sea better?")
    print("1) Land.")
    print("2) Sea.")
    answer2: int = int(input("Enter which number you choose: "))
    if answer2 == 1:
        print("It is pretty obvious your princess soulmate is Rapunzel " + HAT)
    elif answer2 == 2:
        print("It is pretty obvious your princess soulmate is Ariel " + HAT)
    else:
        print("I'm sorry, that is not an option. Please pick again.")
    points = points + 1
    print(f"Adventure Points: {points}")


if __name__ == "__main__":
    main()
