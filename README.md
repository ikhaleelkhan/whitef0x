# WhiteF0x - Sub Domain Enumeration Tool
WhiteF0x is a powerful sub domain enumeration tool that allows you to quickly and easily scan a domain for subdomains using customizable wordlists, multithreaded scanning, and recursive enumeration.

Features
Fast and efficient scanning of subdomains using customizable wordlists
Recursive enumeration for up to a specified number of levels
Multithreaded scanning for faster results
Support for both HTTP and HTTPS protocols
Customizable timeout for each HTTP request
Output results to a file

Usage
To use WhiteF0x, simply run the script with the desired options. 

For example:

``python whitef0x.py example.com -w subdomains.txt common.txt -r 2 -t 20 -p https -o results.txt --timeout 10``

This command would scan the domain 'example.com' using the wordlists 'subdomains.txt' and 'common.txt' for up to 2 levels of recursive subdomain enumeration, with 20 threads and the HTTPS protocol. The results of the scan would be saved to a file called 'results.txt', with a timeout of 10 seconds for each HTTP request.

# Installation
To install WhiteF0x, simply clone the repository and install the required dependencies:

``git clone https://github.com/ikhaleelkhan/whitef0x.git``

``cd whitef0x``

``pip install -r requirements.txt``

# Contributing
If you find a bug or have a feature request, please open an issue or submit a pull request. Contributions are always welcome!

# License
WhiteF0x is licensed under the MIT License. See the LICENSE file for more information.


