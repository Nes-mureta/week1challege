# Program to create a list of integers and compute the sum
numbers_input = input("Enter a list of integers separated by spaces: ")
numbers_list = [int(num) for num in numbers_input.split()]
sum_of_numbers = sum(numbers_list)
print("Sum of the numbers:", sum_of_numbers)

# Tuple containing names of five favorite books
favorite_books = ("Book 1", "Book 2", "Book 3", "Book 4", "Book 5")

# Printing each book name on a separate line using a for loop
print("Favorite Books:")
for book in favorite_books:
    print(book)

# Program to store information about a person using a dictionary
person = {}
person['name'] = input("Enter your name: ")
person['age'] = input("Enter your age: ")
person['favorite_color'] = input("Enter your favorite color: ")
print("Person Information:", person)

# Program to create a new set containing elements common to two sets
set1_input = input("Enter elements for the first set separated by spaces: ")
set2_input = input("Enter elements for the second set separated by spaces: ")
set1 = set(map(int, set1_input.split()))
set2 = set(map(int, set2_input.split()))
common_elements = set1.intersection(set2)
print("Common elements in both sets:", common_elements)

# Program to store a list of words and filter words with odd number of characters
words = ["apple", "banana", "orange", "grape", "kiwi", "pineapple"]
odd_length_words = [word for word in words if len(word) % 2 != 0]
print("Words with odd number of characters:", odd_length_words)