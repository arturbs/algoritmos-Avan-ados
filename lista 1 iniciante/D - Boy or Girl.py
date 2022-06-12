user_name = input()
letters = []
for n in range(len(user_name)):
    if user_name[n] not in letters:
        letters.append(user_name[n])

if len(letters) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")