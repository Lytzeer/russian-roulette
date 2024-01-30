"""Russian Roulette game"""

from random import randint, seed
from rich import print
from rich.panel import Panel


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


def print_panel():
    """Print panel"""
    return Panel(
        """[white]Russian Roulette
You have 6 barrels in front of you
You have to shoot yourself in the head
You can spin the barrel and shoot
Good luck
I hope you have life insurance[/white]""",
        title="[red]Russian Roulette[/red]",
        subtitle="[purple]Made By : Lytzeer[/purple]",
        border_style="blue",
        title_align="left",
        width=50,
    )


def main():
    """Main function"""
    seed()
    barrels = 6
    bullet = randint(1, barrels)
    print(print_panel())
    print("[yellow]Press enter to start...[yellow]")
    input()
    for _ in range(barrels):
        chamber = spin(barrels)
        if check(chamber, bullet):
            print_loose()
            break
        print_alive()
        barrels -= 1
        print(f"Safe chambers left: [green]{barrels}[/green]")
        press_enter()
    if check_win(barrels):
        print_win()


if __name__ == "__main__":
    main()
