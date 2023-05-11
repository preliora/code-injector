import pymem
from time import sleep

with open(r"the code path", "r") as file:
    code = file.read()

process = pymem.Pymem(input("Process: "))

try:
    process.inject_python_interpreter()
    process.inject_python_shellcode(code)
except:
    print("Make sure process is open.")
