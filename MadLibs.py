# string concatenation (akak how to put strings together)
# suppose we want to create a string that says "subscribe to ____"

# youtuber = "Pedro Alberto" # some string variable

# # a few ways to do this
# print("subscribe to " + youtuber)
# print("subscribe to {}".format(youtuber))
# print(f"subscribe to {youtuber}")

adj = input("Adjetivo: ")
verbo1 = input("Verbo: ")
verbo2 = input("Verbo: ")
pessoa_famosa = input("Pessoa Famosa: ")

madlib = f"Programar é tão massa, eu me sinto {adj}, é como se eu fosse {verbo1} ou então, como se eu fosse {verbo2}, assim como {pessoa_famosa}"

print(madlib)