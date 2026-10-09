import re

EMAIL_PATTERN = re.compile(
    r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}\b"
)

def find_emails(text):
    emails = EMAIL_PATTERN.findall(text)
    return emails

if __name__ == "__main__":
    text = input("Enter text containing email addresses: ")
    emails = find_emails(text)

    if emails:
        print("Email addresses found:")
        for email in emails:
            print(email)
    else:
        print("No email addresses found.")
