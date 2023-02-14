import argparse
import requests
import dns.resolver
from tqdm import tqdm
from colorama import Fore, Style


def get_subdomains(domain, wordlist):
    subdomains = []
    with open(wordlist, 'r') as f:
        for line in f:
            subdomain = line.strip()
            url = f'http://{subdomain}.{domain}'
            try:
                requests.get(url)
            except requests.ConnectionError:
                pass
            else:
                print(Fore.GREEN + f'[+] Found subdomain: {url}' + Style.RESET_ALL)
                subdomains.append(url)
    return subdomains


def get_recursive_subdomains(domain, recursive, wordlists):
    subdomains = []
    if not recursive:
        return get_subdomains(domain, wordlists)
    else:
        subdomain_queue = list(get_subdomains(domain, wordlists))
        for subdomain in tqdm(subdomain_queue):
            try:
                answers = dns.resolver.resolve(subdomain, 'A')
            except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer):
                pass
            else:
                for rdata in answers:
                    ip = rdata.to_text()
                    print(Fore.BLUE + f'[+] Found IP address: {ip}' + Style.RESET_ALL)
                    new_subdomain = f'{ip}.in-addr.arpa'
                    if new_subdomain not in subdomain_queue and new_subdomain not in subdomains:
                        subdomain_queue.append(new_subdomain)
                        subdomains.append(new_subdomain)
        return subdomains


def main():
    parser = argparse.ArgumentParser(description='WhiteF0x Sub Domain Enumeration Tool')
    parser.add_argument('domain', help='target domain to enumerate subdomains for')
    parser.add_argument('-r', '--recursive', action='store_true', help='enable recursive subdomain enumeration')
    parser.add_argument('-w', '--wordlist', default='common.txt', help='specify a custom wordlist file')
    parser.add_argument('-v', '--verbose', action='store_true', help='enable verbose output')
    parser.add_argument('-vv', '--extra-verbose', action='store_true', help='enable extra verbose output')
    parser.add_argument('-o', '--output', help='specify an output file')
    args = parser.parse_args()

    if args.extra_verbose:
        print(Fore.YELLOW + '[+] Running in extra verbose mode' + Style.RESET_ALL)
    elif args.verbose:
