#!/usr/bin/env python3

def total(initial=5, *numbers, extra_number): 
	count = initial
	for number in numbers: 
		count += number
	count += extra_number 
	print(count)
	
total(10, 3, 2, extra_number=50)
