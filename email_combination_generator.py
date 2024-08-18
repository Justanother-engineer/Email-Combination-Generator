import argparse
import csv
import sys

def generate_emails(first_name, last_name, domain):
    emails = [
        f"{first_name}{last_name}@{domain}",
        f"{first_name[0]}{last_name}@{domain}",
        f"{first_name}{last_name[0]}@{domain}",
        f"{first_name[0]}{last_name[0]}@{domain}",
        f"{first_name}.{last_name}@{domain}",
        f"{first_name[0]}.{last_name}@{domain}",
        f"{first_name}.{last_name[0]}@{domain}"
    ]
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
    print(f"\n [+] Emails saved to {file_name}.")

def process_input_file(file_path, domain):
    emails = []
    try:
        with open(file_path, "r") as file:
            for line in file:
                first_name, last_name = line.strip().split()
                emails.extend(generate_emails(first_name, last_name, domain))
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
        sys.exit(1)
    except ValueError:
        print(f"Error: Each line in the file should contain a first name and a last name separated by space.")
        sys.exit(1)
    return emails

def main():

    parser = argparse.ArgumentParser(
        description="Generate email ID combinations based on first name and last name",
        usage="%(prog)s [-f FIRSTNAME -l LASTNAME | -i INPUTFILE] -d DOMAIN [-s FILENAME]"
    )
    parser.add_argument("-f", help="First Name", metavar="FIRSTNAME")
    parser.add_argument("-l", help="Last Name", metavar="LASTNAME")
    parser.add_argument("-i", help="Input file containing first name and last name pairs separated by space", metavar="INPUTFILE")
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
        emails = generate_emails(args.f, args.l, args.d)

    for email in emails:
        print(email)

    if args.s:
        save_to_file(emails, args.s)

if __name__ == "__main__":
    main()
