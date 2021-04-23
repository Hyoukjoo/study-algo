n = int(input())

cases = [int(input()) for case in range(n)]

for case in cases:
	binary = bin(case)[2:][::-1]
	temp = []
	for i in range(len(binary)):
		if binary[i] == '1':
			temp.append(str(i))
	print(' '.join(temp))
