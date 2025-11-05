# CompTIA Security+ SY0-701 Certification Exam: Full Exam Objectives

## Test Details

- **Required Exam:** SY0-701
- **Number of Questions:** Maximum of 90
- **Types of Questions:** Multiple-choice and performance-based
- **Length of Test:** 90 minutes
- **Recommended Experience:** Minimum 2 years in IT administration with a focus on security, hands-on experience with technical information security, and broad knowledge of security concepts

---

## Exam Domains and Weight

| Domain                                        | Percentage of Exam |
| --------------------------------------------- | ------------------ |
| 1.0 General Security Concepts                 | 12%                |
| 2.0 Threats, Vulnerabilities, and Mitigations | 22%                |
| 3.0 Security Architecture                     | 18%                |
| 4.0 Security Operations                       | 28%                |
| 5.0 Security Program Management and Oversight | 20%                |
| **Total**                               | 100%               |

---

# 1.0 General Security Concepts

### 1.1 Compare and contrast various types of security controls

- **Categories:** Technical, Managerial, Operational, Physical
- **Control Types:** Preventive, Deterrent, Detective, Corrective, Compensating, Directive

### 1.2 Summarize fundamental security concepts

- **CIA Triad:** Confidentiality, Integrity, Availability
- **Non-repudiation**
- **AAA:** Authentication, Authorization, Accounting
  - Authenticating people
  - Authenticating systems
  - Authorization models
- **Gap Analysis**
- **Zero Trust**
  - Control Plane
    - Adaptive identity
    - Threat scope reduction
    - Policy-driven access control
    - Policy Administrator
    - Policy Engine
  - Data Plane
    - Implicit trust zones
    - Subject/System
    - Policy Enforcement Point
- **Physical Security**
  - Bollards, Access control vestibule, Fencing, Video surveillance, Security guard, Access badge, Lighting
  - Sensors: Infrared, Pressure, Microwave, Ultrasonic
- **Deception and Disruption Technology**
  - Honeypot, Honeynet, Honeyfile, Honeytoken

### 1.3 Explain the importance of change management processes

- **Business processes:** Approval process, Ownership, Stakeholders, Impact analysis, Test results, Backout plan, Maintenance window, SOP
- **Technical implications:** Allow/Deny lists, Restricted activities, Downtime, Service/Application restart, Legacy apps, Dependencies
- **Documentation:** Updating diagrams, policies, procedures
- **Version Control**

### 1.4 Explain cryptographic solutions

- **PKI:** Public key, Private key, Key escrow
- **Encryption:** Full-disk, Partition, File, Volume, Database, Record; Transport/communication; Symmetric/Asymmetric; Key exchange; Algorithms; Key length
- **Tools:** TPM, HSM, Key management system, Secure enclave
- **Obfuscation:** Steganography, Tokenization, Data masking
- **Hashing & Salting**
- **Digital Signatures & Key stretching**
- **Blockchain & Open Public Ledger**
- **Certificates:** Certificate authorities, CRLs, OCSP, Self-signed, Third-party, Root of trust, CSR, Wildcard

---

# 2.0 Threats, Vulnerabilities, and Mitigations

### 2.1 Compare common threat actors and motivations

- **Threat actors:** Nation-state, Unskilled attacker, Hacktivist, Insider, Organized crime, Shadow IT
- **Attributes:** Internal/external, Resources/funding, Level of sophistication
- **Motivations:** Data exfiltration, Espionage, Service disruption, Blackmail, Financial gain, Philosophical/political, Ethical, Revenge, Chaos, War

### 2.2 Explain common threat vectors and attack surfaces

- **Vectors:** Email, SMS, IM, Image-based, File-based, Voice call, Removable devices
- **Vulnerable software:** Client-based, Agentless, Unsupported systems
- **Networks:** Wireless, Wired, Bluetooth, Open ports
- **Default credentials**
- **Supply chain:** MSPs, Vendors, Suppliers
- **Social Engineering:** Phishing, Vishing, Smishing, Impersonation, BEC, Pretexting, Watering hole, Brand impersonation, Typosquatting

### 2.3 Explain types of vulnerabilities

- **Application:** Memory injection, Buffer overflow, Race conditions, TOC/TOU, Malicious update
- **OS-based, Web-based, Hardware, Virtualization, Cloud-specific, Supply chain, Cryptographic, Misconfiguration, Mobile, Zero-day**

### 2.4 Analyze indicators of malicious activity

