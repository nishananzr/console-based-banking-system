# console-based-banking-system
A beginner-friendly Python project simulating a console-based banking system to practice core programming concepts. It allows users to create bank accounts, validate essential personal details through input forms (KYC), and assigns unique account numbers. The system automates the data validation process using regular expressions and provides a simple CLI experience for users.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

> Create new bank accounts
> Validate customer information (Name, PAN, Aadhaar, DOB, Phone)
> Digital Banking Facility activation
> Secure login functionalities
> Choose between Savings, Current and Salary account types
> Generate unique account numbers
> Account transactions, balance checking and other basic banking features
> Modular Python code for easy updates

## Prerequisites
To run this project, ensure the following:

> Python 3.x installed on your system
> Basic terminal or command-line usage knowledge
> Text editor or IDE (VS Code, PyCharm, etc.)

## Installation 

1. ### Clone The Repository
   ~~~
     git clone https://github.com/<your-github-username>/banking-system.git
     cd banking-system
   ~~~
2. ### Install Dependencies
This project uses only standard Python libraries. You don’t need to install any third-party packages.

## Configuration
There is no external API used in this version. All validations are handled locally via Python code using regex.
If you're expanding the project later to use APIs or databases, you can place the credentials in a config.py file and import them securely.

## Usage
1. ### Run the Main Script
To start the application:

~~~
    python bank_system.py
~~~

2. ### Follow the Prompts

> Enter user details when prompted
> Choose the account type
> The system will validate inputs and generate an account

3. ### Output
> Successfully created account info will be shown in the terminal
> Errors will be logged if input validation fails

## Project Structure

~~~
    ## Project Structure

```
CONSOLEBASED_BANKING/
├── Bankings.py              # Main Python script with all banking logic
├── accounts.txt             # Stores account holder info
├── digital_users.txt        # Tracks digital banking users
├── transactions.txt         # Logs of all transactions
├── README.md                # Project documentation (this file)
```

~~~

## Contributing

Pull requests are welcome! If you'd like to contribute:

> Fork the repository
> Create your feature branch (git checkout -b feature/YourFeature)
> Commit your changes (git commit -m 'Add your feature')
> Push to the branch (git push origin feature/YourFeature)
> Open a pull request

## License 
This project is licensed under the MIT License – feel free to use it and modify it as you like.

## Contact 
Created by Nishana Nizar
email : nishananzr13@gmail.com
GitHub: github.com/nishananzr



