import argparse
import os
import re
import json

parser = argparse.ArgumentParser(description="The Python Project Manager.")
parser.add_argument('command', choices=["run", "test", "new"])

args = parser.parse_args()

def error(msg):
    print("\n" + msg + "\n")
    print("Exiting.")
    exit()

if args.command == "test":
    if not os.path.exists(".pargo.json"):
        error("This is not a pargo directory.")
    file = open(".pargo.json", "r")
    pargocfg = json.load(file)
    file.close()
    entry = pargocfg["test"]
    print("\n\t Running tests...\n\n")
    os.system("python " + entry)
    exit()

if args.command == "new":
    name = input("Name of project: ")
    if os.path.exists(name):
        error("Folder already exists!")
    os.makedirs(name, exist_ok=True)
    entry = input("Program entry point: [main.py] ")
    entry = "main.py" if entry == "" else entry
    test = input("Program test file: [test.py] ")
    test = "test.py" if test == "" else test
    author = input("Author: ")
    jstring = "{\n"
    jstring += "\t\"entry\": \"" + entry + "\",\n"
    jstring += "\t\"test\": \"" + test + "\",\n"
    jstring += "\t\"author\": \"" + author + "\"\n}"
    file = open(name + "/.pargo.json", "w")
    file.write(jstring)
    file.close()
    file = open(name + "/" + entry, "w")
    file.write("print(\"It Works!\")")
    file.close()
    file = open(name + "/" + test, "w")
    file.write("print(\"No tests yet.\")")
    file.close()
    exit()

if args.command == "run":
    if os.path.exists(".pargo.json"):
        file = open(".pargo.json", "r")
        pargocfg = json.load(file)
        file.close()
        entry = pargocfg["entry"]
        os.system("python " + entry)
        exit()
    else:
        error("This is not a project directory.")

parser.print_help()