- **Malware:** Ransomware, Trojan, Worm, Spyware, Bloatware, Virus, Keylogger, Logic bomb, Rootkit
- **Physical attacks:** Brute force, RFID cloning, Environmental
- **Network attacks:** DDoS (Amplified/Reflected), DNS, Wireless, On-path, Credential replay, Malicious code
- **Application attacks:** Injection, Buffer overflow, Replay, Privilege escalation, Forgery, Directory traversal
- **Cryptographic attacks:** Downgrade, Collision, Birthday
- **Password attacks:** Spraying, Brute force
- **Indicators:** Account lockout, Concurrent session usage, Blocked content, Impossible travel, Resource consumption, Missing logs

### 2.5 Mitigation techniques

- **Segmentation, Access control, Application allow list, Isolation, Patching, Encryption, Monitoring, Least privilege**
- **Hardening:** Endpoint protection, Host-based firewall/HIPS, Disabling ports/protocols, Default password changes, Removal of unnecessary software

---

# 3.0 Security Architecture

### 3.1 Compare security implications of architecture models

- **Models:** Cloud, Hybrid, IaC, Serverless, Microservices, SDN, On-premises, Centralized vs decentralized, Containerization, Virtualization, IoT, ICS/SCADA, RTOS, Embedded systems
- **Considerations:** Availability, Resilience, Cost, Responsiveness, Scalability, Patch availability, Ease of recovery, Power, Compute

### 3.2 Apply security principles to enterprise infrastructure

- **Device placement, Security zones, Attack surface, Connectivity, Fail-open/fail-closed, Device attributes, Active/passive, Inline/monitor**
- **Network appliances:** Jump server, Proxy server, IPS/IDS, Load balancer, Sensors
- **Port security:** 802.1X, EAP
- **Firewalls:** WAF, UTM, NGFW, Layer 4/7
- **Secure communication:** VPN, TLS, IPSec, SD-WAN, SASE
- **Control selection:** Effective controls selection

### 3.3 Protect data

- **Data types:** Regulated, Trade secret, Intellectual property, Legal, Financial, Human/non-human readable
- **Data classification:** Sensitive, Confidential, Public, Restricted, Private, Critical
- **Data states:** At rest, In transit, In use
- **Methods:** Geographic restrictions, Encryption, Hashing, Masking, Tokenization, Obfuscation, Segmentation, Permissions

### 3.4 Resilience and Recovery

- **High availability:** Load balancing, Clustering
- **Sites:** Hot, Cold, Warm, Geographic dispersion
- **Platforms:** Multi-cloud, Continuity of operations
- **Backups:** Onsite/offsite, Frequency, Encryption, Snapshots, Replication
- **Testing:** Tabletop, Failover, Simulation, Parallel processing
- **Power:** Generators, UPS

---

# 4.0 Security Operations

### 4.1 Security techniques

- **Secure baselines:** Establish, Deploy, Maintain
- **Hardening targets:** Mobile, Workstations, Switches, Routers, Cloud, Servers, ICS/SCADA, RTOS, IoT
- **Wireless:** Site surveys, Heat maps, WPA3, AAA/RADIUS, Authentication protocols
- **Application security:** Input validation, Secure cookies, Static/Dynamic code analysis, Code signing
- **Sandboxing, Monitoring**

### 4.2 Asset Management

- **Acquisition/procurement, Assignment/accounting, Monitoring/asset tracking, Disposal/decommissioning**

### 4.3 Vulnerability Management

- Identification (scans, OSINT, penetration tests)
- Analysis (false positives/negatives, CVSS, CVE)
- Response & remediation (patching, compensating controls)
- Validation & reporting

### 4.4 Security Alerting and Monitoring

- Log aggregation, Alerting, Scanning, Reporting, Archiving
- Tools: SCAP, SIEM, Antivirus, DLP, SNMP, NetFlow, Vulnerability scanners

### 4.5 Identity and Access Management

- Firewalls, IDS/IPS, Web filtering, OS security, Secure protocols, DNS/email security, DLP, NAC, EDR/XDR
- Provisioning/de-provisioning, Permission assignment, Identity proofing, Federation, SSO (LDAP, OAuth, SAML)
- Access controls: Mandatory, Discretionary, Role-based, Rule-based, Attribute-based, Time-of-day, Least privilege
- MFA: Biometrics, Hard/Soft tokens, Security keys
- Password best practices, Passwordless, Privileged access management

