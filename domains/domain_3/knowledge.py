"""
Domain 3: Security Architecture
================================
Weight: 18% of exam
Official CompTIA Security+ SY0-701
"""

DOMAIN_3_KNOWLEDGE = {
    "name": "Security Architecture",
    "weight": "18%",
    "topics": {
        "architecture_models": {
            "description": "Security implications of various architecture models",
            "cloud_models": [
                "Cloud - Remote computing resources and services",
                "Hybrid - Mix of on-premises and cloud",
                "Multi-cloud - Using multiple cloud providers",
            ],
            "modern_architectures": [
                "Infrastructure as Code (IaC) - Automated infrastructure provisioning",
                "Serverless - Function-as-a-Service, no server management",
                "Microservices - Distributed application architecture",
                "Software-Defined Networking (SDN) - Programmable networks",
                "Containerization - Lightweight application packaging (Docker, Kubernetes)",
                "Virtualization - Virtual machines and hypervisors",
            ],
            "specialized_systems": [
                "IoT - Internet of Things devices",
                "ICS/SCADA - Industrial Control Systems",
                "RTOS - Real-Time Operating Systems",
                "Embedded Systems - Purpose-built computing devices",
            ],
            "on_premises": [
                "On-premises - Locally hosted infrastructure",
                "Centralized vs Decentralized - Architecture topology",
            ],
            "considerations": [
                "Availability - System uptime and accessibility",
                "Resilience - Ability to recover from disruptions",
                "Cost - Total cost of ownership",
                "Responsiveness - Performance and latency",
                "Scalability - Ability to grow with demand",
                "Ease of Deployment - Implementation complexity",
                "Risk Transference - Shifting risk to providers",
                "Ease of Recovery - Business continuity",
                "Patch Availability - Update management",
                "Power - Energy consumption",
                "Compute - Processing capabilities",
            ],
            "key_points": [
                "Each architecture has unique security implications",
                "Cloud introduces shared responsibility model",
                "ICS/SCADA systems require specialized security",
            ],
        },
        "enterprise_infrastructure": {
            "description": "Applying security principles to enterprise infrastructure",
            "design_principles": [
                "Device Placement - Strategic positioning of security devices",
                "Security Zones - Network segmentation (DMZ, internal, external)",
                "Attack Surface - Minimizing exposure points",
                "Connectivity - Secure communication channels",
                "Fail-open vs Fail-closed - Failure modes for security devices",
            ],
            "device_attributes": [
                "Active vs Passive - Device operation mode",
                "Inline vs Monitor Mode - Traffic handling approach",
            ],
            "network_appliances": [
                "Jump Server - Secure administrative access point",
                "Proxy Server - Intermediary for client requests",
                "IPS/IDS - Intrusion Prevention/Detection Systems",
                "Load Balancer - Distributing traffic across servers",
                "Sensors - Security monitoring devices",
            ],
            "port_security": [
                "802.1X - Network access control standard",
                "EAP - Extensible Authentication Protocol",
            ],
            "firewall_types": [
                "Web Application Firewall (WAF) - Application-layer filtering",
                "Unified Threat Management (UTM) - All-in-one security appliance",
                "Next-Generation Firewall (NGFW) - Advanced threat protection",
                "Layer 4 Firewall - Transport layer filtering",
                "Layer 7 Firewall - Application layer filtering",
            ],
            "secure_communication": [
                "VPN - Virtual Private Network tunneling",
                "TLS - Transport Layer Security",
                "IPSec - IP Security protocol suite",
                "SD-WAN - Software-Defined Wide Area Network",
                "SASE - Secure Access Service Edge",
            ],
            "key_points": [
                "Defense in depth uses multiple security layers",
                "Network segmentation limits lateral movement",
                "Choose appropriate controls for each security zone",
            ],
        },
        "data_protection": {
            "description": "Methods to protect data confidentiality and integrity",
            "data_types": [
                "Regulated Data - GDPR, HIPAA, PCI DSS protected",
                "Trade Secret - Proprietary business information",
                "Intellectual Property - Patents, copyrights, trademarks",
                "Legal Information - Attorney-client privileged",
                "Financial Data - Payment and accounting information",
                "Human-readable - Text, documents",
                "Non-human-readable - Binary, encrypted data",
            ],
            "data_classification": [
                "Sensitive - Requires protection but not regulated",
                "Confidential - Internal use only",
                "Public - Freely available information",
                "Restricted - Highly sensitive, limited access",
                "Private - Personal or proprietary information",
                "Critical - Essential for operations",
            ],
            "data_states": [
                "At Rest - Stored data on disk or media",
                "In Transit - Data moving across networks",
                "In Use - Data being processed in memory",
            ],
            "protection_methods": [
                "Geographic Restrictions - Data residency requirements",
                "Encryption - Converting data to unreadable format",
                "Hashing - One-way cryptographic transformation",
                "Masking - Obscuring sensitive data elements",
                "Tokenization - Replacing data with surrogate values",
                "Obfuscation - Making data difficult to understand",
                "Segmentation - Isolating sensitive data",
                "Permission Management - Access control lists",
            ],
            "key_points": [
                "Protect data in all three states",
                "Classification drives protection requirements",
                "Encryption is primary confidentiality control",
            ],
        },
        "resilience_recovery": {
            "description": "High availability and disaster recovery strategies",
            "high_availability": [
                "Load Balancing - Distributing workload across systems",
                "Clustering - Multiple systems working as one",
                "Active-Active - All nodes processing simultaneously",
                "Active-Passive - Standby nodes ready to take over",
            ],
            "disaster_recovery_sites": [
                "Hot Site - Fully operational backup facility",
                "Cold Site - Empty facility with infrastructure only",
                "Warm Site - Partially equipped backup facility",
                "Geographic Dispersion - Multiple locations for redundancy",
            ],
            "platform_diversity": [
                "Multi-cloud - Using multiple cloud providers",
                "Hybrid Cloud - On-premises and cloud combination",
                "Continuity of Operations (COOP) - Maintaining critical functions",
            ],
            "backup_strategies": [
                "Onsite Backups - Local backup storage",
                "Offsite Backups - Remote backup storage",
                "Backup Frequency - How often backups occur",
                "Encryption - Protecting backup data",
                "Snapshots - Point-in-time copies",
                "Replication - Real-time data copying",
                "Journaling - Transaction logging",
            ],
            "recovery_testing": [
                "Tabletop Exercises - Discussion-based testing",
                "Failover Testing - Switching to backup systems",
                "Simulation - Mock disaster scenarios",
                "Parallel Processing - Running systems simultaneously",
            ],
            "power_management": [
                "Generators - Long-term power backup",
                "UPS - Uninterruptible Power Supply (short-term)",
                "PDU - Power Distribution Unit",
            ],
            "key_points": [
                "Hot sites provide fastest recovery",
                "Regular backup testing is essential",
                "Geographic dispersion protects against regional disasters",
                "RTO and RPO drive recovery strategy",
            ],
        },
    },
}