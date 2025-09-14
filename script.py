import urllib.parse

# Example Paynow response URL-encoded string
response_string = ("reference=Test%2bTransaction&paynowreference=30245467&amount=5.00"
                   "&status=Created&pollurl=https%3a%2f%2fwww.paynow.co.zw%2fInterface%2fCheckPayment%2f%3fguid%3d4a388062-5042-4b2d-a054-93da0277f1f2"
                   "&hash=DA3A911ED0B4F8D23BA8C25E3D5ECAF203B8EFF871374C9556EF85D0E7608F94EF7A26AA5ACD4FA88C2A211405F3890BB7B54459C0E1366D8215DF15D529053F")

# Parse the string into a dictionary
parsed = urllib.parse.parse_qs(response_string)

# Clean display
print("=== PAYNOW SANDBOX TEST RESULT ===")
print(f"Merchant Reference: {urllib.parse.unquote(parsed['reference'][0])}")
print(f"Paynow Reference: {parsed['paynowreference'][0]}")
print(f"Amount: {parsed['amount'][0]}")
print(f"Status: {parsed['status'][0]}")
print(f"Polling URL: {urllib.parse.unquote(parsed['pollurl'][0])}")
print(f"Hash: {parsed['hash'][0]}")
print("==================================")
