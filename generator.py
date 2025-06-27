#1 /user/bin/env python3

import requests
import dns.resolver
from pythonping import ping
import sys

# generate distracting traffic
# generate random HTTP traffic
def random_http_site(site):
    try:
        requests.get(site)
    except:
        print("Partially missing random HTTP traffic generation.")

random_http_site('http://http-password.badssl.com')
random_http_site('http://google.com/generate_204')
random_http_site('http://http-textarea.badssl.com')
random_http_site('http://captive.apple.com')
random_http_site('http://http.badssl.com')
random_http_site('http://httpbin.org/')
random_http_site('http://example.com')

#generate random HTTPS traffic
def random_https_site(site):
    try:
        requests.get(site)
    except:
        print("Partially missing random HTTPS traffic generation.")

random_https_site('https://en.wikipedia.org/wiki/Jane_Austen')
random_https_site('https://www.virustotal.com/gui/domain/www.thelegacy.de/relations')
random_https_site('https://www.parcjeandrapeau.com/en/circuit-gilles-villeneuve-multi-purpose-track-provelo-sports-training-montreal/')
random_https_site('https://www.walmart.com/search/?query=lawn+swimming+pools')
random_https_site('https://www.linkedin.com/feed/')
random_https_site('https://www.amazon.jobs/en/')
random_https_site('https://www.barnesandnoble.com/')
random_https_site('https://www.crowdstrike.com/en-us/')

#generate random DNS traffic
def random_dns(domain, method):
    try:
        res = dns.resolver.resolve(domain, method)
    except:
        print("Partially missing random DNS traffic generation.")

random_dns('dsu.edu', 'TXT')
random_dns('byu.edu', 'A')
random_dns('berkeley.edu', 'A')
random_dns('cmu.edu', 'A')
random_dns('stanford.edu', 'A')
random_dns('k-staterandomrandom.edu', 'A')

# question 01
q1headers = {'User-Agent': 'sxm-android/7.10.0 Amazon/KFTUWI Android/11'}
try:
    q1 = requests.get('https://insane-about-jane.blogspot.com/', headers = q1headers)
    q1 = requests.get('https://insane-about-jane.blogspot.com/p/quilted-hugs-quilt.html', headers = q1headers)
    q1.close()
except:
    print("Unable to generate QUESTION 1.")

# question 02 + question 03
try:
    q2 = requests.get('http://neverssl.com')
    q2.close()
except:
    print("Unable to generate QUESTION 2-3.")

# question 04 + question 05 + question 06
try:
    q4headers = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.4b) Gecko/20030516 Mozilla Firebird/0.6'}
    q4 = requests.get('http://httpforever.com/', headers = q4headers)
    q4.close()
except:
    print("Unable to generate QUESTION 4-6.")

# question 07
try:
    q7headers = {'User-Agent': 'Mozilla/5.0 (X11; U; Linux; nb-NO) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.2 (Change: 0 )'}
    q7 = requests.get('https://harvard.edu', headers = q7headers)
    q7 = requests.get('https://pll.harvard.edu/catalog/free', headers = q7headers)
    q7 = requests.get('https://college.harvard.edu/', headers = q7headers)
    q7 = requests.get('https://www.harvardonline.harvard.edu/', headers = q7headers)
    q7 = requests.get('https://hsph.harvard.edu/', headers = q7headers)
    q7 = requests.get('https://hls.harvard.edu/', headers = q7headers)
    q7 = requests.get('https://dataverse.harvard.edu/', headers = q7headers)
    q7 = requests.get('https://www.hks.harvard.edu/', headers = q7headers)
    q7.close()
except:
    print("Unable to generate QUESTION 7.")

# question 08
try:
    q8headers = {'User-Agent':'WhatsApp/2.24.21.79 Android/14 Device/Xiaomi-22126RN91Y'}
    q8 = requests.get('http://www.faqs.org/faqs/', headers = q8headers)
    q8 = requests.get('http://www.faqs.org/terms.html', headers = q8headers)
    q8 = requests.get('http://www.faqs.org/popular/popular1.html', headers = q8headers)
    q8 = requests.get('http://www.faqs.org/popular/popular1.html', headers = q8headers)
    q8 = requests.get('http://www.faqs.org/popular/popular3.html', headers = q8headers)
    q8 = requests.get('http://www.faqs.org/popular/popular4.html', headers = q8headers)
    q8 = requests.get('http://www.faqs.org/topRated.html', headers = q8headers)
    q8 = requests.get('http://www.faqs.org/faqs/faqsearch.html', headers = q8headers)
    q8 = requests.get('http://www.faqs.org/contrib/', headers = q8headers)
    q8 = requests.get('http://www.faqs.org/docs/', headers = q8headers)
    q8 = requests.get('http://www.faqs.org/rfcs/', headers = q8headers)
    q8 = requests.get('http://www.faqs.org/rfcs/rfc-sidx13.html', headers = q8headers)
    q8 = requests.get('http://www.faqs.org/rfcs/rfc1208.html', headers = q8headers)
    q8 = requests.get('http://www.faqs.org/faqs/', headers = q8headers)
    q8 = requests.get('http://www.faqs.org/topRated.html', headers = q8headers)
    q8.close()
except:
    print("Unable to generate QUESTION 8.")

# question 09
try:
    q9headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 15; Pixel 7a Build/AP4A.250205.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/134.0.6998.39 Mobile Safari/537.36 Barcelona 371.0.0.37.110 Android (35/15; 420dpi; 1080x2400; Google/google; Pixel 7a; lynx'}
    q9 = requests.get('https://tls-v1-2.badssl.com:1012/', headers = q9headers)
    q9.close()
except:
    print("Unable to generate QUESTION 9.")

# question 10
try:
    q10headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.6796.73 Safari/537.36 OPR/114.0.5076.93'}
    q10 = requests.get('http://detectportal.firefox.com/success.txt', headers = q10headers)
    q10.close()
except:
    print("Unable to generate QUESTION 10.")

#  question 11
try:
    res = dns.resolver.resolve('espn.com', 'A')
except:
    print("Unable to generate QUESTION 11.")

# question 12
try:
    res = dns.resolver.resolve('mail.google.com', 'TXT')
except:
    print("Unable to generate QUESTION 12.")

# question 13
try:
    res = dns.resolver.Resolver()
    res.nameservers=['149.112.112.112']
    res.resolve('jcpenney.com')
except:
    print("Unable to generate QUESTION 13.")

# question 14
try:
    ping('8.8.8.8')
    ping('1.1.1.1')
    ping('8.8.8.12')
    ping('8.8.4.4')
    ping('8.8.8.15')
    ping('9.9.9.9')
    ping('8.8.8.27')
    ping('1.0.0.1')
    ping('8.8.8.35')
    ping('149.112.112.112')
    ping('8.8.8.107')
    ping('1.1.1.1')
    ping('8.8.8.237')
except:
    print("Unable to generate QUESTION 14.")

#question 15
try:
    ping('1.1.1.1', size = 64)
except:
    print("Unable to generate QUESTION 15")

sys.exit()

# sources
# https://stackoverflow.com/questions/10606133/sending-user-agent-using-requests-library-in-python
# https://explore.whatismybrowser.com/
# https://stackoverflow.com/questions/13842116/how-do-we-get-txt-cname-and-soa-records-from-dnspython
# https://www.geeksforgeeks.org/python/sending-dns-request-responses-with-python/
# https://stackoverflow.com/questions/3898363/set-specific-dns-server-using-dns-resolver-pythondns
# https://superuser.com/questions/1213116/are-there-well-known-http-only-sites