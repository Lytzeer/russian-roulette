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
    

def main():
    seed()
    barrels = 6
    bullet = randint(1, barrels)
    for i in range(barrels):
        chamber = spin(barrels)
        if check(chamber, bullet):
            print_loose()
            break
        else:
            print_alive()
            barrels -= 1
        print(f"Safe chambers left: [green]{barrels}[/green]")
        if i != 5:
            sleep(5)
        
    if check_win(barrels):
        print_win()


if __name__ == "__main__":
    main()