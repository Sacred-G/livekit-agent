"""
Domain 2: Threats, Vulnerabilities, and Mitigations
=====================================================
Weight: 22% of exam
Official CompTIA Security+ SY0-701
"""

DOMAIN_2_KNOWLEDGE = {
    "name": "Threats, Vulnerabilities, and Mitigations",
    "weight": "22%",
    "topics": {
        "threat_actors": {
            "description": "Common threat actors and their motivations",
            "actor_types": [
                "Nation-state - Government-sponsored attackers with vast resources",
                "Unskilled Attacker - Script kiddies using existing tools",
                "Hacktivist - Ideologically motivated attackers",
                "Insider Threat - Employees or contractors with access",
                "Organized Crime - Criminal groups seeking financial gain",
                "Shadow IT - Unauthorized technology use within organization",
            ],
            "attributes": [
                "Internal vs External - Location relative to organization",
                "Resources/Funding - Financial backing and capabilities",
                "Level of Sophistication - Technical skill and knowledge",
            ],
            "motivations": [
                "Data Exfiltration - Stealing sensitive information",
                "Espionage - Intelligence gathering",
                "Service Disruption - Causing downtime or damage",
                "Blackmail - Extortion and threats",
                "Financial Gain - Direct monetary benefit",
                "Philosophical/Political - Ideological reasons",
                "Ethical - White hat security research",
                "Revenge - Retaliation or payback",
                "Chaos - Disruption for its own sake",
                "War - Cyber warfare operations",
            ],
            "key_points": [
                "Threat actors vary greatly in capability and intent",
                "Understanding motivation helps predict behavior",
                "Insider threats are particularly dangerous",
            ],
        },
        "threat_vectors": {
            "description": "Common threat vectors and attack surfaces",
            "message_based": [
                "Email - Phishing and malware delivery",
                "SMS - Smishing attacks",
                "Instant Messaging - Social engineering via IM",
            ],
            "file_based": [
                "Image-based - Malware hidden in images",
                "File-based - Infected documents or executables",
            ],
            "voice_and_physical": [
                "Voice Call - Vishing (voice phishing)",
                "Removable Devices - USB drives with malware",
            ],
            "network_vectors": [
                "Wireless Networks - Unsecured Wi-Fi",
                "Wired Networks - Physical network access",
                "Bluetooth - Short-range wireless attacks",
                "Open Ports - Exposed services",
            ],
            "vulnerable_software": [
                "Client-based - Vulnerable applications",
                "Agentless - Systems without security agents",
                "Unsupported Systems - End-of-life software",
            ],
            "supply_chain": [
                "Managed Service Providers (MSP) - Third-party IT services",
                "Vendors - Hardware/software suppliers",
                "Suppliers - Component manufacturers",
            ],
            "default_credentials": [
                "Default Passwords - Unchanged factory settings",
                "Default Accounts - Unmodified user accounts",
            ],
            "key_points": [
                "Attack surface is all possible entry points",
                "Multiple vectors increase attack opportunities",
                "Supply chain attacks affect many organizations",
            ],
        },
        "social_engineering": {
            "description": "Social engineering tactics and techniques",
            "phishing_variants": [
                "Phishing - Mass fraudulent emails",
                "Spear Phishing - Targeted attacks on specific individuals",
                "Whaling - Targeting high-level executives",
                "Vishing - Voice phishing via phone calls",
                "Smishing - SMS-based phishing",
            ],
            "manipulation_tactics": [
                "Impersonation - Pretending to be someone else",
                "Business Email Compromise (BEC) - Compromised executive emails",
                "Pretexting - Creating false scenarios",
                "Watering Hole - Compromising frequently visited sites",
                "Brand Impersonation - Fake company communications",
                "Typosquatting - Registering similar domain names",
            ],
            "key_points": [
                "Exploits human psychology, not technical vulnerabilities",
                "User awareness training is primary defense",
                "Always verify unusual requests",
            ],
        },
        "vulnerabilities": {
            "description": "Types of vulnerabilities in systems and applications",
            "application_vulnerabilities": [
                "Memory Injection - Inserting code into memory",
                "Buffer Overflow - Exceeding memory boundaries",
                "Race Conditions - Timing-dependent flaws",
                "Time-of-Check/Time-of-Use (TOC/TOU) - State changes between checks",
                "Malicious Update - Compromised software updates",
            ],
            "system_vulnerabilities": [
                "Operating System-based - OS-level vulnerabilities",
                "Web-based - Web application flaws",
                "Hardware Vulnerabilities - Firmware and chip flaws",
                "Virtualization - Hypervisor and VM escape issues",
                "Cloud-specific - Multi-tenancy and misconfiguration",
                "Mobile Device - Smartphone and tablet vulnerabilities",
            ],
            "other_vulnerabilities": [
                "Supply Chain - Compromised components or software",
                "Cryptographic - Weak or broken encryption",
                "Misconfiguration - Improperly configured systems",
                "Zero-day - Unknown vulnerabilities without patches",
            ],
            "key_points": [
                "All software has potential vulnerabilities",
                "Zero-day exploits are most dangerous",
                "Regular patching reduces risk",
            ],
        },
        "malicious_activity": {
            "description": "Indicators of malicious activity and attacks",
            "malware_types": [
                "Ransomware - Encrypts data and demands payment",
                "Trojan - Disguised malicious software",
                "Worm - Self-replicating malware",
                "Spyware - Secretly monitors user activity",
                "Bloatware - Unwanted pre-installed software",
                "Virus - Attaches to files and spreads",
                "Keylogger - Records keyboard input",
                "Logic Bomb - Triggered malicious code",
                "Rootkit - Hides malware at system level",
            ],
            "physical_attacks": [
                "Brute Force - Exhaustive password attempts",
                "RFID Cloning - Copying access badges",
                "Environmental - Temperature, humidity attacks",
            ],
            "network_attacks": [
                "DDoS - Distributed Denial of Service",
                "Amplified/Reflected DDoS - Using third parties to amplify",
                "DNS Attacks - DNS poisoning or hijacking",
                "Wireless Attacks - Evil twin, deauth, WPS attacks",
                "On-path Attack - Man-in-the-middle interception",
                "Credential Replay - Reusing captured credentials",
                "Malicious Code - Drive-by downloads, code injection",
            ],
            "application_attacks": [
                "Injection Attacks - SQL, LDAP, XML injection",
                "Buffer Overflow - Memory corruption",
                "Replay Attacks - Resending captured data",
                "Privilege Escalation - Gaining higher access",
                "Forgery - CSRF, request forgery",
                "Directory Traversal - Accessing unauthorized directories",
            ],
            "cryptographic_attacks": [
                "Downgrade Attack - Forcing weaker encryption",
                "Collision Attack - Finding hash collisions",
                "Birthday Attack - Exploiting probability in hashing",
            ],
            "password_attacks": [
                "Password Spraying - Trying common passwords across accounts",
                "Brute Force - Trying all possible combinations",
            ],
            "indicators": [
                "Account Lockout - Multiple failed login attempts",
                "Concurrent Session Usage - Same account, multiple locations",
                "Blocked Content - Unusual traffic patterns",
                "Impossible Travel - Logins from distant locations quickly",
                "Resource Consumption - Unusual CPU/memory/bandwidth usage",
                "Missing Logs - Evidence of tampering",
            ],
            "key_points": [
                "Multiple indicators together signal compromise",
                "Behavioral analysis detects anomalies",
                "Log monitoring is essential for detection",
            ],
        },
        "mitigation_techniques": {
            "description": "Techniques to mitigate threats and vulnerabilities",
            "network_controls": [
                "Segmentation - Dividing network into zones",
                "Access Control - Restricting resource access",
                "Isolation - Separating critical systems",
            ],
            "application_controls": [
                "Application Allow List - Only approved apps run",
                "Input Validation - Checking user input",
            ],
            "system_hardening": [
                "Endpoint Protection - Antivirus, EDR, XDR",
                "Host-based Firewall - System-level filtering",
                "Host-based IPS (HIPS) - System intrusion prevention",
                "Disabling Ports/Protocols - Reduce attack surface",
                "Default Password Changes - Remove factory credentials",
                "Removal of Unnecessary Software - Minimize installed programs",
            ],
            "operational_controls": [
                "Patching - Regular security updates",
                "Encryption - Protecting data confidentiality",
                "Monitoring - Continuous surveillance",
                "Least Privilege - Minimum necessary access",
            ],
            "key_points": [
                "Defense in depth uses multiple mitigations",
                "Patching is critical for known vulnerabilities",
                "Least privilege limits damage from compromise",
            ],
        },
    },
}