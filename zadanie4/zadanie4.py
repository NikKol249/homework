dnidict = {
	1:'monday, working_day',
	2:'tuesday, working_day',
	3:'wednesday, working_day',
	4:'thursday, working_day',
	5:'friday, working_day',
	6:'saturday, get_drunk',
	7:'sunday, get_drunk'
}

nomer = 1
a = 1

while nomer <= 7:
	print (nomer, dnidict[a])
	nomer = nomer + 1
	a = a + 1