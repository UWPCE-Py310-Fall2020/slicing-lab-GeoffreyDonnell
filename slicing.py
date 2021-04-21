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

	pass

a_string = "this is a string"
a_tuple = (2, 54, 13, 12, 5, 32)

assert exchange_first_last(a_string) == "ghis is a strint"
assert exchange_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)

def every_other_removed(seq):
	seq_list = list(seq)  # convert tuple to list
	seq_remove = seq_list[0::2]

	if isinstance(seq, tuple) == True:
		seq_tuple = tuple(seq_remove) #converting the list into tuple
		return seq_tuple

	if isinstance(seq, str) == True:
		seq_string = ''.join([str(elem) for elem in seq_remove])
		return seq_string

removed_string=('ABCDEF')
removed_tuple=(1, 2, 3, 4, 5, 6)

assert every_other_removed(removed_string) == ('ACE')
assert every_other_removed(removed_tuple) == (1, 3, 5)

def first4_last4_every_other_removed(seq):
    pass
def seq_reversed(seq):
    pass
def last_third_first_third_mid_third(seq):
    pass

