
# # Method 2 

# #     import os

# # while True:
# #   x = input("what did you want to speak = ")
# #   if x == "q":
# #     os.system("say'thanks by by'")
# #     break
# #   os.system(f"say {x}")



import pyttsx3
hlo

engine = pyttsx3.init()

while True:
    x = input("What did you want to speak? (Type 'q' to quit) = ")
    
    if x.lower() == "q":
        engine.say("Thanks, bye- bye")
        engine.runAndWait()
        break
    engine.say(x) 



    engine.runAndWait()
