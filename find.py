import json
import argparse
import function

parser = argparse.ArgumentParser(
    description='Program for searching people with specific parameters'
    )
parser.add_argument('catalog')
parser.add_argument(
    '--max_age', dest='max_age', type=int, help='Write max age of person'
    )
parser.add_argument(
    '--min_age', dest='min_age', type=int, help='Write min age of person'
    )
parser.add_argument(
    '--sex', dest='sex', type=str, help='Write sex of person'
    )
parser.add_argument(
    '--professions', dest='professions', nargs="*",
    type=str,  help='Write list of persons'
    )
args = parser.parse_args()

file = open(args.catalog)
people = json.load(file)
file.close()

print(function.find_people(
    people, args.max_age, args.min_age, args.sex, args.professions
    )
)
