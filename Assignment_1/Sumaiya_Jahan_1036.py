# name: Sumaiya Jahan; ID:1036

name = "Sumaiya Jahan"

# Remove spaces from the name
nsName = ""
for ch in name:
    if ch != " ":
        nsName += ch

# Print the original name
print("Full Name:", name)

# Count vowels and consonants
vwl = "aeiouAEIOU"
vcnt = 0
concnt = 0

for letter in nsName:
    if letter in vwl:
        vcnt += 1
    else:
        concnt += 1

print("Vowels:", vcnt)
print("Consonants:", concnt)

# Print ASCII values of each character
asci_value = []
print("ASCII Values:")
for letter in name:
   asci_value.append(ord(letter))
print(f"ASCII Values : {asci_value}")
# Reverse the name
rev_name = ""
for ch in name:
    rev_name = ch + rev_name

print("Reversed Name:", rev_name)

# Check if name is a palindrome
if name == rev_name:
    print("Is Palindrome: Yes")
else:
    print("Is Palindrome: No")

# Find and print unique letters
unq_let = []
for ch in nsName:
    if ch not in unq_let:
        unq_let.append(ch)

unq_let.sort()
print("Unique Letters:", unq_let)

# Find first non-repeating character
for ch in nsName:
    count = 0
    for other in nsName:
        if ch == other:
            count += 1
    if count == 1:
        print("First Non-Repeating Character:", ch)
        break
