alphabet = ['a','b','c','d','e','f','g','h','i','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','w','x','y','z']
names = ['mina','muuo']
for name in names:
    name_letter = []
    for letter in name:
        value = alphabet.index(letter)+1
        name_letter.append(value)
name_sum = sum(name_letter)
print(f"{name_sum}")
#lists ca also e used i rages as the_list = list(rage(10))
#cas e cocateated as radlist = list1 + list2.this will give the idex .format.idex(i)
