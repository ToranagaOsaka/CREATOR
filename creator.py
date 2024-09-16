import os
import sys
from eth_account import Account
import secrets
import concurrent.futures
import winsound  # For playing sound on Windows (use playsound for cross-platform)
from termcolor import colored

# Folder for saving vanity wallets
vanity_folder = "vanity_wallets"
os.makedirs(vanity_folder, exist_ok=True)

# Function to print ASCII art in green
def print_ascii_art():
    art = '''
    ▐▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▌
    ▐ ▄████▄   ██▀███  ▓█████ ▄▄▄     ▄▄▄█████▓ ▒█████   ██▀███  ▌
    ▐▒██▀ ▀█  ▓██ ▒ ██▒▓█   ▀▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒▌
    ▐▒▓█    ▄ ▓██ ░▄█ ▒▒███  ▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒▌
    ▐▒▓▓▄ ▄██▒▒██▀▀█▄  ▒▓█  ▄░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄  ▌
    ▐▒ ▓███▀ ░░██▓ ▒██▒░▒████▒▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒▌
    ▐░ ░▒ ▒  ░░ ▒▓ ░▒▓░░░ ▒░ ░▒▒   ▓▒█░ ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░▌
    ▐  ░  ▒     ░▒ ░ ▒░ ░ ░  ░ ▒   ▒▒ ░   ░      ░ ▒ ▒░   ░▒ ░ ▒░▌
    ▐░          ░░   ░    ░    ░   ▒    ░      ░ ░ ░ ▒    ░░   ░ ▌
    ▐░ ░         ░        ░  ░     ░  ░            ░ ░     ░     ▌
    ▐░                                                           ▌
    ▐▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▌
    '''
    print(colored(art, 'green'))

# Function to generate a single vanity Ethereum address with the specified prefix and suffix
def generate_vanity_address(prefix, suffix, case_sensitive=False):
    while True:
        # Generate a random private key
        priv_key = "0x" + secrets.token_hex(32)
        account = Account.from_key(priv_key)
        address = account.address

        # If case sensitivity is required, compare addresses exactly as per the casing in the prefix and suffix
        if case_sensitive:
            if address[2:].startswith(prefix) and address[-len(suffix):] == suffix:
                return {"address": address, "privKey": priv_key}
        else:
            # Compare the address ignoring case sensitivity
            if address[2:].lower().startswith(prefix.lower()) and address[-len(suffix):].lower() == suffix.lower():
                return {"address": address, "privKey": priv_key}

# Function to manage the generation of vanity addresses with threads
def generate_vanity_addresses(prefix, suffix, case_sensitive=False):
    print(f"Starting to generate vanity addresses with prefix '{prefix}' and suffix '{suffix}' using multiple threads...")
    # Limit the number of threads to half of the available logical processors
    num_cores = 10  # Using half of the 20 logical processors
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_cores) as executor:
        futures = [executor.submit(generate_vanity_address, prefix, suffix, case_sensitive) for _ in range(num_cores)]

        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result:
                print(f"Vanity address generated: {result['address']}")
                save_vanity_wallet(result)
                play_success_sound()
                executor.shutdown(wait=False)
                break

# Function to save the generated vanity address and private key to a file
def save_vanity_wallet(vanity_wallet):
    vanity_filename = f"{vanity_folder}/{vanity_wallet['address']}.txt"
    with open(vanity_filename, 'w') as f:
        f.write(f"Vanity Address: {vanity_wallet['address']}\n")
        f.write(f"Private Key: {vanity_wallet['privKey']}\n")
    
    print(f"Successfully saved vanity wallet to '{vanity_filename}'")

# Function to play success sound
def play_success_sound():
    # This plays a .wav sound, "chaching.wav"
    try:
        winsound.PlaySound("chaching.wav", winsound.SND_FILENAME)
        print("Cha-ching! Sound played.")
    except Exception as e:
        print(f"Error playing sound: {e}")

# Function to repeat the process
def repeat_process():
    while True:
        # Get user input for the prefix and suffix
        prefix = input("Enter the first two digits after 0x (prefix): ")
        suffix = input("Enter the last three digits of the address (suffix): ")

        # Validate input
        if len(prefix) != 2 or len(suffix) != 3:
            print("The prefix must be exactly two characters and the suffix must be exactly three characters.")
            continue

        # Option for case sensitivity
        case_sensitive_input = input("Should the address check be case-sensitive? (y/n): ").lower()
        case_sensitive = case_sensitive_input == 'y'

        generate_vanity_addresses(prefix, suffix, case_sensitive)

        # Ask if the user wants to generate more addresses
        another_round = input("Do you want to generate another vanity address? (y/n): ").lower()
        if another_round != 'y':
            print("Exiting the program.")
            break

# Main function
def main():
    # Print ASCII art
    print_ascii_art()

    # Start the process
    repeat_process()

# Start the program
if __name__ == "__main__":
    main()
