def madlib1():
    noun = input("Enter a noun: ")
    plural_noun = input("Enter a plural noun: ")
    noun_two = input("Enter a noun: ")
    place = input("Enter a place: ")
    adjective = input("Enter a adjective: ")

    print(f"Be kind to your {noun}-footed {plural_noun}.\nFor a duck may be somebody`s {noun_two},\nBe kind to your {plural_noun} in {place}\nWhere the weather is always {adjective}.\nYou may think that this is the {noun},\nWell it is.")

def madlib2():

    adjective = input("Enter a adjective: ")
    noun = input("Enter a noun: ")
    noise = input("Enter a noise: ")
    animal = input("Enter an animal: ")

    print(f"{adjective} Macdonald had a {noun}, E-I-E-I-O\n \
    and on that {noun} he had an {animal}, E-I-E-I-O\n \
    with a {noise} {noise} here\n \
    and a {noise} {noise}there,\n \
    here a {noise}, there a {noise},\n \
    everywhere a{ noise} {noise},\n \
    {adjective} Macdonald had a {noun}, E-I-E-I-O.")

madlib_dictionary = {"Be kind": madlib1, "Old Macdonald":madlib2}

print("¡Welcome to my madlib GAME!")
print("Select the book you like:\n")

for index,title in enumerate(madlib_dictionary.keys()):
    print(f"{index}) {title}")

opcion = int(input("Your selection: "))

for index,title in enumerate(madlib_dictionary.keys()):
    if opcion == index:
        madlib_dictionary[title]()

