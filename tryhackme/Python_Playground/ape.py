#!/usr/bin/python3

import math
import string


def str_2_int_arr(s):
	intArr = []
	for c in s:
		charCode = ord(c)

		partA = math.floor(charCode / 26)
		partB = charCode % 26

		# print(f'Part A: {partA} \nPart B: {partB}')
		intArr.append(partA)
		intArr.append(partB)
	return intArr

def int_arr_2_text(int_arr):
	txt = ''
	for i in int_arr:
		txt += chr(97 + i)
	return txt


# def text_2_int_arr(text):
# 	intArr = []
# 	for c in text:
# 		intArr.append(ord(c) - 97)
# 	return intArr

# def int_arr_2_str(intArr):
# 	txt = ''
# 	for i in range(0, len(intArr), 2):
# 		partA = intArr[i]
# 		partB = intArr[i+1]
# 		for j in range(ord('A'), 200):
# 			if math.floor(j/26) == partA and (j%26) == partB:
# 				txt += chr(j)
# 				break
# 	return txt

hashed = 'dxeedxebdwemdwesdxdtdweqdxefdxefdxdudueqduerdvdtdvdu'
known = 'spaghetti'

while (len(known) * 4) < len(hashed):
	for c in string.printable:
		test = known + c
		test_hash = int_arr_2_text(str_2_int_arr(int_arr_2_text(str_2_int_arr(test))))
		if test_hash == hashed[:len(test)*4]:
			known += c
			break

print(known)