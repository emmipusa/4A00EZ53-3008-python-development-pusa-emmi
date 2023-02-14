def reverse(s):   
    
    reversed_s = ""
    x = len(s) - 1
    
    while x >= 0:
        reversed_s += s[x]
        x -= 1
    return reversed_s

print(reverse("Kalle"))

