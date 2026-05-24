import re
import json

#reading the raw data or input from .txt file
file = open("../input/raw-text.txt", "r", encoding="utf-8")
content = file.read()
file.close()

#regex for ALU email addresses
email_regex = r'[a-zA-Z0-9._%+-]+@(alueducation\.com|alumni\.alueducation\.com|si\.alueducation\.com)'

#regex for credit card numbers
card_regex = r'\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b'

#regex for phone numbers
phone_regex = r'(\+\d{1,3}[\s-]?\d{3}[\s-]?\d{3}[\s-]?\d{3,4}|\b\d{10}\b)'

#Regex for hashtags
hashtag_regex = r'#[A-Za-z0-9_]+'

found_emails = re.finditer(email_regex, content)
found_cards = re.findall(card_regex, content)
found_phones = re.findall(phone_regex, content)
found_hashtags = re.findall(hashtag_regex, content)

valid_emails = []

# Ignoring suspicious email inputs
for item in found_emails:
    full_email = item.group()

    if ".." not in full_email and "<script>" not in full_email.lower() and " " not in full_email:
        
        parts = full_email.split("@")
        username = parts[0]
        domain = parts[1]

        hidden_email = username[:2] + "***@" + domain

        valid_emails.append(hidden_email)

valid_emails = list(dict.fromkeys(valid_emails))
found_cards = list(dict.fromkeys(found_cards))
found_hashtags = list(dict.fromkeys(found_hashtags))

#clean phone results 
clean_phones = []

for p in found_phones:
    phone = p.replace("\n", " ").strip()

    if phone not in clean_phones:
        clean_phones.append(phone)

secured_cards = []

#Hiding part of the credit card numbers
for number in found_cards:
    cleaned = re.sub(r'[- ]', '', number)

    if len(cleaned) == 16 and cleaned.isdigit():
        hidden = "************" + cleaned[-4:]
        secured_cards.append(hidden)

#organizing the extracted datasets 
results = {
    "emails": valid_emails,
    "credit_cards": secured_cards,
    "phone_numbers": clean_phones,
    "hashtags": found_hashtags
}

#writing the results into the .json file

output = open("../output/sample-output.json", "w", encoding="utf-8")

json.dump(results, output, indent=4)

output.close()

# printing the final extracted results(output) to the console 

print(json.dumps(results, indent=4))
