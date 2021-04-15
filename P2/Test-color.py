import termcolor
import colorama

colorama.init(strip="False")   # This is just for windows.
print("To server:", end="")
print(termcolor.colored("Message", "yellow"))