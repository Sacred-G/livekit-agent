"""
Security+ Practice Questions
=============================
Practice quiz questions for CompTIA Security+ (SY0-701) exam.

NOTE: The main knowledge base has been moved to the 'domains' package.
This file now contains practice questions organized by domain for targeted quizzing.

Features:
- DOMAIN_PRACTICE_QUESTIONS: Questions organized by Security+ domain (1-5)
- PRACTICE_QUESTIONS: All questions flattened for general quizzes
- Domain-specific quizzing allows focused practice on particular exam areas

Usage:
- Use quiz_domain(domain, num_questions) for targeted practice
- Use quiz_me(num_questions) for random questions from all domains
- Use list_quiz_domains() to see available domains and question counts
"""

# The comprehensive knowledge base is now in: domains/domain_1/knowledge.py through domain_5/knowledge.py
# Agent imports ALL_DOMAINS from domains package instead of using this file's old KNOWLEDGE_BASE

# Domain-specific practice questions for targeted quizzing
DOMAIN_PRACTICE_QUESTIONS = {
    "domain_1": [
        {
            "question": "Which malware can replicate without user interaction?",
            "options": ["A) Virus", "B) Worm", "C) Trojan", "D) Rootkit"],
            "correct": "B",
            "explanation": "Worms self-replicate and spread across networks without user action.",
        },
        {
            "question": "What does CIA Triad stand for?",
            "options": [
                "A) Confidentiality, Integrity, Availability",
                "B) Control, Identity, Access",
                "C) Cryptography, Identification, Authentication",
                "D) Compliance, Investigation, Analysis",
            ],
            "correct": "A",
            "explanation": "The CIA Triad is Confidentiality, Integrity, Availability.",
        },
        {
            "question": "Which type of attack involves sending falsified emails to appear legitimate?",
            "options": ["A) Phishing", "B) Vishing", "C) Smishing", "D) Spoofing"],
            "correct": "A",
            "explanation": "Phishing uses email to trick users into revealing sensitive information.",
        },
        {
            "question": "What is the primary purpose of a firewall?",
            "options": [
                "A) Encrypt data", 
                "B) Filter network traffic", 
                "C) Detect malware", 
                "D) Backup data"
            ],
            "correct": "B",
            "explanation": "Firewalls filter and control network traffic based on security rules.",
        },
        {
            "question": "Which authentication factor is something you ARE?",
            "options": ["A) Password", "B) Token", "C) Fingerprint", "D) PIN"],
            "correct": "C",
            "explanation": "Biometric factors like fingerprints are something you ARE (Type 2).",
        },
        {
            "question": "What type of malware encrypts files and demands payment?",
            "options": ["A) Ransomware", "B) Spyware", "C) Adware", "D) Logic bomb"],
            "correct": "A",
            "explanation": "Ransomware encrypts victim's files and demands payment for decryption.",
        },
        {
            "question": "Which attack involves intercepting communication between two parties?",
            "options": ["A) Man-in-the-middle", "B) DoS", "C) SQL injection", "D) Cross-site scripting"],
            "correct": "A",
            "explanation": "Man-in-the-middle attacks intercept and potentially alter communications.",
        },
        {
            "question": "What is the purpose of a DMZ network?",
            "options": [
                "A) Separate internal network from external threats",
                "B) Encrypt all traffic",
                "C) Store sensitive data",
                "D) Monitor user activity"
            ],
            "correct": "A",
            "explanation": "A DMZ provides a buffer zone between trusted internal networks and untrusted external networks.",
        },
        {
            "question": "Which type of firewall operates at the transport layer?",
            "options": ["A) Stateful inspection", "B) Packet filtering", "C) Proxy", "D) Next-generation"],
            "correct": "A",
            "explanation": "Stateful inspection firewalls operate at the transport layer and track connection states.",
        },
        {
            "question": "What is social engineering?",
            "options": [
                "A) Manipulating people to divulge information",
                "B) Hacking software systems",
                "C) Breaking encryption",
                "D) Scanning network ports"
            ],
            "correct": "A",
            "explanation": "Social engineering exploits human psychology to gain confidential information.",
        },
        {
            "question": "Which protocol is considered insecure for remote access?",
            "options": ["A) Telnet", "B) SSH", "C) HTTPS", "D) SFTP"],
            "correct": "A",
            "explanation": "Telnet transmits data in plaintext, making it insecure for remote access.",
        },
        {
            "question": "What is a zero-day vulnerability?",
            "options": [
                "A) Unknown vulnerability with no available patch",
                "B) Virus that activates on January 1st",
                "C) Exploit that requires zero user interaction",
                "D) Security flaw in new software releases"
            ],
            "correct": "A",
            "explanation": "Zero-day vulnerabilities are unknown to the vendor and have no available patches.",
        },
        {
            "question": "Which device operates at Layer 2 of the OSI model?",
            "options": ["A) Switch", "B) Router", "C) Firewall", "D) Load balancer"],
            "correct": "A",
            "explanation": "Switches operate at Layer 2 (Data Link layer) of the OSI model.",
        },
        {
            "question": "What is the primary purpose of penetration testing?",
            "options": [
                "A) Identify security vulnerabilities",
                "B) Monitor network traffic",
                "C) Encrypt sensitive data",
                "D) Backup critical systems"
            ],
            "correct": "A",
            "explanation": "Penetration testing simulates attacks to identify security weaknesses.",
        },
        {
            "question": "Which type of authentication uses something you KNOW?",
            "options": ["A) Password", "B) Fingerprint", "C) Smart card", "D) Retina scan"],
            "correct": "A",
            "explanation": "Passwords, PINs, and security questions are knowledge factors (something you know).",
        },
    ],
    "domain_2": [
        {
            "question": "Which encryption uses the same key for encrypt/decrypt?",
            "options": ["A) Asymmetric", "B) Symmetric", "C) Hashing", "D) Public Key"],
            "correct": "B",
            "explanation": "Symmetric encryption uses one shared key.",
        },
        {
            "question": "What is the purpose of a certificate authority (CA)?",
            "options": [
                "A) Issue digital certificates",
                "B) Encrypt email",
                "C) Block malware",
                "D) Monitor network traffic"
            ],
            "correct": "A",
            "explanation": "CAs issue and verify digital certificates for public key infrastructure.",
        },
        {
            "question": "Which hashing algorithm is considered insecure?",
            "options": ["A) SHA-256", "B) SHA-512", "C) MD5", "D) bcrypt"],
            "correct": "C",
            "explanation": "MD5 has known vulnerabilities and is considered insecure for cryptographic purposes.",
        },
        {
            "question": "What does PKI stand for?",
            "options": [
                "A) Public Key Infrastructure",
                "B) Private Key Initiative",
                "C) Password Key Interface",
                "D) Protected Key Identification"
            ],
            "correct": "A",
            "explanation": "PKI is Public Key Infrastructure, used for managing digital certificates.",
        },
        {
            "question": "Which protocol is used for secure web browsing?",
            "options": ["A) HTTP", "B) FTP", "C) HTTPS", "D) Telnet"],
            "correct": "C",
            "explanation": "HTTPS uses SSL/TLS to encrypt web traffic.",
        },
        {
            "question": "What is the primary purpose of salting in password hashing?",
            "options": [
                "A) Prevent rainbow table attacks",
                "B) Speed up hashing",
                "C) Reduce storage requirements",
                "D) Simplify password recovery"
            ],
            "correct": "A",
            "explanation": "Salting adds random data to passwords before hashing to prevent rainbow table attacks.",
        },
        {
            "question": "Which symmetric encryption algorithm is commonly used?",
            "options": ["A) AES", "B) RSA", "C) ECC", "D) DSA"],
            "correct": "A",
            "explanation": "AES (Advanced Encryption Standard) is widely used symmetric encryption.",
        },
        {
            "question": "What is a digital signature used for?",
            "options": [
                "A) Verify authenticity and integrity",
                "B) Encrypt data",
                "C) Compress files",
                "D) Hide information"
            ],
            "correct": "A",
            "explanation": "Digital signatures verify the authenticity and integrity of digital messages.",
        },
        {
            "question": "Which key exchange protocol provides forward secrecy?",
            "options": ["A) Diffie-Hellman", "B) RSA", "C) AES", "D) MD5"],
            "correct": "A",
            "explanation": "Diffie-Hellman provides forward secrecy, meaning past sessions remain secure even if keys are compromised.",
        },
        {
            "question": "What is the purpose of a certificate revocation list (CRL)?",
            "options": [
                "A) List revoked certificates",
                "B) Issue new certificates",
                "C) Encrypt communications",
                "D) Store private keys"
            ],
            "correct": "A",
            "explanation": "CRLs contain serial numbers of certificates that have been revoked before expiration.",
        },
        {
            "question": "Which encryption mode requires each block to be encrypted sequentially?",
            "options": ["A) CBC", "B) ECB", "C) CTR", "D) GCM"],
            "correct": "A",
            "explanation": "CBC (Cipher Block Chaining) requires each block to be encrypted sequentially using the previous block's ciphertext.",
        },
        {
            "question": "What is steganography?",
            "options": [
                "A) Hiding data within other data",
                "B) Encrypting data with keys",
                "C) Compressing data",
                "D) Transferring data securely"
            ],
            "correct": "A",
            "explanation": "Steganography conceals messages within other non-secret data or media.",
        },
        {
            "question": "Which algorithm is used for asymmetric encryption?",
            "options": ["A) RSA", "B) AES", "C) DES", "D) 3DES"],
            "correct": "A",
            "explanation": "RSA is a widely used asymmetric encryption algorithm for secure data transmission.",
        },
        {
            "question": "What is the purpose of a nonce in cryptography?",
            "options": [
                "A) Ensure uniqueness in cryptographic operations",
                "B) Encrypt data",
                "C) Hash passwords",
                "D) Sign documents"
            ],
            "correct": "A",
            "explanation": "A nonce (number used once) ensures replay attacks cannot succeed.",
        },
        {
            "question": "Which protocol provides secure email transmission?",
            "options": ["A) S/MIME", "B) SMTP", "C) POP3", "D) IMAP"],
            "correct": "A",
            "explanation": "S/MIME (Secure/Multipurpose Internet Mail Extensions) provides secure email transmission.",
        },
    ],
    "domain_3": [
        {
            "question": "What is the primary goal of identity and access management (IAM)?",
            "options": [
                "A) Manage user identities and control access",
                "B) Encrypt all data",
                "C) Monitor network traffic",
                "D) Backup systems"
            ],
            "correct": "A",
            "explanation": "IAM manages digital identities and controls user access to resources.",
        },
        {
            "question": "Which authentication method requires two or more factors?",
            "options": ["A) Single-factor", "B) Multi-factor", "C) Biometric", "D) Token-based"],
            "correct": "B",
            "explanation": "Multi-factor authentication requires two or more different types of authentication.",
        },
        {
            "question": "What is the principle of least privilege?",
            "options": [
                "A) Give users maximum access",
                "B) Give users only necessary access",
                "C) No access for anyone",
                "D) Same access for all users"
            ],
            "correct": "B",
            "explanation": "Least privilege means users only get the minimum access required for their job.",
        },
        {
            "question": "Which account type should be disabled when not needed?",
            "options": ["A) User", "B) Admin", "C) Guest", "D) Service"],
            "correct": "C",
            "explanation": "Guest accounts should be disabled when not in use to reduce security risks.",
        },
        {
            "question": "What is the purpose of account lockout policies?",
            "options": [
                "A) Prevent password guessing",
                "B) Force password changes",
                "C) Log user activity",
                "D) Encrypt passwords"
            ],
            "correct": "A",
            "explanation": "Account lockout prevents brute force attacks by limiting failed login attempts.",
        },
        {
            "question": "Which protocol provides centralized authentication?",
            "options": ["A) LDAP", "B) HTTP", "C) FTP", "D) SMTP"],
            "correct": "A",
            "explanation": "LDAP (Lightweight Directory Access Protocol) provides centralized authentication services.",
        },
        {
            "question": "What is the purpose of role-based access control (RBAC)?",
            "options": [
                "A) Assign permissions based on job roles",
                "B) Encrypt user data",
                "C) Monitor network traffic",
                "D) Backup user accounts"
            ],
            "correct": "A",
            "explanation": "RBAC assigns permissions to users based on their job roles within an organization.",
        },
        {
            "question": "Which authentication factor is something you HAVE?",
            "options": ["A) Password", "B) Token", "C) Fingerprint", "D) Voice pattern"],
            "correct": "B",
            "explanation": "Tokens, smart cards, and keys are possession factors (something you have).",
        },
        {
            "question": "What is the purpose of password complexity requirements?",
            "options": [
                "A) Make passwords harder to guess",
                "B) Speed up login process",
                "C) Reduce storage needs",
                "D) Simplify password recovery"
            ],
            "correct": "A",
            "explanation": "Password complexity requirements make passwords more resistant to guessing and cracking attacks.",
        },
        {
            "question": "Which technology provides single sign-on (SSO) capability?",
            "options": ["A) SAML", "B) SSL", "C) SSH", "D) SMTP"],
            "correct": "A",
            "explanation": "SAML (Security Assertion Markup Language) enables single sign-on across different systems.",
        },
        {
            "question": "What is the primary purpose of an identity provider (IdP)?",
            "options": [
                "A) Authenticate users and provide identity information",
                "B) Store application data",
                "C) Monitor network traffic",
                "D) Encrypt communications"
            ],
            "correct": "A",
            "explanation": "Identity providers authenticate users and manage identity information for SSO systems.",
        },
        {
            "question": "Which type of attack tries to gain access by using default credentials?",
            "options": ["A) Default credential attack", "B) Phishing", "C) Man-in-the-middle", "D) DoS"],
            "correct": "A",
            "explanation": "Default credential attacks exploit unchanged default usernames and passwords.",
        },
        {
            "question": "What is the purpose of just-in-time (JIT) access?",
            "options": [
                "A) Grant temporary access when needed",
                "B) Provide permanent admin rights",
                "C) Encrypt all data",
                "D) Monitor user activity"
            ],
            "correct": "A",
            "explanation": "JIT access provides temporary permissions that are automatically revoked after use.",
        },
        {
            "question": "Which protocol is used for secure remote authentication?",
            "options": ["A) RADIUS", "B) HTTP", "C) FTP", "D) Telnet"],
            "correct": "A",
            "explanation": "RADIUS provides centralized authentication, authorization, and accounting for network access.",
        },
        {
            "question": "What is the purpose of privileged access management (PAM)?",
            "options": [
                "A) Control and monitor privileged accounts",
                "B) Encrypt all user data",
                "C) Backup critical systems",
                "D) Monitor network traffic"
            ],
            "correct": "A",
            "explanation": "PAM systems control, monitor, and audit privileged access to critical resources.",
        },
    ],
    "domain_4": [
        {
            "question": "What type of testing involves simulating an attack?",
            "options": ["A) Penetration testing", "B) Vulnerability scanning", "C) Code review", "D) Risk assessment"],
            "correct": "A",
            "explanation": "Penetration testing simulates real attacks to identify security weaknesses.",
        },
        {
            "question": "Which log type records user access to resources?",
            "options": ["A) Access logs", "B) Error logs", "C) System logs", "D) Debug logs"],
            "correct": "A",
            "explanation": "Access logs record who accessed what resources and when.",
        },
        {
            "question": "What is the purpose of SIEM systems?",
            "options": [
                "A) Collect and analyze log data",
                "B) Encrypt network traffic",
                "C) Manage user accounts",
                "D) Backup data"
            ],
            "correct": "A",
            "explanation": "SIEM systems collect, correlate, and analyze security event data from multiple sources.",
        },
        {
            "question": "Which scanning method identifies open ports and services?",
            "options": ["A) Port scanning", "B) Vulnerability scanning", "C) Network mapping", "D) Packet sniffing"],
            "correct": "A",
            "explanation": "Port scanning identifies open ports and the services running on them.",
        },
        {
            "question": "What is the first step in incident response?",
            "options": ["A) Preparation", "B) Detection", "C) Containment", "D) Recovery"],
            "correct": "A",
            "explanation": "Preparation is the first phase of incident response, establishing policies and tools.",
        },
        {
            "question": "Which tool is used for network protocol analysis?",
            "options": ["A) Wireshark", "B) Nmap", "C) Metasploit", "D) Burp Suite"],
            "correct": "A",
            "explanation": "Wireshark is a network protocol analyzer used for packet capture and analysis.",
        },
        {
            "question": "What is the purpose of a honeypot?",
            "options": [
                "A) Attract and detect attackers",
                "B) Encrypt sensitive data",
                "C) Monitor legitimate users",
                "D) Backup critical systems"
            ],
            "correct": "A",
            "explanation": "Honeypots are decoy systems designed to attract and detect attackers.",
        },
        {
            "question": "Which type of attack overwhelms a system with traffic?",
            "options": ["A) Denial of Service", "B) Phishing", "C) SQL injection", "D) Cross-site scripting"],
            "correct": "A",
            "explanation": "DoS attacks overwhelm systems with excessive traffic to make them unavailable.",
        },
        {
            "question": "What is the purpose of intrusion detection systems (IDS)?",
            "options": [
                "A) Monitor network for malicious activity",
                "B) Encrypt all traffic",
                "C) Manage user accounts",
                "D) Backup data"
            ],
            "correct": "A",
            "explanation": "IDS monitors network or system activities for malicious violations or policies.",
        },
        {
            "question": "Which phase of incident response involves stopping the spread?",
            "options": ["A) Containment", "B) Detection", "C) Eradication", "D) Recovery"],
            "correct": "A",
            "explanation": "Containment involves isolating affected systems to prevent further damage.",
        },
        {
            "question": "What is the purpose of security baselines?",
            "options": [
                "A) Establish minimum security standards",
                "B) Monitor network traffic",
                "C) Encrypt data",
                "D) Backup systems"
            ],
            "correct": "A",
            "explanation": "Security baselines define the minimum level of security required for systems.",
        },
        {
            "question": "Which tool is primarily used for vulnerability scanning?",
            "options": ["A) Nessus", "B) Wireshark", "C) Metasploit", "D) John the Ripper"],
            "correct": "A",
            "explanation": "Nessus is a widely used vulnerability scanner for identifying security weaknesses.",
        },
        {
            "question": "What is the purpose of security information and event management?",
            "options": [
                "A) Real-time monitoring and analysis",
                "B) Data encryption",
                "C) User authentication",
                "D) System backup"
            ],
            "correct": "A",
            "explanation": "SIEM provides real-time monitoring, correlation, and analysis of security events.",
        },
        {
            "question": "Which type of testing examines code without executing it?",
            "options": ["A) Static analysis", "B) Dynamic analysis", "C) Penetration testing", "D) Vulnerability scanning"],
            "correct": "A",
            "explanation": "Static analysis examines code for vulnerabilities without running it.",
        },
        {
            "question": "What is the purpose of security orchestration?",
            "options": [
                "A) Automate security tasks and workflows",
                "B) Encrypt all communications",
                "C) Monitor user activity",
                "D) Backup critical data"
            ],
            "correct": "A",
            "explanation": "Security orchestration automates and coordinates security tasks across multiple tools.",
        },
    ],
    "domain_5": [
        {
            "question": "Which law regulates healthcare data protection in the US?",
            "options": ["A) HIPAA", "B) GDPR", "C) SOX", "D) PCI DSS"],
            "correct": "A",
            "explanation": "HIPAA protects healthcare information and sets standards for its security.",
        },
        {
            "question": "What is the primary purpose of data classification?",
            "options": [
                "A) Organize data by sensitivity",
                "B) Encrypt all data",
                "C) Delete old data",
                "D) Backup data"
            ],
            "correct": "A",
            "explanation": "Data classification organizes information based on sensitivity and protection requirements.",
        },
        {
            "question": "Which regulation governs credit card data protection?",
            "options": ["A) PCI DSS", "B) HIPAA", "C) FERPA", "D) GLBA"],
            "correct": "A",
            "explanation": "PCI DSS sets standards for protecting credit card data.",
        },
        {
            "question": "What is the purpose of data retention policies?",
            "options": [
                "A) Define how long to keep data",
                "B) Encrypt sensitive data",
                "C) Monitor network traffic",
                "D) Block unauthorized access"
            ],
            "correct": "A",
            "explanation": "Data retention policies specify how long different types of data should be kept.",
        },
        {
            "question": "Which privacy regulation applies to EU citizens' data?",
            "options": ["A) GDPR", "B) HIPAA", "C) SOX", "D) FERPA"],
            "correct": "A",
            "explanation": "GDPR protects personal data of EU citizens and has global impact.",
        },
        {
            "question": "What is the primary goal of risk management?",
            "options": [
                "A) Identify and mitigate risks",
                "B) Eliminate all risks",
                "C) Ignore minor risks",
                "D) Transfer all risks"
            ],
            "correct": "A",
            "explanation": "Risk management aims to identify, assess, and mitigate risks to acceptable levels.",
        },
        {
            "question": "Which law regulates financial reporting and corporate governance?",
            "options": ["A) Sarbanes-Oxley Act", "B) HIPAA", "C) GDPR", "D) FERPA"],
            "correct": "A",
            "explanation": "SOX establishes requirements for financial reporting and internal controls.",
        },
        {
            "question": "What is the purpose of a business impact analysis (BIA)?",
            "options": [
                "A) Identify critical business functions",
                "B) Encrypt sensitive data",
                "C) Monitor network traffic",
                "D) Backup systems"
            ],
            "correct": "A",
            "explanation": "BIA identifies and prioritizes critical business functions and their dependencies.",
        },
        {
            "question": "Which type of risk involves financial loss?",
            "options": ["A) Financial risk", "B) Operational risk", "C) Strategic risk", "D) Compliance risk"],
            "correct": "A",
            "explanation": "Financial risk involves potential monetary losses from various sources.",
        },
        {
            "question": "What is the purpose of Acceptable Use Policies (AUP)?",
            "options": [
                "A) Define appropriate technology use",
                "B) Encrypt all communications",
                "C) Monitor user activity",
                "D) Backup critical data"
            ],
            "correct": "A",
            "explanation": "AUPs establish rules for acceptable use of organizational technology resources.",
        },
        {
            "question": "Which regulation protects student education records?",
            "options": ["A) FERPA", "B) HIPAA", "C) GDPR", "D) SOX"],
            "correct": "A",
            "explanation": "FERPA protects the privacy of student education records.",
        },
        {
            "question": "What is the purpose of due care in security?",
            "options": [
                "A) Implement appropriate security measures",
                "B) Guarantee complete security",
                "C) Monitor all activity",
                "D) Encrypt all data"
            ],
            "correct": "A",
            "explanation": "Due care involves taking responsible security measures to protect assets.",
        },
        {
            "question": "Which concept requires organizations to protect sensitive data?",
            "options": ["A) Due diligence", "B) Due care", "C) Risk acceptance", "D) Risk avoidance"],
            "correct": "A",
            "explanation": "Due diligence involves understanding and identifying risks before implementing controls.",
        },
        {
            "question": "What is the primary purpose of disaster recovery planning?",
            "options": [
                "A) Restore operations after disruption",
                "B) Prevent all disasters",
                "C) Monitor daily operations",
                "D) Encrypt data"
            ],
            "correct": "A",
            "explanation": "Disaster recovery planning focuses on restoring critical operations after disruptions.",
        },
        {
            "question": "Which law governs financial institutions' data protection?",
            "options": ["A) GLBA", "B) HIPAA", "C) FERPA", "D) SOX"],
            "correct": "A",
            "explanation": "GLBA (Gramm-Leach-Bliley Act) regulates how financial institutions handle customer data.",
        },
    ],
}

# Flatten all domain questions for general quizzes
PRACTICE_QUESTIONS = []
for domain_questions in DOMAIN_PRACTICE_QUESTIONS.values():
    PRACTICE_QUESTIONS.extend(domain_questions)