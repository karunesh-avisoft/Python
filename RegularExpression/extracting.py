import re
contact="Contact us at support@example.com or sales@example.co.uk"
emails=re.findall('[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
,contact)
print('Emails:',emails)
total = "Total: $25.90"
total_price = re.search(r'([\d]+\.\d{2})', total)
print(total_price.group(1))