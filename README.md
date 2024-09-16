

# CREATOR

## Ethereum Vanity Address Generator

**CREATOR** is a multi-threaded tool designed to generate Ethereum addresses that match a specific prefix and/or suffix. The program allows you to specify the exact two-character prefix and three-character suffix and will generate valid Ethereum addresses that match those criteria. Additionally, the program plays a celebratory sound when it successfully generates a vanity address.

## Features
- **Multi-threaded execution**: Uses multiple CPU cores to generate vanity addresses faster.
- **Prefix and Suffix matching**: Specify the first two and last three characters of the address.
- **Cross-platform**: Works on Windows and other platforms.
- **Cha-ching sound**: Plays a sound on success (Windows only).
- **Continuous generation**: Prompts for a new prefix and suffix after every successful generation.

## Requirements
- **Python 3.x**
- Required Python libraries:
  - `eth-account`
  - `concurrent.futures`
  - `secrets` (part of the Python standard library)
  - `winsound` (for Windows) or `playsound` (for cross-platform sound)

## Installation

### Clone this repository:

```bash
git clone https://github.com/ToranagaOsaka/creator.git
```
### Install required dependencies:
```bash
pip install -r requirements.txt
```
For sound effects, ensure you have chaching.wav in the same directory as the script.

## Usage
Run the script:
``` bash
python creator.py
```
When prompted, enter the first two characters (prefix) after 0x and the last three characters (suffix) of the Ethereum address you want to generate.

Wait for the program to generate a matching vanity address. The process will terminate once a matching address is found and saved.

After a successful generation, you will be prompted to enter new prefix and suffix values, allowing for continuous address creation.

## Example
``` bash
$ python creator.py
Enter the first two digits after 0x (prefix): ab
Enter the last three digits of the address (suffix): 123

Starting to generate vanity addresses with prefix 'ab' and suffix '123' using multiple threads...
Vanity address generated: 0xab...123
Successfully saved vanity wallet to 'vanity_wallets/0xab...123.txt'
Cha-ching! Sound played.
```
### Bitcoin Donations: 1LEyTb6q2HXdqChQTx28eKvBpraPF34Vwc
