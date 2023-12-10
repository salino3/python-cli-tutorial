# python -m venv venv
# pip install click (virtual enviroment)

import click

@click.group()
def cli():
    pass

if __name__ == '__main__':
    cli()


print("Finish...")



