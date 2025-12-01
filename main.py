print(Problem 1)
radius = int(input("What is the radius of the circle? "))
radius = int(radius)
type_of_radius = type(radius)
print(type_of_radius)
area = 3.14*(radius*radius)
print(area)






print(Problem 2)
a = int(input("What is the value for a? "))
b = int(input("What is the value for b? "))


print("Let's solve for (a - b)+(a * b):")
answer = (a - b)+(a * b)
print("Here is the answer: " + str(answer))






print(Problem 3)
which_art = input("Do you want to see Art #1 or #2?: ")


if which_art == "1":
   print('''
    .-""""-.
   / -   -  \
  |  .-. .- |
  |  \o| |o (
  \     ^    \
  |'.  )--'  /|
 / / '-. .-'`\ \
/ /'---` `---'\ \
'.__.       .__.'
    `|     |`
     |     \
     \      '--.
      '.        `\
        `'---.   |
jgs         ,__) /
            `..'
   ''')
else:
   print('''
             (
              )
             (
       /\  .-"""-.  /\
      //\\/  ,,,  \//\\
      |/\| ,;;;;;, |/\|
      //\\\;-"""-;///\\
     //  \/   .   \/  \\
    (| ,-_| \ | / |_-, |)
      //`__\.-.-./__`\\
     // /.-(() ())-.\ \\
    (\ |)   '---'   (| /)
     ` (|           |) `
jgs     \)           (/
   ''')

