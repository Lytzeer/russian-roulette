"""Russian Roulette game"""

from random import randint, seed
from rich import print


def shoot(barrels, bullet):
    """Shoot yourself in the head"""
    chamber = randint(1, barrels)
    if chamber == bullet:
        print("You shoot yourself")
    else:
        print("You are lucky")


def check(chamber, bullet):
    """Check if bullet is in chamber"""
    return chamber == bullet


def spin(barrels):
    """Spin the barrel"""
    return randint(1, barrels)


def print_loose():
    """Print loose message"""
    print("[red]You shoot yourself[/red]")


def print_alive():
    """Print alive message"""
    print("[green]You are lucky[/green]")


def print_win():
    """Print win message"""
    print("[green]You win[/green]")


def check_win(barrels):
    """Check if you win"""
    return barrels == 0


def press_enter():
    """Press enter to continue"""
    print("[yellow]Press enter to another try...[/yellow]")
    input()


def main():
    """Main function"""
    seed()
    barrels = 6
    bullet = randint(1, barrels)
    print("Russian Roulette")
    print("You have 6 barrels in front of you")
    print("[blue]You have to shoot yourself in the head[/blue]")
    print("[blue]You can spin the barrel and shoot[/blue]")
    print("[red]Good luck[/red]")
    print("[red]I hope you have life insurance[/red]\n")
    print("[yellow]Press enter to start...[yellow]")
    input()
    for _ in range(barrels):
        chamber = spin(barrels)
        if check(chamber, bullet):
            print_loose()
            break
        print_alive()
        barrels -= 1
        print("Safe chambers left: [green]{barrels}[/green]")
        press_enter()
    if check_win(barrels):
        print_win()


if __name__ == "__main__":
    main()
