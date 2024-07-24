# Brainwave Tasks

## Task 1 : Password-Strength-Checker

**Objective** : 
- Develop a tool to assess the strength of passwords entered by users. Implement algorithms to analyze factors such as length, complexity, and uniqueness to provide feedback on password strength.

**Details** : 
- What is the basic length and complexity of password ?  
  - Minimum 8 Characters Long ?  ( CHECK IF THE LENGTH OF STRING IS GREATER THAN 8 ? )
  - Should be Alpha-numeric with special character ?
	- One Upper Case [A-Z]   ( CHECK IF STRING CONTAINS ANY UPPER-CASE ?)
	- One Number [0-9]  ( CHECK IF STRING CONTAINS ANY NUMBER ? )
	- One Special-character [./+@#$!] so on. ( CHECK IF STRING CONTAINS ANY SPECIAL CHARACTERS ? )

## Task 2 : Phishing-Link-Scanner

**Objective** : 
- We need to scan the suspicious link. Suspicious link is a dangerous web page link, which can steal credentials (user/password) or download malwares.

**Details** : 
- Ask user to "Please enter the link you would like to scan ?" 
	- "www.malware.com"
- Scanning for the link : 
	- Go to https://www.virustotal.com/ page or URLScan.io page.
	- Enter the URL to scan "www.malware.com" 
	- Result if it's malicious or not.
- Response user that - "It's a PHISHING link"
