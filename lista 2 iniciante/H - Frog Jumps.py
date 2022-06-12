z = int(input())

for x in range(z):
    a = str(input())
    a += "0"
    a = [char for char in a]
    count = 0
    sizes = ""
    for b in range(len(a)):
        if (a[b]) == "L":
            count += 1
        else:
            sizes += str(count)
            sizes += "f"
            count = 0
           
    sizes = sizes.split("f")
    maior = 1
    for l in range(len(sizes)-1):
        if int(sizes[l]) > (maior - 1):
            maior = int(sizes[l]) + 1
        
    print (maior)