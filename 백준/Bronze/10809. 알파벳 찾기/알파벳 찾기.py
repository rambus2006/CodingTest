from string import ascii_lowercase

s = str(input())
alphabet_list = list(ascii_lowercase)
reslist = []
for alpha in alphabet_list:
	reslist.append(str(s.find(alpha)))

res=' '.join(reslist)
print(res)
