def exchange_first_last(seq):
	seq_list = list(seq) #First convert tuple into list
	first = seq_list[0] #grabbing the first value of the list
	last = seq_list[-1] #grabbing the last value of the list
	length = len(seq_list) #determing the length of the seq_list/input
	seq_list[0] = last #replacing first value with last
	seq_list[-1] = first #replacing last value with first

	if isinstance(seq, tuple) == True:
		seq_tuple = tuple(seq_list) #converting the list into tuple
		return seq_tuple

	if isinstance(seq, str) == True:
		seq_string = ''.join([str(elem) for elem in seq_list])
		return seq_string
	else:
		return seq_list
	pass

def every_other_removed(seq):
	seq_list = list(seq)  # convert tuple to list
	seq_remove = seq_list[0::2]

	if isinstance(seq, tuple) == True:
		seq_tuple = tuple(seq_remove) #converting the list into tuple
		return seq_tuple

	if isinstance(seq, str) == True:
		seq_string = ''.join([str(elem) for elem in seq_remove])
		return seq_string
	else:
		return seq_remove

def first4_last4_every_other_removed(seq):
	seq_list = list(seq) #First convert input into list
	if len(seq_list) < 10: #input needs to pass this test
		return print('Input needs to have at least 10 characters')
		exit()
	else:
		middle = seq_list[4:-4]
		middle_every_other = middle[::2]

	if isinstance(seq, tuple) == True: #if given an tuple we will need to return a tuple
		seq_tuple = tuple(middle_every_other) #converting the list into tuple
		return seq_tuple

	if isinstance(seq, str) == True: #if given a string we will need to return a string
		seq_string = ''.join([str(elem) for elem in middle_every_other])
		return seq_string
	else:
		return middle_every_other
	pass

def seq_reversed(seq):
	reversed_input = list(seq[::-1])

	if isinstance(seq, tuple) == True:
		seq_tuple = tuple(reversed_input) #converting the list into tuple
		return seq_tuple

	if isinstance(seq, str) == True:
		seq_string = ''.join([str(elem) for elem in reversed_input])
		return seq_string
	else:
		return reversed_input
	pass

def last_third_first_third_mid_third(seq):
	seq_list = list(seq)  # First convert input into list
	size = len(seq_list)
	if not size % 3 == 0:
		print('Input needs to be in multiples of 3')
		exit()
	else:
		increment = int(size / 3)
		first_third = seq_list[0:increment]
		middle_third = seq_list[increment:2 * increment]
		last_third = seq_list[2 * increment:3 * increment]
		total = last_third + first_third + middle_third

	if isinstance(seq, tuple) == True:  # if given an tuple we will need to return a tuple
		seq_tuple = tuple(total)  # converting the list into tuple
		return seq_tuple

	if isinstance(seq, str) == True:  # if given a string we will need to return a string
		seq_string = ''.join([str(elem) for elem in total])
		return seq_string
	else:
		return total
	pass

#Below are asserts I have written to test my code

a_list = [1, 'A', 2, 'B', 3, 'C']
a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)
assert exchange_first_last(a_list) == ['C', 'A', 2, 'B', 3, 1]
assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

removed_list = [1, 'A', 2, 'B', 3, 'C']
removed_string = ('ABCDEF')
removed_tuple = (1, 2, 3, 4, 5, 6)
assert every_other_removed(removed_list) == [1, 2, 3]
assert every_other_removed(removed_string) == ('ACE')
assert every_other_removed(removed_tuple) == (1, 3, 5)

first4last4_list = [1, 'A', 2, 'B', 3, 'C', 4, 'D', 5, 'E', 6, 'F']
first4last4_string = ('0123456789AB')
first4last4_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)

assert first4_last4_every_other_removed(first4last4_list) == [3, 4]
assert first4_last4_every_other_removed(first4last4_string) == ('46')
assert first4_last4_every_other_removed(first4last4_tuple) == (5,7)

reversed_list = [1,2,3,4,5,6,7,8,9,10]
reversed_string = 'somewords'
reversed_tuple = (1,2,3,4,5,6,7,8,9,10)

assert seq_reversed(reversed_list) == [10,9,8,7,6,5,4,3,2,1]
assert seq_reversed(reversed_string) == 'sdrowemos'
assert seq_reversed(reversed_tuple) == (10,9,8,7,6,5,4,3,2,1)

third_tuple_small = ('A', 'B', 'C')
third_tuple_large = ('A', 'B', 'C', 'D', 'E', 'F')
third_list = [1,2,3,4,5,6]
third_string = '123ABC'
assert last_third_first_third_mid_third(third_tuple_small) == ('C', 'A', 'B')
assert last_third_first_third_mid_third(third_tuple_large) == ('E', 'F', 'A', 'B', 'C', 'D')
assert last_third_first_third_mid_third(third_list) == [5, 6, 1, 2, 3, 4]
assert last_third_first_third_mid_third(third_string) == ('BC123A')