import re
contact="Contact us at support@example.com or sales@example.co.uk"
emails=re.findall('[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
,contact)
print('Emails:',emails)