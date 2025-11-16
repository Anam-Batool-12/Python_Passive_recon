# For educational and authorized testing only. 
# Do NOT use this tool on domains without permission.

import dns.resolver

domain = input("Enter domain name: ")
record_types = ["A", "AAAA", "NS", "MX", "TXT", "SOA", "CNAME"]

def fetch_record(domain, record_type):
    try:
        answers = dns.resolver.resolve(domain, record_type)
        return [str(rdata) for rdata in answers]

    except dns.resolver.NoAnswer:
        return ["No record found"]
    except dns.resolver.NXDOMAIN:
        return ["Domain does not exist"]
    except dns.resolver.Timeout:
        return ["Query timed out"]
    except Exception as e:
        return [f"Error: {e}"]

print("\n--- DNS Record Enumeration ---\n")

for rt in record_types:
    print(f"{rt} Records:")
    results = fetch_record(domain, rt)
    for r in results:
        print(f"  → {r}")
    print()
