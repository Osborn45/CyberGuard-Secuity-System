

print("------------------------")
print("Cyberguard v.1.0")
print("Personal Security System")
print("------------------------")

#Introduction to System

print("Welcome. Security Analyst")
print("Your Goal is to monitor user account information and identify potential threats")
print("Please start security assesment....")

# User Information Collection

print("Please Enter User Account Information:")

username = input("Enter username:")

email = input("Enter Email Address:")

password = input("Enter Password:")

age = int(input("Enter Age:"))

ip_address = input("Enter Ip Address:")

failed_attempts = int(input("Enter Failed login attempts:"))

account_input = input("Is the account Active or Inactive: ")

account_status = account_input.strip().upper() == "ACTIVE"

# Security Threat Detection

print("Account Security Analysis")

# Failed login attempts analysis
if failed_attempts == 0:
    login_message = "No failed login attempts detected."
elif failed_attempts < 5:
    login_message = "Low security alert: Failed login attempts detected."
else:
    login_message = "CRITICAL: Possible brute-force attack detected"

if not account_status:
    account_message = "Account is inactive."
    threat_level = "HIGH"
    recommendation = "Re-enable the account only after verifying the owner and reviewing account activity."
elif failed_attempts >= 5:
    account_message = "Account is active."
    threat_level = "HIGH"
    recommendation = "Investigate login activity and disable the account immediately."
elif failed_attempts >= 1:
    account_message = "Account is active."
    threat_level = "LOW"
    recommendation = "Monitor login activity for further suspicious behaviour."
else:
    account_message = "Account is active."
    threat_level = "LOW"
    recommendation = "No immediate action required. Continue monitoring."

password_length = len(password)

if password_length < 8:
    password_strength = "WEAK"
elif password_length < 12:
    password_strength = "MODERATE"
else:
    password_strength = "STRONG"

print(password_strength)


print("----------------------------------------")
print("         CYBERGUARD SECURITY REPORT")
print("----------------------------------------")

print("USER Account INFORMATION")
print("----------------------------------------")

print("Username:", username)
print("Email:", email)
print("Age:", age)
print("IP Address:", ip_address)

if account_status == True:
    print("Account Status: ACTIVE")
else:
    print("Account Status: INACTIVE")


print("\nSECURITY ANALYSIS")
print("----------------------------------------")

print("Password Assessment:", password_strength)
print("Failed Login Attempts:", failed_attempts)

print("\nTHREAT DETECTION")
print("----------------------------------------")

print(login_message)
print(account_message)


if failed_attempts >= 5 and account_status == True:
    print("[CRITICAL] Multiple failed login attempts!")
    print("[WARNING] Possible brute-force attack detected.")

elif failed_attempts >= 1 and account_status == True:
    print("[WARNING] Unsuccessful login attempts detected.")

elif account_status == False:
    print("[WARNING] Account is currently inactive.")

else:
    print("[SAFE] No suspicious login activity detected.")


print("\nFINAL SECURITY STATUS")
print("----------------------------------------")

print("THREAT LEVEL:", threat_level)

print("\nRECOMMENDATION:")
print(recommendation)

print("\n========================================")
print("       END OF SECURITY REPORT")
print("========================================")






