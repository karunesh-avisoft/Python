import pyttsx3
# engine = pyttsx3.init()
# engine.say("Hi, we are learning how to import and use modules and we are able to do this with pyttsx3 a text to speech conversion module.")
# engine.runAndWait()

# Reference counting
import sys

x = [1, 2, 3]
print(sys.getrefcount(x)) 

y = x
print(sys.getrefcount(x)) 

y = None
print(sys.getrefcount(x))

# garbage collection
import gc
print("Generational threshold: ",gc.get_threshold())
gc.set_threshold(1000, 10, 10)
print("Generational threshold: ",gc.get_threshold())