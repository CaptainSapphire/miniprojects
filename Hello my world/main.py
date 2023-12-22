#print("Hello World")
#Functions
def check (a, b, c):
  if a == b:
    print("Correct!")
  else:
    while a != b:
      print("To say 'Hello World in " + c + ", say the following: ")
      print("print('Hello World')")
      python = input ("Try it!")
      if python == pythonans:
        print("Correct!")
        break

#Variables
username = input("What is your name? ")
partnername = input("What is your best friend/spouse/partner's name? (Enter 'single' if single.) ")
pythonans = "print('Hello World')"
htmlans = "<p>'Hello World'</p>"
javascriptans = "console.log('Hello World')"
language = ""
#Introduction
print("Welcome " + username + ".")
print("In code, one of the most often used phrases is 'Hello World.'")
print("A “Hello, world!” program is traditionally used to introduce novice programmers to a programming language.")
print("Why don't we learn how to say 'hello world' in a variety of languages?")
#Hello World in Python
language = "Python"
print("To say 'Hello World in " + language + ", say the following:'")
print("print('Hello World')")
python = input ("Try it!")
check(python, pythonans, language)
#Hello World in HTML
print("Now let's try saying it in another language: HTML. This isn't quite a language, but it'll still work! Try saying:")
print("<p>'Hello World'</p>")
html = input("Try it!")
check(html, htmlans, "HTML")
print("Let's do one more!")
#Hello World in Javascript
language = "Javascript"
print("To say 'Hello World in " + language + ", say the following:'")
print("console.log('Hello World')")
javascript = input("Let's try it!")
check(javascript, javascriptans, language)

if partnername.lower != "single":
  #continue
  print("not single")
  print("Here is how to say 'Hello World' in the language of you partner, " + partnername.capitalize() + ".")
  print("Hello " + username.capitalize() + ".")
  print("Get it- because you are their world! And of course, by this being sent to you, you know what your partner is telling you.")
  print("Thank you for learning some code and being so kind to your World.")
else: 
  #end
  print("Thank you for learning with us!")
