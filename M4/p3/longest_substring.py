'''Assume s is a string of lower case characters.'''
STR_S = input()
M_C = 0
G_C = 0
C_CO = 0
for i in range(len(STR_S)-1):
    if STR_S[i] <= STR_S[i+1]:
        C_CO += 1
    else:
        C_CO = 0
    if G_C < C_CO:
        G_C = C_CO
        M_C = i
    d_d = M_C-G_C+1
print(STR_S[d_d:d_d+G_C+1])
