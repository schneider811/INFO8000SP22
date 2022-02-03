from numpy import c_


a_string = "a double quoted string can contain ''"
another_string = 'a single quotes string can contain ""'
an_escaped_string = "a double quoted string can contain \"\", but \\ must be escaped(double \\)"

a_triple_quoted_string = """everything

i type

here
sas

ds
s
is ignore This can be used to create muli-line comments - however better is to comment multi lines"""

a_formatted_string = f"a normal formatted string can contain variables {a_string}"
a_long_number= 22/7
print(a_formatted_string)

print (f'{a_long_number:.2f}')

a_long_number= 3.146

print(f'{a_long_number:.400f}')

a_string = "abc"
b_string = "b"
ab_string = f"{a_string}{b_string}"
print(ab_string)

a_raw_string = r"a raw string can contain \ characters"
print(a_raw_string)

a_raw_formated_string = rf"a raw formatted string can still contain other things {ab_string}"
print(a_raw_formated_string)

a_concatenation = "The approximation of pi is: " + str(a_long_number)
print(a_concatenation)

a_capitalized_string = "ABC"
print(a_capitalized_string)
a_lowercase_string = a_capitalized_string.lower()
print(a_lowercase_string)

a_string_with_padding = "     3       4     \n"
a_string = a_string_with_padding.strip() #returns a copy a_string = a_string_with_padding.strip()

a_string_as_a_list = list(a_string)
print(a_string_as_a_list)
a_list_as_a_string = "".join(a_string_as_a_list)
print(a_list_as_a_string)

a_string = "hello world"
a_substring = a_string[::-1]#reverses
print(a_substring)
a_substring = a_string[:3]#first 3 in list
print(a_substring)

print(len(a_substring))

for i in range(0,len(a_substring)):
    print(a_substring[i])

for c in a_substring:
    print(c)

correct_number = 7

while True:
    user_input = int(input("Guess a number: "))
    correct = user_input == correct_number
    print(correct)
    if correct:
        break
print("good job")

