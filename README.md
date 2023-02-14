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

`python whitef0x.py example.com -w wordlists/common.txt,wordlists/custom.txt -r -v`

This will scan the example.com domain using the wordlists/common.txt and wordlists/custom.txt wordlist files, perform a recursive subdomain enumeration, and output verbose results. You can replace example.com with the domain you want to scan, and specify your own wordlist file(s) as needed.

Options
Here are the available command line options for WhiteF0x:

`usage: whitef0x.py [-h] [-w WORDLISTS] [-r] [-v] domain`

WhiteF0x Sub Domain Enumeration Tool

positional arguments:
  domain                Domain to scan

optional arguments:
  -h, --help            show this help message and exit
  -w WORDLISTS, --wordlists WORDLISTS
                        Path to wordlist file(s) (separated by comma). Default is "wordlists/common.txt".
  -r, --recursive       Recursive subdomain enumeration
  -v, --verbose         Verbose output

Examples
Here are some example commands for using WhiteF0x:

# Scan example.com using the default wordlist
`python whitef0x.py example.com`

# Scan example.com using a custom wordlist
`python whitef0x.py example.com -w custom_wordlist.txt`

# Perform a recursive scan of example.com using the default wordlist
`python whitef0x.py example.com -r`

# Output verbose results for example.com using the default wordlist
`python whitef0x.py example.com -v`



Contributing
Contributions to WhiteF0x are always welcome! If you find a bug or have an idea for a new feature, please open an issue or submit a pull request.

