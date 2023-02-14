#!/usr/bin/env python3

import argparse
import dns.resolver
import os
import sys
import concurrent.futures
from termcolor import colored

BANNER = colored("""
 __      __    _      _______          _       
 \ \    / /   | |    |__   __|        | |      
  \ \  / /   _| |_ ___  | | ___   ___ | |_ ___ 
   \ \/ / | | | __/ _ \ | |/ _ \ / _ \| __/ __|
    \  /| |_| | ||  __/ | | (_) | (_) | |_\__ \\
     \/  \__,_|\__\___| |_|\___/ \___/ \__|___/
""", 'cyan')

def get_subdomains(domain, wordlists):
    subdomains = set()
    for wordlist in wordlists:
        with open(wordlist, 'r') as f:
            for line in f:
                subdomain = line.strip()
                if subdomain:
                    hostname = f"{subdomain}.{domain}"
                    subdomains.add(hostname)
    return subdomains

def get_recursive_subdomains(domain, recursive, wordlists):
    subdomains = set()
    if not recursive:
        subdomains.update(get_subdomains(domain, wordlists))
    else:
        subdomains_to_check = {domain}
        discovered_subdomains = set()
        while subdomains_to_check:
            subdomain = subdomains_to_check.pop()
            if subdomain not in discovered_subdomains:
                discovered_subdomains.add(subdomain)
                try:
                    answers = dns.resolver.resolve(subdomain, 'A')
                    for rdata in answers:
                        subdomains.add(subdomain)
                        print(colored(f"[+] Discovered subdomain: {subdomain}", 'green'))
                except:
                    pass
                subdomains_to_check.update(get_subdomains(subdomain, wordlists))
    return subdomains

def main():
    parser = argparse.ArgumentParser(description=BANNER)
    parser.add_argument('domain', help='The domain to enumerate subdomains for')
    parser.add_argument('-r', '--recursive', action='store_true', help='Recursively search for subdomains')
    parser.add_argument('-w', '--wordlists', default='common.txt', help='Comma-separated list of wordlists to use')
    parser.add_argument('-o', '--output', default='subdomains.txt', help='File to write output to')
    parser.add_argument('-t', '--threads', default=10, type=int, help='Number of threads to use for subdomain lookup')
    parser.add_argument('-v', '--verbose', action='store_true', help='Show verbose output')
    args = parser.parse_args()

    if args.verbose:
        print(colored(f"[i] Starting WhiteF0x with options: {args}", 'yellow'))

    wordlists = args.wordlists.split(',')
    subdomains = get_recursive_subdomains(args.domain, args.recursive, wordlists)

    with open(args.output, 'w') as f:
        for subdomain in subdomains:
            f.write(subdomain + '\n')
            if args.verbose:
                print(colored(f"[i] Writing subdomain to file: {subdomain}", 'yellow'))

    if args.verbose:
        print(colored(f"[i] Finished! Discovered {len(subdomains)} subdomains", 'yellow'))

if __name__ == '__main__':
    main()
