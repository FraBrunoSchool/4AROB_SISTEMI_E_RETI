"""
1. Go through this program and write a comment above each line explaining it.
2. Find all the places where a string is put inside a string. There are four places.
3. Are you sure there are only four places? How do you know? Maybe I like lying.
4. Explain why adding the two strings w and e with + makes a longer string.

2. Line 20:22 and 20:45, Line 27:17, Line 29:23;
3. It could also be in Line 39:22, but in this case the variable "hilarious" is of type bool;
4. Because the + operator concatenate the first string with the second string;
"""

# assegno 10 a types_of_people
types_of_people = 10
# ad x assegno una f-string
x = f"There are {types_of_people} types of people."
# a binary assegno una stringa
binary = "binary"
# a do_not assegno una stringa
do_not = "don't"
# ad x assegno una f-string
y = f"Those who know {binary} and those who {do_not}."

# stampo x
print(x)
# stampo y
print(y)
# stampo usando f-string che stampa x che a sua volta è una f-string
print(f"I said: {x}")
# stampo usando f-string che stampa y che a sua volta è una f-string
print(f"I also said: '{y}'")

# assegno a hilarious False che è una variabile bool
hilarious = False
# assegno a joke_evaluation una stringa, da notare le graffe al fondo che servono per usare .format
joke_evaluation = "Isn't that joke so funny?! {}"

# stampo usando .format
print(joke_evaluation.format(hilarious))

# a w assegno una stringa
w = "This is the left side of..."
# a e assegno una stringa
e = "a string with a right side."

# stampo w concatenata a e
print(w + e)
