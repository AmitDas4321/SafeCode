import os
import base64
import zlib
import marshal

# Clear terminal and display message with colors
os.system("clear")
os.system("figlet Safe Code")
print("\033[1;35m" + "="*60)
print("\033[1;37m" + "                   Safe Code Encryption Script")
print("="*60)
print("\033[1;32m" + "               Author   : AmitDas")
print("               GitHub   : https://github.com/AmitDas4321")
print("="*60)
print("\033[0m")  # Reset to default text color

# Display instructions for the user with color and styling
print("\033[1;36m" + "="*60)
print("[INFO] - How to Use:")
print("\033[0;37m" + "1. Use the 'ls' command to list files in the current directory.")
print("2. Use the 'cd <directory>' command to change to a different directory.")
print("3. Enter the name of the Python script (e.g., script.py) that you want to encrypt.")
print("4. The encrypted script will be saved with a new name in the format 'encrypted_<script_name>.py'.")
print("\033[1;36m" + "="*60)
print("\033[0m")  # Reset to default text color

# Function to handle restricted shell (allow 'ls', 'cd', or script name)
def handle_shell():
    while True:
        command = input("\033[1;33mEnter the name of the script file you want to encrypt (e.g., script.py): \033[0m").strip()  # Direct prompt
        
        # If the user enters 'ls', list the files in the current directory
        if command == "ls":
            os.system("ls")

        # If the user enters 'cd <directory>', change directory
        elif command.startswith("cd "):
            path = command[3:].strip()  # Get the directory path after 'cd '
            if os.path.isdir(path):
                os.chdir(path)  # Change the directory
                print(f"\033[1;32mChanged directory to {path}\033[0m")
            else:
                print(f"\033[1;31m[ERROR] - '{path}' is not a valid directory.\033[0m")
        
        # If the user enters a script name (e.g., script.py), proceed to encryption
        elif os.path.exists(command) and command.endswith(".py"):
            script_path = command
            print(f"\033[1;34mEncrypting the script: {script_path}\033[0m")
            return script_path  # Return the selected script for encryption

        # If the user enters 'exit', break out of the loop
        elif command == "exit":
            break
        
        # For any other command, show an error message
        else:
            print("\033[1;31m[ERROR] - Invalid command. Only 'ls', 'cd <directory>', or a script name are allowed.\033[0m")

# Allow user to interact with the restricted shell
script_path = handle_shell()

# Read the original script
with open(script_path, "r") as file:
    code = file.read()

# Compile the script into bytecode
compiled_code = compile(code, "<string>", "exec")

# Serialize using marshal
marshalled_code = marshal.dumps(compiled_code)

# Compress with zlib
compressed_code = zlib.compress(marshalled_code)

# Encode with Base64
encoded_code = base64.b64encode(compressed_code)

# Dynamically create the encrypted script file name
# It will be in the format 'encrypted_<original_script_name>'
encrypted_script_name = f"encrypted_{os.path.splitext(os.path.basename(script_path))[0]}.py"

# Save the encrypted script with the new name
with open(encrypted_script_name, "w") as file:
    file.write(f"import base64, zlib, marshal\n")
    file.write(f"exec(marshal.loads(zlib.decompress(base64.b64decode({repr(encoded_code)}))))\n")

# Final message with more visual appeal
print("\033[1;32m" + "="*60)
print(f"[SUCCESS] - Encryption completed successfully!")
print(f"[INFO] - The script is saved as '{encrypted_script_name}'.")
print("="*60)
print("\033[0m")  # Reset to default text color
