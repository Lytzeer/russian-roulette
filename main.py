from rich import print
from random import randint, seed
from time import sleep


def shoot(barrels,bullet):
    chamber = randint(1, barrels)
    if chamber == bullet:
        print("You shoot yourself")
    else:
        print("You are lucky")


def check(chamber,bullet):
    if chamber == bullet:
        return True
    else:
        return False
    

def spin(barrels):
    return randint(1, barrels)


def print_loose():
    print("[red]You shoot yourself[/red]")


def print_alive():
    print("[green]You are lucky[/green]")


def print_win():
    print("[green]You win[/green]")


def check_win(barrels):
    if barrels == 0:
        return True
    else:
        return False
    

def press_enter():
    print("[yellow]Press enter to another try...[/yellow]")
    input()


def main():
    seed()
    barrels = 6
    bullet = randint(1, barrels)
    print("Russian Roulette")
    print("You have 6 barrels in front of you")
    print("You have to shoot yourself in the head")
    print("You can spin the barrel and shoot")
    print("Good luck \n")
    print(f"[yellow]Press enter to start...[yellow]")
    input()
    for i in range(barrels):
        chamber = spin(barrels)
        if check(chamber, bullet):
            print_loose()
            break
        else:
            print_alive()
            barrels -= 1
        print(f"Safe chambers left: [green]{barrels}[/green]")
        press_enter()
        
    if check_win(barrels):
        print_win()


if __name__ == "__main__":
    main()