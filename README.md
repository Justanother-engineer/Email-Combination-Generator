# Email Generator Script

This Python script generates email ID combinations based on first names, last names, and a company domain. You can either provide the names directly via command-line arguments or through a text file.

## Features

- Generate email IDs based on first name, last name, and domain.
- Save generated email IDs to a `.txt` or `.csv` file.
- Process input from either command-line arguments or a text file.

## Installation

Clone the repository:
   ```bash
   git clone https://github.com/yourusername/repository-name.git
   cd repository-name
```

## Usage

You can use the script by providing either first name and last name directly or an input file. The domain is required in both cases.

### 1. Generate Emails from Command-Line Arguments:

```bash
python email_generator.py -f FIRSTNAME -l LASTNAME -d DOMAIN [-s FILENAME]
```
- -f: First Name
- -l: Last Name
- -d: Company Domain (required)
- -s: Specify the output file name and format (e.g., emails.txt or emails.csv)

### 2. Generate Emails from an Input File:

```bash
python email_generator.py -i INPUTFILE -d DOMAIN [-s FILENAME]
```

- -i: Input file containing first name and last name pairs separated by space (one pair per line)
- -d: Company Domain (required)
- -s: Specify the output file name and format (e.g., emails.txt or emails.csv)

## Example

### 1. From command-line arguments:

```bash
python email_generator.py -f John -l Doe -d example.com -s emails.csv
```

### From an input file:

```bash
python email_generator.py -i names.txt -d example.com -s emails.txt
```
```bash
names.txt format is as below:
John Doe
Jane Smith
```

## Error Handling
The script will provide error messages if:
- The input file is not found.
- The file format is incorrect (should contain pairs of names separated by space).
- Both -f and -l arguments and -i are provided simultaneously or neither is provided.

## Contributing

Feel free to open issues or submit pull requests if you find any bugs or have suggestions for improvements.

## Disclaimer

**This script is provided for educational purposes only.** It is intended for use in Capture The Flag (CTF) challenges, penetration testing, and other security-related educational activities. 

**Do not use this script for malicious purposes or to engage in any illegal activities.** Unauthorized access or use of computer systems and data without permission is against the law and can result in severe penalties.

By using this script, you agree to use it responsibly and ethically. The authors and contributors of this project assume no responsibility for any misuse or damage caused by this script. Always ensure you have proper authorization before using any tool or script in a security context.
