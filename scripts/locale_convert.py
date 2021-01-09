# Designed for Python 3.7. May not work on other versions.

# Imports
import argparse
import re
from io import StringIO

# Argument handler
arghandler = argparse.ArgumentParser(description='Convert LaserTank localization files.')
arghandler.add_argument('--input', type=str, help='The input file', required=True)
arghandler.add_argument('--output', type=str, help='The output file', required=True)
arghandler.add_argument('--lang', type=str, help='The language code', required=True)

# Regular expressions
menu_intro = re.compile('(([0-9]{2}|-{2}),){3}')

# Main function
def main(inpath, outpath, lang):
	print('Converting...')
	parsed = StringIO()
	parsed.write('{\n\t\t')
	with open(inpath, 'r', encoding='UTF-8') as infile:
		item_key = 0
		for in_line in infile:
			is_section = False
			# Remove leading/trailing whitespace
			in_line = in_line.strip()
			# Double up backslashes
			in_line = in_line.replace('\\', '\\\\')
			# Fix valid escape sequences
			in_line = in_line.replace('\\\\n', '\\n')
			in_line = in_line.replace('\\\\t', '\\t')
			# Escape double quotes
			in_line = in_line.replace('"', r'\"')
			# Ignore empty lines
			if len(in_line) == 0:
				continue
			# Ignore comments
			if in_line.startswith('#'):
				continue
			# Strip menu stuff if present
			if menu_intro.match(in_line[0:9]):
				in_line = in_line[9:]
				tab_loc = in_line.find(r'\t')
				if tab_loc != -1:
					in_line = in_line[:tab_loc]
				in_line = in_line.replace('&', '')
				in_line = in_line.replace('SEPARATOR', '__SEPARATOR__')
			# If we got here, there is something to parse
			parsed.write('"key' + str(item_key) + '": "' + in_line + '",\n\t\t')
			item_key += 1
	# Fix up the parsed data
	parsed = parsed.getvalue()[:-4] + '\n\t}'
	# Write the results
	with open(outpath, 'w', encoding='UTF-8') as outfile:
		outfile.write(parsed)
	# Tell the user we are done
	print('Conversion successful!')

# Get things going
if __name__ == '__main__':
	args = arghandler.parse_args()
	main(args.input, args.output, args.lang)
