# Do NOT use it on systems or domains you don't own or have written permission to test.

import whois
domain = input("Enter the domain name here: ")
print (f"Your Entered Domain is: {domain}")

try:
    domain_info = whois.whois(domain)
    print("WHOIS query successful!")

except Exception as e:
    print(f"Error: {e}")


print("Registrar:", domain_info.registrar)
print("Creation Date:", domain_info.creation_date)
print("Expiration Date:", domain_info.expiration_date)
print("Name Servers:", domain_info.name_servers)
print("Emails:", domain_info.emails)



if not domain_info.domain_name:
    print("Invalid domain or private WHOIS info.")
