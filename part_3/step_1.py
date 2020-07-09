import argparse

parser = argparse.ArgumentParser(description='Command Line Interface (CLI) For Recording Film Reviews To File')
parser.add_argument('--film-name', help='Name Of Film', type=str)
parser.add_argument('--stars', help='Star Rating Of Film', type=int)

args = parser.parse_args()

with open("film_reviews.txt", 'a') as file:
    file.write(f'{args.film_name}, {args.stars}\n')
