# Project Title

These are simple python projects for absolute beginners <br>
These projects will help you practice the basic programming concepts<br>
A little piece of advice; don't spend too much time on practicing simple projects<br>
After making some projects, think of a problem you have and try solving it using programming<br>
This will allow you to study more advanced methods

![Project Logo](path/to/logo.png)

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Contact](#contact)

## Installation

Instructions for how to install and get the project running.

### Prerequisites

Ensure you have the following software installed before proceeding:

- [Python 3.11](https://www.python.org/downloads/release/python-3110/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) (optional but recommended)

### Checking Your Python Version

To verify that you have Python 3.11 installed, you can run:

```sh
python --version
```

### Installation Steps

1. Clone the repo
    ```sh
    git clone https://github.com/your_username/repo_name.git](https://github.com/ZeyadMohamad/Simple-Python-projects.git
    ```
2. Install python-dotenv
    ```sh
   pip install python-dotenv
    ```
3. Create a .env file
   ```sh
      # .env
    DATABASE_URL=postgresql://user:password@localhost:5432/mydatabase
    SECRET_KEY=mysecretkey
    DEBUG=True
    ```
4. Load environment variables in your Python code
    ```sh
    # app.py or main.py
    from dotenv import load_dotenv
    import os
    
    # Load environment variables from .env file
    load_dotenv()
    
    # Accessing environment variables
    database_url = os.getenv('DATABASE_URL')
    secret_key = os.getenv('SECRET_KEY')
    debug = os.getenv('DEBUG') == 'True'
    
    print(f'Database URL: {database_url}')
    print(f'Secret Key: {secret_key}')
    print(f'Debug Mode: {debug}')

    ```
## Usage
You can directly copy the program code and paste it in your environment <br>
You can also run the program using cmd
```sh
python clock.py
```

## License
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Contact Me
Gmail: zeyadezat2004@gmail.com <br>
Linkedin: https://www.linkedin.com/in/zeyad-mohammad-52258a283/ <br>
Hackerrank: https://www.hackerrank.com/profile/zoz_moh2004
