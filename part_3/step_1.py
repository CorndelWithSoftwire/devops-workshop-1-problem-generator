import click

@click.command()
@click.option('--film-name', help='Name Of Film', required=True)
@click.option('--stars', help='Star Rating Of Film', required=True)
def record(film_name, stars):
    """Command Line Interface (CLI) For Recording Film Reviews To File"""
    
    with open("film_reviews.txt", 'a') as file:
        file.write(f'{film_name}, {stars}\n')
    
    click.echo('Film Review Recorded To File')

if __name__ == '__main__':
    record()