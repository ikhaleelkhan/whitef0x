# WhiteF0x Sub Domain Enumeration Tool
WhiteF0x is a Python tool for enumerating subdomains of a given domain. It is designed to be a lightweight, fast, and easy-to-use alternative to other subdomain enumeration tools like Sublist3r and Subfinder.

Installation
WhiteF0x requires Python 3.x and the dnspython and argparse modules. You can install these dependencies using pip:

`pip install dnspython argparse`

To install WhiteF0x, simply clone the repository:1



`git clone https://github.com/ikhaleelkhan/whitef0x.git`

Usage
To use WhiteF0x, simply run the whitef0x.py script and specify the domain you want to scan. By default, the tool will use the wordlists/common.txt wordlist file, but you can specify your own wordlist(s) using the -w flag. If you want to perform a recursive subdomain enumeration, use the -r flag. To enable verbose output, use the -v flag.

Here's an example usage of WhiteF0x:

`python whitef0x.py example.com -w subdomains.txt common.txt -r 2 -t 20 -p https -o results.txt --timeout 10`




Contributing
Contributions to WhiteF0x are always welcome! If you find a bug or have an idea for a new feature, please open an issue or submit a pull request.

