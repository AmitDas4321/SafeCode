# SafeCode Encryption Script 🔐

![Hero_image](https://i.ibb.co/5WXBzJ4D/SafeCode.png)

## Overview
SafeCode is a Python-based encryption tool designed to securely encrypt your Python scripts. It ensures that your code remains safe from unauthorized access and protects intellectual property by converting scripts into an unreadable format. The encryption process involves compiling the script to bytecode, serializing it, and then compressing and encoding the bytecode, making it challenging for anyone to reverse-engineer your code.

## Why Use SafeCode 🚀

SafeCode is essential for developers who want to protect their Python code, especially when sharing or distributing it. Here are some reasons why you should use SafeCode:
- **Protect Intellectual Property** 💼: Safeguard your Python code from being copied or tampered with.
- **Prevent Unauthorized Access** 🚫: Encrypt your script to ensure only authorized users can access and run it.
- **Easy to Use** 👍: The encryption process is simple, and it integrates seamlessly with your workflow, offering a command-line interface for easy interaction.

Follow these steps to clone the repository and set up the environment:

### 1. Clone the repository 🖥️

Clone the SafeCode repository to your local machine using:

```bash
git clone https://github.com/AmitDas4321/SafeCode.git
```

### 2. Install dependencies 📦

Navigate into the cloned repository and install the required dependencies:

```bash
cd SafeCode && python3 setup.py install
```

This will install all the necessary dependencies.

## 📷 Screenshots
Here are some screenshots of the script in action:

**1️⃣ Running the script and Encrypt code**

![Running the script](https://i.ibb.co/M5yLV1yC/Running-the-script-and-Encrypt-code.png)

**2️⃣ Encrypted script is saved**

![Encrypyed Script](https://i.ibb.co/ccmkTtNy/Encrypted-Script.png)


## Usage 🔧

Once the installation is complete, you can use the `safeCode.py` script to encrypt your Python files.

### 1. Running the Script ▶️

To start the script, simply run:

```bash
python3 safeCode.py
```

### 2. How to Use the Script 📝

- The script will guide you with commands in a restricted shell.
  - Type `ls` to list the files in the current directory.
  - Type `cd <directory>` to change directories.
  - Type the name of the Python script you want to encrypt (e.g., `script.py`).
  - The script will be encrypted and saved as `encrypted_<script_name>.py` in the default directory (usually your Desktop).

### 3. Encryption Process 🔐

The encryption works by:
- Reading the Python script file you specify.
- Compiling the script to bytecode.
- Serializing the bytecode using `marshal`.
- Compressing the serialized bytecode with `zlib`.
- Encoding the compressed bytecode with `base64`.

The encrypted script is saved in the format `encrypted_<script_name>.py`.

### 4. Example 💡

For example, if you want to encrypt a Python script called `example.py`, you will:
- Run the script with `python3 safeCode.py`
- Select `example.py` when prompted.
- The encrypted script will be saved as `encrypted_example.py` on your Desktop.

## Features ✨

- **Secure Encryption:** 🔒 Ensures that only valid requests will trigger encryption.
- **Interactive Shell:** 💻 Provides an interactive shell where users can manage directories and files.
- **Base64, zlib, and marshal:** 🔐 Uses these techniques for encryption, ensuring a secure and compact output.

## Contributing 🤝

Contributions are welcome! If you'd like to contribute to the project, please fork the repository, make changes, and submit a pull request. ✨
