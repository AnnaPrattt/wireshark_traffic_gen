![header.jpg](header.jpg)
<br>
This **Wireshark Traffic Generation** script automatatically generates network traffic to be analyzed in Wireshark. This tool was designed to give junior security professionals experience analyzing traffic in the tool.

# Requirements
* python3
* dependent libraries `requests`, `dnspyton`, and `pythonping`
* local user rights (admin privileges not required)

# Usage
Intial configuration:
```bash
git clone <insert link>
pip3 install -r requirements.txt
python3 generator.py
```

Users should start their Wireshark capture FIRST and then run the generator.py script.

Questions corresponding to the traffic generated are in this repository, located at ./questions/. Two files are included:
* questions_NO_ANSWERS.md
* questions_WITH_ANSWERS.md

The answer key also provides intended learning outcomes for each question.

# Features
The traffic generator currently generates these traffic types:
* HTTP
* HTTPS
* ICMP
* DNS

Distracting traffic is also generated to add obfuscate the "target" traffic that answers the practice questions.

# Errors
If traffic for a specific question cannot be generated, a message will be printed to the console: `"Unable to generate QUESTION ##."`.<br> If a user recieve these errors, they should not spent time trying to answer that question.

# User Modifications
This script intentionally does NOT use variables. Users wishing to make modifications to the script should edit the script directly. 

# Future Work
* Add server-dependent network traffic (SSH, FTP, etc.) -- deploy servers on the client with local containers?