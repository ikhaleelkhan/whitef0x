import argparse
import concurrent.futures
import dns.resolver
import requests
import sys
import os

def get_subdomains(domain, wordlists):
    subdomains = set()
    for wordlist in wordlists:
        with open(wordlist, 'r') as f:
            for line in f:
                subdomain = line.strip() + '.' + domain
                subdomains.add(subdomain)
    return subdomains

def get_recursive_subdomains(domain, level, wordlists):
    if level == 0:
        return set()
    subdomains = get_subdomains(domain, wordlists)
    recursive_subdomains = set()
    for subdomain in subdomains:
        try:
            answers = dns.resolver.resolve(subdomain, 'A')
            for answer in answers:
                recursive_subdomains.add(subdomain)
                recursive_subdomains.update(get_recursive_subdomains(answer.address, level-1, wordlists))
        except:
            pass
    return recursive_subdomains

def scan_subdomain(subdomain, scan_opts):
    try:
        response = requests.get(scan_opts['proto'] + '://' + subdomain, timeout=scan_opts['timeout'])
        if response.status_code == 200:
            print(subdomain)
        if scan_opts['output']:
            with open(scan_opts['output'], 'a') as f:
                f.write(subdomain + '\n')
    except:
        pass

def main():
    parser = argparse.ArgumentParser(description='WhiteF0x Sub Domain Enumeration Tool')
    parser.add_argument('domain', type=str, help='the domain to scan')
    parser.add_argument('-w', '--wordlists', type=str, nargs='+', default=['subdomains.txt', 'common.txt'], help='the wordlists to use for subdomain enumeration')
    parser.add_argument('-r', '--recursive', type=int, default=0, help='the number of levels of recursive subdomain enumeration')
    parser.add_argument('-t', '--threads', type=int, default=10, help='the number of threads to use for scanning')
    parser.add_argument('-p', '--proto', type=str, default='http', help='the protocol to use for scanning (http or https)')
    parser.add_argument('-o', '--output', type=str, default=None, help='the file to output results to')
    parser.add_argument('--timeout', type=int, default=5, help='the timeout in seconds for each HTTP request')
    args = parser.parse_args()

    if args.recursive > 0:
        subdomains = get_recursive_subdomains(args.domain, args.recursive, args.wordlists)
    else:
        subdomains = get_subdomains(args.domain, args.wordlists)

    scan_opts = {
        'proto': args.proto,
        'timeout': args.timeout,
        'output': args.output,
    }

    with concurrent.futures.ThreadPoolExecutor(max_workers=args.threads) as executor:
        executor.map(scan_subdomain, subdomains, [scan_opts]*len(subdomains))

if __name__ == '__main__':
    main()
