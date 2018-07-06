vowels=['A','E','I','O','U']

def approach1(inp):
    stuart=0
    kevin= 0
    for i in range(len(inp)):
        if inp[i] in vowels:
            kevin+=len(inp)-i
        else:
            stuart+=len(inp)-i

    if kevin>stuart:
        print("Kevin",kevin)
    elif stuart>kevin:
        print("Stuart",stuart)
    else:
        print("Draw")



inp = input()
approach1(inp)

#
# vowels=['A','E','I','O','U']
# stuart=0
# kevin= 0
# for i in range(len(inp)):
#     size =0
#     while i+size<len(inp):
#         tmp_str=inp[i:i+size+1]
#         print(tmp_str)
#         if tmp_str[0] in vowels:
#             kevin+=1
#         else:
#             stuart+=1
#         size+=1
#
# if kevin>stuart:
#     print("Kevin",kevin)
# elif stuart>kevin:
#     print("Stuart",stuart)
# else:
#     print("Draw")
