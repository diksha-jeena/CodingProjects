vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
vowelCount = 0
with open("task.txt" , "w") as file:
  file.write("Hello \n")
  file.write("This is Diksha Jeena")

with open("task.txt" , "r") as file:
  content = file.read()
  for i in content:
    if(i in vowels):
      vowelCount += 1
print("Vowel count = " , vowelcount )
