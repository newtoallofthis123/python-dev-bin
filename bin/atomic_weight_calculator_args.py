import json
import re
import argparse

int_to_str_seperator = re.compile("([a-zA-Z]+)([0-9]+)")

parser = argparse.ArgumentParser()
parser.add_argument("molecular_formula",help="Give the molecular formula in the syntax 'C12|H12|OH1'")
args = parser.parse_args()

def calculator(e):
	with open('atomic_weights.json', 'r') as file:
		content = file.read()
		atomic_weights = json.loads(content)
		atom_raw = e.split("|")
		atoms = dict()
		for i in atom_raw:
			atom = int_to_str_seperator.match(i).groups()
			atomic_weight = atomic_weights[str.lower(atom[0])]
			weight = atomic_weight * int(atom[1])
			atoms[atom[0]] = weight
		print(f'Atomic Weight of {e}: {sum(atoms.values())}')

atom_to_calculate = args.molecular_formula
calculator(atom_to_calculate)