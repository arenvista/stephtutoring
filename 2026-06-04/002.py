# - [x] Syllabus, and Computers are Neat 2026-02-02
# - [x] Input and Variables 2026-02-04
myInput: str = input("Enter an input: ")
print(myInput)
# - [x] Conditionals 2026-02-09
if int(myInput) is not 10:
    print("input is NOT 10")
else:
    print("input IS 10")
# - [x] Advanced Conditionals 2026-02-11
# - [x] Linux 2026-02-16
# - [x] Number Systems 2026-02-18
# - [ ] Lists and Loops 2026-02-23
my_empty_list = [] 
my_full_list = [1, 2, "3"]
for item in my_full_list:
    print(item)

animal = "avaax"
print(animal)
animal = [character for character in animal]
print(animal)

for char_index in range(len(animal)):
    if animal[char_index] == "a":
        animal.remove("a")
    print(animal[char_index], char_index)
print(animal)
# - [ ] Advanced Lists and Loops 2026-02-25
# - [ ] While Loops 2026-03-02
# - [ ] Strings! 2026-03-04
# - [ ] Functions 2026-03-23
# - [ ] Advanced Functions 2026-03-25
# - [ ] 2D Lists 2026-03-30
# - [ ] File Input/Output 2026-04-01
# - [ ] Sets and Tuples 2026-04-06
