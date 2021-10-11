types_of_people = 10
x = f"There are {types_of_people} types of people"
binary = "binary"                                       
do_not = "don't"
y = f"Those who know {binary} and who {do_not}."
print(x)
print(y)
print(f"I said: {x}")
print(f"I also said: '{y}'")
hilarious = True
is_not = "isn't"
joke_evaluation = "{} that joke so funny?! {}"
print(joke_evaluation.format(is_not,hilarious)) #.format() fills the blank "{}"s 
w = "This is the left side of ..."
e = "a string with a right side."
print(w + e)
