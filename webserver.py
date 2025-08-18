# Initial server configuration
server_ip = ("192.168.1.1",)  # Tuple - fixed and unchangeable
allowed_ips = ["192.168.1.10", "192.168.1.20"]  # List - can be updated

# Function to update allowed IPs
def update_allowed_ips(new_ip):
    if new_ip not in allowed_ips:
        allowed_ips.append(new_ip)
        print(f"IP {new_ip} added to allowed list.")
    else:
        print(f"IP {new_ip} already in allowed list.")

# Function to display configuration
def display_config():
    print("\n--- Server Configuration ---")
    print(f"Server IP (unchanged): {server_ip[0]}")
    print("Allowed IPs:", allowed_ips)

# Main menu
while True:
    print("\n1. Add Allowed IP")
    print("2. Display Configuration")
    print("3. Try to Change Server IP (Not Allowed)")
    print("4. Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        ip = input("Enter IP to allow: ")
        update_allowed_ips(ip)

    elif choice == '2':
        display_config()

    elif choice == '3':
        try:
            server_ip[0] = "10.0.0.1"  # Attempt to modify the tuple
        except TypeError:
            print("Error: Cannot modify server_ip (it's a tuple and should not change).")

    elif choice == '4':
        print("Exiting...")
        break

    else:
        print("Invalid choice.")
