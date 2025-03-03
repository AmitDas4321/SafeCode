## Installation

Follow these steps to clone the repository and set up the environment:

### 1. Clone the repository

Clone the SafeCode repository to your local machine using the following command:

```bash
git clone https://github.com/AmitDas4321/SafeCode.git
```

### 2. Install the required dependencies

Navigate into the cloned directory and install the required dependencies by running:

```bash
cd SafeCode && python3 setup.py install
```

This will install all the necessary dependencies required for the tool to run smoothly.

## Usage

Once the setup is complete, you can use the `safeCode.py` script to encrypt Python files.

### Encrypting a Python script

To encrypt a Python script, use the following command:

```bash
python3 safeCode.py encrypt <path_to_your_python_script>
```

Replace `<path_to_your_python_script>` with the path of the Python file you want to encrypt.

### Decrypting an encrypted script

To decrypt a previously encrypted script, use the following command:

```bash
python3 safeCode.py decrypt <path_to_encrypted_script>
```

Replace `<path_to_encrypted_script>` with the path of the encrypted Python script you want to decrypt.

## Features

- **Secure Encryption:** Encrypts your Python script to keep your code safe.
- **Decryption Support:** Allows you to decrypt encrypted scripts when needed.
- **Conditional Encryption:** The encryption process is only allowed under certain conditions, making it more secure.

## Contributing

Contributions are welcome! If you would like to contribute to the SafeCode project, feel free to fork the repository, make your changes, and submit a pull request.
