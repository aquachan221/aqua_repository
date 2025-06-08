import click
import msvcrt

@click.command()
def main():
    click.echo("Press any key to continue...")
    key = msvcrt.getch()
    click.echo(f"You pressed: {key.decode()}")

if __name__ == "__main__":
    main()