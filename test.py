from paynow import Paynow
import time

# -------------------------------
# Paynow Sandbox Keys & URLs
# -------------------------------
PAYNOW_INTEGRATION_ID = 'put it here'
PAYNOW_INTEGRATION_KEY = 'put it here'
PAYNOW_RETURN_URL = 'http://localhost:8000/payments/return/'
PAYNOW_RESULT_URL = 'http://localhost:8000/payments/result/'
PAYNOW_MERCHANT_EMAIL = 'email here'

# -------------------------------
# Initialize Paynow
# -------------------------------
paynow = Paynow(
    integration_id=PAYNOW_INTEGRATION_ID,
    integration_key=PAYNOW_INTEGRATION_KEY,
    result_url=PAYNOW_RESULT_URL,
    return_url=PAYNOW_RETURN_URL
)

# -------------------------------
# Create Test Payment
# -------------------------------
print("=== PAYNOW SANDBOX TEST ===\n")
payment = paynow.create_payment('Test Transaction', PAYNOW_MERCHANT_EMAIL)
payment.add('Test Item', 5.00)

response = paynow.send(payment)
if response.success:
    print("✅ Payment created successfully!\n")
    print("Item: Test Item")
    print("Amount: $5.00")
    print("Redirect URL (open in browser to simulate payment):", response.redirect_url)
    print("Polling URL:", response.poll_url)
else:
    print("❌ Payment creation failed:", response.errors)
    exit()

# -------------------------------
# Poll for Payment Status
# -------------------------------
print("\n=== POLLING PAYMENT STATUS ===")
poll_url = response.poll_url
max_attempts = 24  # polls for up to 2 minutes (24 * 5s)
attempt = 0

while attempt < max_attempts:
    status = paynow.check_transaction_status(poll_url)
    print(f"[Attempt {attempt+1}] Current status: {status.status}")
    
    if status.status in ['Paid', 'Cancelled', 'Failed']:
        break
    
    time.sleep(5)
    attempt += 1

# -------------------------------
# Final Result
# -------------------------------
if status.status == 'Paid':
    print("\n✅ PAYMENT SUCCESSFUL!")
elif status.status == 'Cancelled':
    print("\n⚠ PAYMENT CANCELLED")
elif status.status == 'Failed':
    print("\n❌ PAYMENT FAILED")
else:
    print("\n⚠ PAYMENT NOT COMPLETED (sandbox simulation may require manual action)")

print("\nFull status data:", status.data)
print("\n=== TEST COMPLETE ===")
