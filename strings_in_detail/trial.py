1. Because they are immutable, changing the contents of a string type variable
means building a new string. One would have to loop along the characters of the
string, appending each in turn to a newly created empty string. Whenever a ':'
is encountered, append ':-)' instead.

2. No, dictionaries need not have the same number of elements because their
elements are not interpolated by position, but rather by key name. This means
the two different % specifiers can reference the same dictionary key, and some
keys may go completely unreferenced.

3. --- names_list.py ---
names = []
name = raw_input('Enter a name')
while name != '':
	names.append(name)
	name = raw_input('Enter a name')

print ",".join(names[:-1])+" and "+name[-1]
--- end names_list.py ---

4. --- till_slip.py ---
till = []
product = raw_input('Product: ')
while product != '':
	price = float(raw_input('Price: '))
	qty = int(raw_input('Quantity: '))
	till.append((qty, product, price))
	product = raw_input('Product: ')

for item in till:
	print "%i %30s @%7.2f"%(item)
--- end till_slip.py ---

5. --- unique_count.py ---
d = {}
s = raw_input('Enter a name: ').lower().capitalize()
while s != '':
	if s in d:
		d[s] += 1
	else:
		d[s] = 1
	s = raw_input('Enter a name: ').lower().capitalize()
print d
--- end unique_count.py ---


