#!/usr/bin/env python3

# Import the use of regular expresion operation
import re

# Opens file to write to
file = open('Question_4_Output.txt','w')

# User input for the oligo sequence
user_oligo = raw_input('Please entered an oligo sequence consisting only of the characters A, C, G, or T: ').upper()

# Function takes in a oligo sequence and returns the reverse complement
def ReverseComplement(sequence):
	reverseCom = ''
	complement = {'A':'T', 'C':'G', 'G':'C', 'T':'A'}
	for base in sequence:
		reverseCom = reverseCom + complement.get(base)

	reverseCom = reverseCom[::-1]
	return reverseCom

# Uses regex to check if the user entered a oligo sequence consisting only of the characters A, C, G, or T
while re.match(r'^[ACGT]+$', user_oligo):

	# Reverses the user input string
	reverse = ReverseComplement(user_oligo)

	# Prints reverse complement to the console
	oligo_output = "Input oligo sequence: %s\n" % user_oligo
	reverse_output = "Reverse oligo sequence complement: %s\n" % reverse
	file.write(oligo_output)
	file.write(reverse_output)

	# Prompts the user to enter another oligo sequence
	user_oligo = raw_input('Please entered another oligo sequence consisting only of the characters A, C, G, or T: ').upper()

# Informs the user they entered an invalid sequence
print("An invalid base was found in the oligo sequence.")