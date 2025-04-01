numbers =[1,2,3]
print(numbers)
my_list = [1, "hello", 3.4]
print(my_list)
languages = ["python", "java", "c++"]
print(languages)
print (languages[0])
print (languages[2])
print(languages[2:3])
languages.append("ruby")
print(languages)
prime_numbers = [2,3,5,7,11]
print(prime_numbers)
even_numbers = [4,6,8]
print(even_numbers)
prime_numbers.extend(even_numbers)
print("list after extending:", prime_numbers)
languages[2] = "c"
print(languages)
del languages[2]
print(languages)
languages.remove("java")
print(languages)
languages.index("ruby")
print(languages)
languages.count("python")
print(languages)
even_numbers.sort()
print(even_numbers)
for number in even_numbers:
    print(number)
    numbers = [number *number for number in range(1,6)]
    print(numbers)