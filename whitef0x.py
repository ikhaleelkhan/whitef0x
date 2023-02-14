#!/usr/bin/env python3

import argparse
import dns.resolver
import socket
import sys


def get_subdomains(domain, wordlists):
    for wordlist in wordlists:
        with open(wordlist, 'r') as f:
            for line in f:
                subdomain = line.strip()
                if subdomain == "":
                    continue
                yield f"{subdomain}.{domain}"


def get_recursive_subdomains(domain, recursive, wordlists):
    subdomains = set()
    processed_subdomains = set()
    subdomains.update(get_subdomains(domain, wordlists))
    processed_subdomains.add(domain)
    while recursive and len(subdomains) > 0:
        subdomain = subdomains.pop()
        if subdomain in processed_subdomains:
            continue
        processed_subdomains.add(subdomain)
        try:
            answers = dns.resolver.query(subdomain, 'A')
            for rdata in answers:
                ip = rdata.address
                subdomains.add((subdomain, ip))
        except:
            pass
    return subdomains


def main():
    parser = argparse.ArgumentParser(description="WhiteF0x - Sub Domain Enumeration Tool")
    parser.add_argument("domain", help="The domain to enumerate subdomains for")
    parser.add_argument("-r", "--recursive", help="Enable recursive subdomain enumeration", action="store_true")
    parser.add_argument("-w", "--wordlists", help="Comma-separated list of wordlists to use", default="wordlists/common.txt")
    parser.add_argument("-v", "--verbose", help="Enable verbose output", action="store_true")
    args = parser.parse_args()

    wordlists = args.wordlists.split(",")
    subdomains = get_recursive_subdomains(args.domain, args.recursive, wordlists)
    for subdomain, ip in subdomains:
        print(f"{subdomain}\t{ip}")
    if args.verbose:
        print(f"Found {len(subdomains)} subdomains.")


if __name__ == "__main__":
    main()
