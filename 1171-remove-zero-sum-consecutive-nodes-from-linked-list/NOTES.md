​Input = [1, 2, -3, 3, 1]
Prefix sum = 1 + 2 - 3 = 0
Output = [3,1]

################################
0    1    3     0           key
0 -> 1 -> 2 -> -3 ->       value

prefix sum | listnode
		0      |      0        dummy
		1      |      1	
  2+1=3    |      2
	3-3=0    |      3
		
###################################
0    3    4
0 -> 3 -> 1

prefix sum | listnode
		0      |      0       dummy
  0+3=3    |      3
	3+1=4    |      1
