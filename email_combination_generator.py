import argparse
import csv
import sys

def generate_emails(first_name, last_name, middle_name, domain):
    # Basic email combinations
    emails = [
        f"{first_name}{last_name}@{domain}",
        f"{first_name[0]}{last_name}@{domain}",
        f"{first_name}{last_name[0]}@{domain}",
        f"{first_name[0]}{last_name[0]}@{domain}",
        f"{first_name}.{last_name}@{domain}",
        f"{first_name[0]}.{last_name}@{domain}",
        f"{first_name}.{last_name[0]}@{domain}"
    ]

    if middle_name:
        # Additional variations with middle name
        emails.extend([
            f"{first_name}{middle_name}{last_name}@{domain}",
            f"{first_name[0]}{middle_name[0]}{last_name}@{domain}",
            f"{first_name}{middle_name[0]}{last_name}@{domain}",
            f"{first_name[0]}{middle_name[0]}{last_name[0]}@{domain}",
            # Additional variations with dots or underscores:
            f"{first_name}.{middle_name}.{last_name}@{domain}",
            f"{first_name}_{middle_name}_{last_name}@{domain}"
        ])

    return emails

def save_to_file(emails, file_name):
    if file_name.endswith(".txt"):
        with open(file_name, "w") as file:
            for email in emails:
                file.write(email + "\n")
    elif file_name.endswith(".csv"):
        with open(file_name, "w", newline='') as file:
            writer = csv.writer(file)
            for email in emails:
                writer.writerow([email])
    print(f"\n[+] Emails saved to {file_name}.")

def process_input_file(file_path, domain):
    emails = []
    try:
        with open(file_path, "r") as file:
            for line_number, line in enumerate(file, start=1):
                line = line.strip()
                
                # Skip empty lines
                if not line:
                    continue

                parts = line.split()

                # Check for valid formats: [first_name, last_name] or [first_name, middle_name, last_name]
                if len(parts) == 2:
                    first_name, last_name = parts
                    middle_name = None
                elif len(parts) == 3:
                    first_name, middle_name, last_name = parts
                else:
                    raise ValueError(f" Invalid format on line {line_number}: ' {line} '\n\n[*] Each line must contain either a first name and a last name or a first name, middle name, and last name, separated by spaces.")

                emails.extend(generate_emails(first_name, last_name, middle_name, domain))

    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    
    return emails

def main():
    parser = argparse.ArgumentParser(
        description="Generate email ID combinations based on first name, last name, and optional middle name",
        usage="%(prog)s [-f FIRSTNAME -l LASTNAME [-m MIDDLENAME] | -i INPUTFILE] -d DOMAIN [-s FILENAME]"
    )
    parser.add_argument("-f", help="First Name", metavar="FIRSTNAME")
    parser.add_argument("-l", help="Last Name", metavar="LASTNAME")
    parser.add_argument("-m", help="Middle Name (optional)", metavar="MIDDLENAME")
    parser.add_argument("-i", help="Input file containing first name, last name, and optional middle name separated by space", metavar="INPUTFILE")
    parser.add_argument("-d", help="Company Domain", metavar="TARGETDOMAIN", required=True)
    parser.add_argument("-s", help="Specify the output file name and format (e.g., emails.txt or emails.csv)", metavar="FILENAME")

    args = parser.parse_args()

    if (args.f and args.l and args.i) or (not args.f and not args.l and not args.i):
        print("Error: You must provide either -f and -l or -i, but not both.")
        parser.print_help()
        sys.exit(1)

    emails = []

    if args.i:
        emails = process_input_file(args.i, args.d)
    else:
        emails = generate_emails(args.f, args.l, args.m, args.d)

    for email in emails:
        print(email)

    if args.s:
        save_to_file(emails, args.s)

if __name__ == "__main__":
    main()