### 4.6 Modifying Enterprise Capabilities

- Automation & orchestration: Provisioning, Guardrails, Ticketing, CI/CD, APIs
- Incident response: Preparation, Detection, Analysis, Containment, Eradication, Recovery, Lessons learned
- Threat hunting, Digital forensics, Root cause analysis

### 4.7 Using Data Sources

- Log data, Firewall, Application, Endpoint, OS, IPS/IDS, Network, Metadata
- Vulnerability scans, Automated reports, Dashboards, Packet captures

---

# 5.0 Security Program Management and Oversight

### 5.1 Security Governance

- Policies: AUP, InfoSec, BC/DR, Incident response, SDLC, Change management
- Standards: Password, Access control, Physical security, Encryption
- Procedures: Onboarding/offboarding, Playbooks
- External considerations: Regulatory, Legal, Industry, Local/Regional/National/Global
- Governance structures: Boards, Committees, Government entities, Centralized/decentralized
- Roles & responsibilities: Owners, Controllers, Processors, Custodians

### 5.2 Risk Management

- Identification, Assessment, Analysis (qualitative/quantitative), Risk register, Tolerance, Appetite, Management strategies, Reporting
- Business Impact Analysis: RTO, RPO, MTTR, MTBF

### 5.3 Third-party Risk

- Vendor assessment, Selection, Agreements (SLA, MOA, MOU, MSA, SOW, NDA, BPA)
- Monitoring, Questionnaires, Rules of engagement

### 5.4 Compliance

- Reporting, Consequences, Monitoring, Privacy, Legal implications

### 5.5 Audits and Assessments

- Attestation, Internal (Compliance, Audit Committee), External (Regulatory, Independent)
- Pen testing: Physical, Offensive, Defensive, Integrated, Known/Partial/Unknown environment
- National/Global, Data ownership, Controller/Processor, Right to be forgotten

### 5.6 Security Awareness

- Phishing campaigns, User guidance/training, Insider threat, Password management, Removable media, Operational security, Reporting, Monitoring, Execution

---

# Acronyms (Partial)

# CompTIA Security+ SY0-701 Comprehensive Exam Preparation Program

---

---

## Acronyms and Key Terms (A–Z)

