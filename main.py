#!/usr/bin/python

import sys

from environment import *

def tokenize(chars):
	return chars.replace('(', ' ( ').replace(')', ' ) ').split()

def parse(program):
	return read_from_tokens(tokenize(program))

def read_from_tokens(tokens):
	if len(tokens) == 0:
		raise SyntaxError('Unexpected EOF while reading')
	token = tokens.pop(0)
	if token == '(':
		L = []
		while tokens[0] != ')':
			L.append(read_from_tokens(tokens))
		tokens.pop(0) # pop off ')'
		return L
	elif token == ')':
		raise SyntaxError('Unexpected ")"')
	else:
		return atom(token)

def atom(token):
	try: return int(token)
	except ValueError:
		try: return float(token)
		except ValueError:
			return Symbol(token)

def repl(prompt='lispy> '):
	while True:
		val = eval(parse(raw_input(prompt)))
		if val is not None:
			print(schemestr(val))

def schemestr(exp):
	if isinstance(exp, List):
		return '(' + ' '.join(map(schemestr, exp)) + ')'
	else:
		return str(exp)

def eval_file(filename):
	with open(filename, 'r') as file:
		data = file.read()
		val = eval(parse(data))
		if val is not None:
			print(schemestr(val))

def main():
	if len(sys.argv) > 1:
		eval_file(sys.argv[1])
	else:
		repl()

program = "(begin (define r 10) (* pi (* r r)))"

if __name__ == '__main__':
	main()
