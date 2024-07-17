#!/usr/bin/python3
import sys

audit_key = sys.argv[1].replace("&", "&amp;")#.removeprefix("QR-Code:")
spend_key = sys.argv[2].replace("&", "&amp;")#.removeprefix("QR-Code:")


with open("tmp/content.xml") as f:
    text = f.read()

text = text.replace("audit-url", audit_key)
text = text.replace("spend-url", spend_key)

with open("tmp/content.xml", "w") as f:
    f.write(text)

# dead code
## return processed key strings for qrencode
#print(audit_key)
#print(spend_key)