- **AAA** – Authentication, Authorization, and Accounting
- **ACL** – Access Control List
- **AES** – Advanced Encryption Standard
- **AES-256** – Advanced Encryption Standard 256-bit
- **AH** – Authentication Header
- **AI** – Artificial Intelligence
- **AIS** – Automated Indicator Sharing
- **ALE** – Annualized Loss Expectancy
- **AP** – Access Point
- **API** – Application Programming Interface
- **APT** – Advanced Persistent Threat
- **ARO** – Annualized Rate of Occurrence
- **ARP** – Address Resolution Protocol
- **ASLR** – Address Space Layout Randomization
- **CHAP** – Challenge Handshake Authentication Protocol
- **CIA** – Confidentiality, Integrity, Availability
- **CIO** – Chief Information Officer
- **CIRT** – Computer Incident Response Team
- **CMS** – Content Management System
- **COOP** – Continuity of Operation Planning
- **COPE** – Corporate Owned, Personally Enabled
- **CP** – Contingency Planning
- **CRC** – Cyclical Redundancy Check
- **CRL** – Certificate Revocation List
- **CSO** – Chief Security Officer
- **CSP** – Cloud Service Provider
- **CSR** – Certificate Signing Request
- **CSRF** – Cross-site Request Forgery
- **CSU** – Channel Service Unit
- **CTM** – Counter Mode
- **CTO** – Chief Technology Officer
- **CVE** – Common Vulnerability Enumeration
- **CVSS** – Common Vulnerability Scoring System
- **CYOD** – Choose Your Own Device
- **DAC** – Discretionary Access Control
- **DBA** – Database Administrator
- **DDoS** – Distributed Denial of Service
- **DEP** – Data Execution Prevention
- **DES** – Digital Encryption Standard
- **DHCP** – Dynamic Host Configuration Protocol
- **DHE** – Diffie-Hellman Ephemeral
- **DKIM** – DomainKeys Identified Mail
- **DLL** – Dynamic Link Library
- **DLP** – Data Loss Prevention
- **DMARC** – Domain Message Authentication Reporting and Conformance
- **DNAT** – Destination Network Address Translation
- **DNS** – Domain Name System
- **DoS** – Denial of Service
- **DPO** – Data Privacy Officer
- **DSA** – Digital Signature Algorithm
- **DSL** – Digital Subscriber Line
- **EAP** – Extensible Authentication Protocol
- **ECB** – Electronic Code Book
- **ECC** – Elliptic Curve Cryptography
- **ECDHE** – Elliptic Curve Diffie-Hellman Ephemeral
- **ECDSA** – Elliptic Curve Digital Signature Algorithm
- **EDR** – Endpoint Detection and Response
- **EFS** – Encrypted File System
- **ERP** – Enterprise Resource Planning
- **ESN** – Electronic Serial Number
- **ESP** – Encapsulated Security Payload
- **FACL** – File System Access Control List
- **FDE** – Full Disk Encryption
- **FIM** – File Integrity Management
- **FPGA** – Field Programmable Gate Array
- **FRR** – False Rejection Rate
- **FTP** – File Transfer Protocol
- **FTPS** – Secured File Transfer Protocol
- **GCM** – Galois Counter Mode
- **GDPR** – General Data Protection Regulation
- **GPG** – Gnu Privacy Guard
- **GPO** – Group Policy Object
- **GPS** – Global Positioning System
- **GPU** – Graphics Processing Unit
- **GRE** – Generic Routing Encapsulation
- **HA** – High Availability
- **HDD** – Hard Disk Drive
- **HIDS** – Host-based Intrusion Detection System
- **HIPS** – Host-based Intrusion Prevention System
- **HMAC** – Hashed Message Authentication Code
- **HOTP** – HMAC-based One-time Password
- **HSM** – Hardware Security Module
- **HTML** – Hypertext Markup Language
- **HTTP** – Hypertext Transfer Protocol
- **HTTPS** – Hypertext Transfer Protocol Secure
- **HVAC** – Heating, Ventilation, Air Conditioning
- **IaaS** – Infrastructure as a Service
- **IaC** – Infrastructure as Code
- **IAM** – Identity and Access Management
- **ICMP** – Internet Control Message Protocol
- **ICS** – Industrial Control Systems
- **IDEA** – International Data Encryption Algorithm
- **IDF** – Intermediate Distribution Frame
- **IdP** – Identity Provider
- **IDS** – Intrusion Detection System
- **IEEE** – Institute of Electrical and Electronics Engineers
- **IKE** – Internet Key Exchange
- **IM** – Instant Messaging
- **IMAP** – Internet Message Access Protocol
- **IoC** – Indicators of Compromise
- **IoT** – Internet of Things
- **IP** – Internet Protocol
- **IPS** – Intrusion Prevention System
- **IPSec** – Internet Protocol Security
- **IR** – Incident Response
- **IRC** – Internet Relay Chat
- **IRP** – Incident Response Plan
- **ISO** – International Standards Organization
- **ISP** – Internet Service Provider
- **ISSO** – Information Systems Security Officer
- **IV** – Initialization Vector
- **KDC** – Key Distribution Center
- **KEK** – Key Encryption Key
- **L2TP** – Layer 2 Tunneling Protocol
- **LAN** – Local Area Network
- **LDAP** – Lightweight Directory Access Protocol
- **LEAP** – Lightweight Extensible Authentication Protocol
- **MaaS** – Monitoring as a Service
- **MAC** – Mandatory Access Control / Media Access Control / Message Authentication Code
- **MAN** – Metropolitan Area Network
- **MBR** – Master Boot Record
- **MD5** – Message Digest 5
- **MDF** – Main Distribution Frame
- **MDM** – Mobile Device Management
- **MFA** – Multifactor Authentication
- **MFD** – Multifunction Device
- **MFP** – Multifunction Printer
- **ML** – Machine Learning
- **MMS** – Multimedia Message Service
- **MOA** – Memorandum of Agreement
- **MOU** – Memorandum of Understanding
- **MPLS** – Multi-protocol Label Switching
- **MSA** – Master Service Agreement
- **MSCHAP** – Microsoft Challenge Handshake Authentication Protocol
- **MSP** – Managed Service Provider
- **MSSP** – Managed Security Service Provider
- **MTBF** – Mean Time Between Failures
- **MTTF** – Mean Time to Failure
- **MTTR** – Mean Time to Recover
- **MTU** – Maximum Transmission Unit
- **NAC** – Network Access Control
- **NAT** – Network Address Translation
- **NDA** – Non-Disclosure Agreement
- **NFC** – Near Field Communication
- **NGFW** – Next-Generation Firewall
- **NIDS** – Network-based Intrusion Detection System
- **NIPS** – Network-based Intrusion Prevention System
- **NIST** – National Institute of Standards & Technology
- **NTFS** – New Technology File System
- **NTLM** – New Technology LAN Manager
- **NTP** – Network Time Protocol
- **OAUTH** – Open Authorization
- **OCSP** – Online Certificate Status Protocol
- **OID** – Object Identifier
- **OS** – Operating System
- **OSINT** – Open-source Intelligence
- **OSPF** – Open Shortest Path First
- **OT** – Operational Technology
- **OTA** – Over the Air
- **OVAL** – Open Vulnerability Assessment Language
- **P12** – PKCS #12
- **P2P** – Peer-to-Peer
- **PaaS** – Platform as a Service
- **PAC** – Proxy Auto Configuration
- **PAM** – Privileged Access Management / Pluggable Authentication Modules
- **PAP** – Password Authentication Protocol
- **PAT** – Port Address Translation
- **PBKDF2** – Password-Based Key Derivation Function 2
- **PBX** – Private Branch Exchange
- **PCAP** – Packet Capture
- **PCI DSS** – Payment Card Industry Data Security Standard
- **PDU** – Power Distribution Unit
- **PEAP** – Protected Extensible Authentication Protocol
- **PED** – Personal Electronic Device
- **PEM** – Privacy Enhanced Mail
- **PFS** – Perfect Forward Secrecy
- **PGP** – Pretty Good Privacy
- **PHI** – Personal Health Information
- **PII** – Personally Identifiable Information
- **PIV** – Personal Identity Verification
- **PKCS** – Public Key Cryptography Standards
- **PKI** – Public Key Infrastructure
- **POP** – Post Office Protocol
- **POTS** – Plain Old Telephone Service
- **PPP** – Point-to-Point Protocol
- **PPTP** – Point-to-Point Tunneling Protocol
- **PSK** – Pre-shared Key
- **PTZ** – Pan-Tilt-Zoom
- **PUP** – Potentially Unwanted Program
- **RA** – Recovery Agent / Registration Authority
- **RACE** – Research and Development in Advanced Communications Technologies in Europe
- **RAD** – Rapid Application Development
- **RADIUS** – Remote Authentication Dial-in User Service
- **RAID** – Redundant Array of Inexpensive Disks
- **RAS** – Remote Access Server
- **RAT** – Remote Access Trojan
- **RBAC** – Role-based Access Control / Rule-based Access Control
- **RC4** – Rivest Cipher version 4
- **RDP** – Remote Desktop Protocol
- **RFID** – Radio Frequency Identifier
- **RIPEMD** – RACE Integrity Primitives Evaluation Message Digest
- **ROI** – Return on Investment
- **RPO** – Recovery Point Objective
- **RSA** – Rivest, Shamir, & Adleman
- **RTBH** – Remotely Triggered Black Hole
- **RTO** – Recovery Time Objective
- **RTOS** – Real-time Operating System
- **RTP** – Real-time Transport Protocol
- **S/MIME** – Secure/Multipurpose Internet Mail Extensions
- **SaaS** – Software as a Service
- **SAE** – Simultaneous Authentication of Equals
- **SAML** – Security Assertions Markup Language
- **SAN** – Storage Area Network / Subject Alternative Name
- **SASE** – Secure Access Service Edge
- **SCADA** – Supervisory Control and Data Acquisition
- **SCAP** – Security Content Automation Protocol
- **SCEP** – Simple Certificate Enrollment Protocol
- **SD-WAN** – Software-defined Wide Area Network
- **SDK** – Software Development Kit
- **SDLC** – Software Development Lifecycle
- **SDLM** – Software Development Lifecycle Methodology
- **SDN** – Software-defined Networking
- **SE Linux** – Security-enhanced Linux
- **SED** – Self-encrypting Drives
- **SEH** – Structured Exception Handler
- **SFTP** – Secured File Transfer Protocol
- **SHA** – Secure Hashing Algorithm
- **SHTTP** – Secure Hypertext Transfer Protocol
- **SIEM** – Security Information and Event Management
- **SIM** – Subscriber Identity Module
- **SLA** – Service-level Agreement
- **SLE** – Single Loss Expectancy
- **SMS** – Short Message Service
- **SMTP** – Simple Mail Transfer Protocol
- **SMTPS** – Simple Mail Transfer Protocol Secure
- **SNMP** – Simple Network Management Protocol
- **SOAP** – Simple Object Access Protocol
- **SOAR** – Security Orchestration, Automation, Response
- **SoC** – System on Chip
- **SOC** – Security Operations Center
- **SOW** – Statement of Work
- **SPF** – Sender Policy Framework
- **SPIM** – Spam over Internet Messaging
- **SQL** – Structured Query Language
- **SQLi** – SQL Injection
- **SRTP** – Secure Real-Time Protocol
- **SSD** – Solid State Drive
- **SSH** – Secure Shell
- **SSL** – Secure Sockets Layer
- **SSO** – Single Sign-on
- **STIX** – Structured Threat Information eXchange
- **SWG** – Secure Web Gateway
- **TACACS+** – Terminal Access Controller Access Control System
- **TAXII** – Trusted Automated eXchange of Indicator Information
- **TCP/IP** – Transmission Control Protocol/Internet Protocol
- **TGT** – Ticket Granting Ticket
- **TKIP** – Temporal Key Integrity Protocol
- **TLS** – Transport Layer Security
- **TOC** – Time-of-check
- **TOTP** – Time-based One-Time Password
- **TOU** – Time-of-use
- **TPM** – Trusted Platform Module
- **TTP** – Tactics, Techniques, and Procedures
- **TSIG** – Transaction Signature
- **UAT** – User Acceptance Testing
- **UAV** – Unmanned Aerial Vehicle
- **UDP** – User Datagram Protocol
- **UEFI** – Unified Extensible Firmware Interface
- **UEM** – Unified Endpoint Management
- **UPS** – Uninterruptable Power Supply
- **URI** – Uniform Resource Identifier
- **URL** – Universal Resource Locator
- **USB** – Universal Serial Bus
- **USB OTG** – USB On the Go
- **UTM** – Unified Threat Management
- **UTP** – Unshielded Twisted Pair
- **VBA** – Visual Basic
- **VDE** – Virtual Desktop Environment
- **VDI** – Virtual Desktop Infrastructure
- **VLAN** – Virtual Local Area Network
- **VLSM** – Variable Length Subnet Masking
- **VM** – Virtual Machine
- **VoIP** – Voice over IP
- **VPC** – Virtual Private Cloud
- **VPN** – Virtual Private Network
- **VTC** – Video Teleconferencing
- **WAF** – Web Application Firewall
- **WAP** – Wireless Access Point
- **WEP** – Wired Equivalent Privacy
- **WIDS** – Wireless Intrusion Detection System
- **WIPS** – Wireless Intrusion Prevention System
- **WO** – Work Order
- **WPA** – Wi-Fi Protected Access
- **WPS** – Wi-Fi Protected Setup
- **WTLS** – Wireless TLS
- **XDR** – Extended Detection and Response
- **XML** – Extensible Markup Language
- **XOR** – Exclusive Or
- **XSRF** – Cross-site Request Forgery
- **XSS** – Cross-site Scripting

