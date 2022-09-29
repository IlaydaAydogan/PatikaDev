# Enter your code here. Read input from STDIN. Print output to STDOUT
stdin=open('STDIN.txt', 'r')
inp=stdin.read()
inp=inp.split('\n')

dict_A_len=int(inp[0][0])
dict_B_len=int(inp[0][2])

dict_B_cont=inp[dict_A_len+1:]

indices_a=[i for i, x in enumerate(inp[0:dict_A_len+1]) if x == 'a']
indices_b=[j for j, x in enumerate(inp[0:dict_A_len+1]) if x == 'b']

print(indices_a, '\n', indices_b)