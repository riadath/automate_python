from sys import argv
script,user = argv
prompt = 'Your answer : '
print(f"Hello {user} I'm the {script} and would like to ask you a few questions")
print(f"Do you like me {user} ?")
liking = input(prompt)
print(f"Where do you live {user}?")
address = input(prompt)
print(f"What is your laptop model {user}?")
laptop = input(prompt)
print(f"""
Now you said {liking} about liking me and you live in {address}. I've 
never been there. You also said that you use {laptop} laptop. Good
""")