---

## Sample Hardware, Software, and Tools

### Equipment

- Tablet
- Laptop
- Web server
- Firewall
- Router
- Switch
- IDS (Intrusion Detection System)
- IPS (Intrusion Prevention System)
- Wireless access point
- Virtual machines
- Email system
- Internet access
- DNS server
- IoT devices
- Hardware tokens
- Smartphone

### Spare Hardware

- NICs (Network Interface Cards)
- Power supplies
- GBICs
- SFPs
- Managed Switch
- Wireless access point
- UPS (Uninterruptable Power Supply)

### Tools

- Wi-Fi analyzer
- Network mapper
- NetFlow analyzer

---

### Software

- Windows OS
- Linux OS
- Kali Linux
- Packet capture software
- Pen testing software
- Static and dynamic analysis tools
- Vulnerability scanner
- Network emulators
- Sample code
- Code editor
- SIEM (Security Information and Event Management)
- Keyloggers
- MDM (Mobile Device Management) software
- VPN
- DHCP service
- DNS service

---

### Other Resources

- Access to cloud environments
- Sample network documentation/diagrams
- Sample logs

---

## Study Tips

1. Memorize the acronyms and their definitions.
2. Understand the difference between attack types and security controls.
3. Practice configuring network and endpoint security tools.
4. Review disaster recovery and business continuity concepts.
5. Utilize lab environments to test security concepts hands-on.
6. Take practice exams to simulate the real testing environment.
