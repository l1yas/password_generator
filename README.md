# Random Password Generator 

A simple **Python tool** to generate **strong, random passwords** using letters, digits, and special characters.
Designed for **learning purposes**, this script demonstrates **basic Python programming, loops, and randomization techniques**.


## Features

* Generates passwords of **user-specified length**.
* Uses a **wide character set**:

  * Uppercase letters (`A-Z`)
  * Lowercase letters (`a-z`)
  * Digits (`0-9`)
  * Special characters (`/*-+=][}{!@#$%^&*()'`)
* Easy to extend with **custom character sets**.
* Interactive: prompts the user for **password length**.

## Usage

1. Run the script:

```bash
python3 password_generator.py
```

2. Enter the desired password length when prompted:

```
Password Length: 16
```

3. The generated password is displayed in the terminal:

```
fG8!a2@Zq4*L1r%M
```


## How it Works

* Imports the `random` and `string` modules.
* Combines letters, digits, and special characters into a single pool.
* Prompts the user for desired password length.
* Uses a `for` loop to **pick random characters** from the pool.
* Concatenates characters into a final password.
* Prints the result to the console.

```python
for i in range(length):
    password += random.choice(characters)
```

## Requirements

* Python 3.x
* No external libraries needed (uses only standard library)


## ⚠️ Disclaimer

* **Do not use this script for production-level password management**.
* For serious security, prefer **password managers** and **cryptographically secure generators**.

