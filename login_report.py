from datetime import datetime

analyst = input("Enter analyst name: ")
username = input("Enter username being analyzed: ")
failed_logins = int(input("Enter number of failed login attempts: "))
privileged = input("Is this a privileged account? (yes/no): ").lower()

if failed_logins > 5 and privileged == "yes":
    risk = "HIGH"
    alert = "[*] CRITICAL: Privileged account under attack!"
elif failed_logins > 5:
    risk = "MEDIUM"
    alert = "[!] ALERT: Multiple failed logins detected."
elif failed_logins > 0:
    risk = "LOW"
    alert = "[-] Notice: Some failed attempts observed."
else:
    risk = "INFORMATIONAL"
    alert = "[+] No failed logins recorded."

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

print("\n" + "="*40)
print("Cyber Defense - Login Attempt Report")
print("="*40)
print(f"Analyst: {analyst}")
print(f"User: {username}")
print(f"Failed Attempts: {failed_logins}")
print(f"Privileged Account: {privileged}")
print(f"Risk Level: {risk}")
print(f"Alert: {alert}")
print(f"Report Generated: {timestamp}")
print("="*40)