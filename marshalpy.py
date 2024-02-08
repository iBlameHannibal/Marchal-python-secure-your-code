from pystyle import *
import marshal
import sys
import subprocess

while True:
    try:
        file_name = Write.Input('Type file name --> : ', Colors.blue_to_cyan)
        with open(file_name, 'r') as file:
            open_read = file.read()
            compiled_code = compile(open_read, "", "exec")
            dumps = marshal.dumps(compiled_code)

        with open('Uncode-' + file_name, "w") as start:
            start.write("import marshal\n")
            start.write("exec(marshal.loads(" + repr(dumps) + "))")

        Write.Print("(+) Done", Colors.green_to_cyan)

    except FileNotFoundError:
        Write.Print("Error: The specified file does not exist.\n", Colors.blue_to_cyan)
    except Exception as e:
        Write.Print(f"Error: {e}", Colors.red_to_cyan)

    choice = Write.Input("[1] Process another file \n[2] Exit \n ", Colors.blue_to_cyan)

    if choice == '1':
        
        continue
    elif choice == '2':
        Write.Print("Exiting...", Colors.blue_to_cyan)
        break
    else:
        Write.Print("Invalid choice. Exiting...", Colors.blue_to_cyan)
        break
