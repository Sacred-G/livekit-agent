"""
Domain 1: General Security Concepts
====================================
Weight: 12% of exam
Official CompTIA Security+ SY0-701
"""

DOMAIN_1_KNOWLEDGE = {
    "name": "General Security Concepts",
    "weight": "12%",
    "topics": {
        "security_controls": {
            "description": "Various types of security controls and their purposes",
            "categories": [
                "Technical - Implemented through technology (firewalls, encryption, antivirus)",
                "Managerial - Administrative controls (policies, procedures, risk assessments)",
                "Operational - Day-to-day operations (security awareness training, configuration management)",
                "Physical - Physical security measures (locks, guards, cameras)",
            ],
            "control_types": [
                "Preventive - Prevent security incidents before they occur",
                "Deterrent - Discourage potential attackers",
                "Detective - Identify security incidents when they occur",
                "Corrective - Fix problems after they've been detected",
                "Compensating - Alternative controls when primary controls aren't feasible",
                "Directive - Direct or guide actions (policies, procedures)",
            ],
            "key_points": [
                "Defense in depth uses multiple control types",
                "Controls work together for comprehensive security",
                "Select controls based on risk assessment",
            ],
            "scripted_lesson": """Let's be real, no prevention is ever perfect. So, what happens if an attacker gets past that first line? Well, that's where detective controls come in. Their job isn't to stop the incident, but to identify it and sound the alarm, letting you know that something is wrong. And you can see the exact same pattern for detection. A technical control like system logs creates the evidence trail. The managerial control is the process of actually reviewing those logs to spot weird anomalies. An operational control is a guard actively patrolling the grounds. And a physical control is a motion detector that trips an alarm. They don't stop the attack, but and this is critical, they tell you it's happening.

So, an alarm goes off, an incident has been detected. Now what? You have to fix it, and you have to fix it fast. That is the job of corrective controls. These are the actions you take after an incident to limit the damage and get back to business. This slide shows that response in action. Just imagine ransomware hits one of your servers. The detection system sends an alert. That's step one. Then the corrective control kicks in. Your team activates its incident response plan. Maybe that means isolating the system and restoring everything from a clean backup. The whole point is to have a swift and orderly recovery.

Now, to round out our framework, let's quickly hit the final three actions. Deterrent controls are all about a bit of psychological warfare. Think of a sign that says, "This area is under video surveillance." It might not physically stop someone, but it sure makes them think twice. Compensating controls are your crucial plan B. When a primary control fails, let's say the power goes out. Your backup generator kicks in, it's a vital safety net. And finally, directive controls are there to guide behavior. That authorized personnel-only sign is a simple command telling people where they should and more importantly shouldn't go.

Now it is so important to remember that this matrix isn't some rigid set in stone rulebook. It's a mental model. It's a really powerful way to organize your thinking about security and to make sure you've got all your bases covered.

So, if there's one key takeaway, it's this. Security is not a one-size-fits-all checklist. It just isn't. The controls a hospital needs to protect patient data are going to be vastly different from what a small retail shop needs. This framework gives you the power to analyze your own specific risks and build a fortress that is just right for you.

So, I'll leave you with this question to chew on. Now that you have this complete framework in your head, which type of security control do you think is the most overlooked out there in the real world? Something to think about. Thanks for joining me today.""",
        },
        "fundamental_concepts": {
            "description": "Core security principles and concepts",
            "cia_triad": [
                "Confidentiality - Data is protected from unauthorized access",
                "Integrity - Data is accurate and hasn't been tampered with",
                "Availability - Data and systems are accessible when needed",
            ],
            "aaa": [
                "Authentication - Verifying identity (who you are)",
                "Authorization - Granting access rights (what you can do)",
                "Accounting - Tracking actions (what you did and when)",
            ],
            "other_concepts": [
                "Non-repudiation - Proof that cannot be denied (digital signatures)",
                "Gap Analysis - Comparing current state to desired state",
                "Zero Trust - Never trust, always verify approach",
            ],
            "key_points": [
                "CIA Triad is foundation of information security",
                "AAA framework controls system access",
                "Zero Trust assumes breach and verifies everything",
            ],
        },
        "zero_trust": {
            "description": "Zero Trust architecture and principles",
            "control_plane": [
                "Adaptive Identity - Dynamic identity verification",
                "Threat Scope Reduction - Minimize attack surface",
                "Policy-driven Access Control - Policies determine access",
                "Policy Administrator - Manages access policies",
                "Policy Engine - Makes access decisions",
            ],
            "data_plane": [
                "Implicit Trust Zones - No implicit trust anywhere",
                "Subject/System - Users and systems requesting access",
                "Policy Enforcement Point - Enforces access decisions",
            ],
            "key_points": [
                "Assumes breach has already occurred",
                "Continuous verification of all users and devices",
                "Micro-segmentation limits lateral movement",
            ],
        },
        "physical_security": {
            "description": "Physical security controls and measures",
            "barriers": [
                "Bollards - Posts to prevent vehicle access",
                "Access Control Vestibule - Double-door entry system",
                "Fencing - Perimeter security barrier",
                "Lighting - Deter intruders and aid surveillance",
            ],
            "access_controls": [
                "Security Guards - Human monitoring and response",
                "Access Badges - Electronic access credentials",
                "Video Surveillance - Continuous monitoring",
            ],
            "sensors": [
                "Infrared - Detects heat signatures",
                "Pressure - Detects weight or force",
                "Microwave - Detects motion through radio waves",
                "Ultrasonic - Detects movement through sound waves",
            ],
            "key_points": [
                "Multiple layers of physical security",
                "Physical security is first line of defense",
                "Sensors provide automated detection",
            ],
        },
        "deception_technology": {
            "description": "Deception and disruption technologies",
            "types": [
                "Honeypot - Fake system to attract attackers",
                "Honeynet - Network of honeypots",
                "Honeyfile - Fake file to detect unauthorized access",
                "Honeytoken - Fake data to track usage",
            ],
            "key_points": [
                "Used to detect and analyze attacker behavior",
                "Provides early warning of attacks",
                "Can gather threat intelligence",
            ],
        },
        "change_management": {
            "description": "Change management processes and procedures",
            "business_processes": [
                "Approval Process - Formal authorization required",
                "Ownership - Clear responsibility for changes",
                "Stakeholders - Identify affected parties",
                "Impact Analysis - Assess potential effects",
                "Test Results - Verify changes work as expected",
                "Backout Plan - Rollback procedure if issues arise",
                "Maintenance Window - Scheduled time for changes",
                "Standard Operating Procedure (SOP) - Documented process",
            ],
            "technical_implications": [
                "Allow/Deny Lists - Update access controls",
                "Restricted Activities - Limit during change windows",
                "Downtime - Plan for service interruptions",
                "Service/Application Restart - Required after changes",
                "Legacy Applications - Consider compatibility",
                "Dependencies - Identify interconnected systems",
            ],
            "key_points": [
                "Reduces risk of unauthorized changes",
                "Ensures changes are tested and documented",
                "Provides rollback capability if needed",
            ],
        },
        "cryptography": {
            "description": "Cryptographic solutions and implementations",
            "pki": [
                "Public Key - Shared openly for encryption",
                "Private Key - Kept secret for decryption",
                "Key Escrow - Third-party key storage",
            ],
            "encryption_types": [
                "Symmetric - Same key for encryption/decryption (AES, DES)",
                "Asymmetric - Public/private key pairs (RSA, ECC)",
                "Full-disk Encryption - Entire disk encrypted",
                "File/Volume Encryption - Specific files or volumes",
                "Database/Record Encryption - Protect data at rest",
                "Transport Encryption - Protect data in transit (TLS, IPSec)",
            ],
            "tools": [
                "TPM - Trusted Platform Module (hardware security)",
                "HSM - Hardware Security Module (key management)",
                "Key Management System - Centralized key administration",
                "Secure Enclave - Isolated processing environment",
            ],
            "obfuscation": [
                "Steganography - Hiding data in other files",
                "Tokenization - Replacing sensitive data with tokens",
                "Data Masking - Obscuring sensitive information",
            ],
            "hashing": [
                "Hashing - One-way cryptographic function (SHA, MD5)",
                "Salting - Adding random data to passwords before hashing",
                "Key Stretching - Making weak keys stronger",
            ],
            "certificates": [
                "Certificate Authorities (CA) - Issue digital certificates",
                "Certificate Revocation List (CRL) - List of revoked certs",
                "OCSP - Online Certificate Status Protocol",
                "Self-signed - Certificate signed by creator",
                "Third-party - Certificate from trusted CA",
                "Root of Trust - Top-level trusted authority",
                "CSR - Certificate Signing Request",
                "Wildcard - Certificate for multiple subdomains",
            ],
            "key_points": [
                "Asymmetric encryption solves key distribution problem",
                "Hashing verifies data integrity",
                "Digital signatures provide non-repudiation",
                "PKI enables secure communication at scale",
            ],
        },
    },
}