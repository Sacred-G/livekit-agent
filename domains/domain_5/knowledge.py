"""
Domain 5: Security Program Management and Oversight
=====================================================
Weight: 20% of exam
Official CompTIA Security+ SY0-701
"""

DOMAIN_5_KNOWLEDGE = {
    "name": "Security Program Management and Oversight",
    "weight": "20%",
    "topics": {
        "security_governance": {
            "description": "Security governance structures and policies",
            "policies": [
                "Acceptable Use Policy (AUP) - User behavior guidelines",
                "Information Security Policy - Overall security framework",
                "Business Continuity/Disaster Recovery (BC/DR) - Continuity planning",
                "Incident Response Policy - Incident handling procedures",
                "Software Development Lifecycle (SDLC) - Secure development",
                "Change Management Policy - System change procedures",
            ],
            "standards": [
                "Password Standards - Authentication requirements",
                "Access Control Standards - Authorization rules",
                "Physical Security Standards - Facility protection",
                "Encryption Standards - Cryptographic requirements",
            ],
            "procedures": [
                "Onboarding/Offboarding - Employee lifecycle management",
                "Playbooks - Step-by-step response guides",
                "Standard Operating Procedures (SOP) - Operational processes",
            ],
            "external_considerations": [
                "Regulatory Requirements - Legal compliance",
                "Legal Requirements - Contractual obligations",
                "Industry Standards - Sector-specific requirements",
                "Local/Regional/National/Global - Geographic compliance",
            ],
            "governance_structures": [
                "Boards - Executive oversight committees",
                "Committees - Specialized working groups",
                "Government Entities - Regulatory bodies",
                "Centralized vs Decentralized - Governance models",
            ],
            "roles_responsibilities": [
                "Owners - Data and system custodians",
                "Controllers - Data processing oversight",
                "Processors - Data handling operations",
                "Custodians - Data protection and storage",
            ],
            "key_points": [
                "Policies define WHAT to do, procedures define HOW",
                "Governance provides strategic direction",
                "Compliance is mandatory, not optional",
            ],
        },
        "risk_management": {
            "description": "Managing organizational risk",
            "risk_processes": [
                "Identification - Finding potential risks",
                "Assessment - Evaluating risk impact and likelihood",
                "Analysis - Qualitative and quantitative analysis",
                "Risk Register - Documenting identified risks",
                "Tolerance - Acceptable risk levels",
                "Appetite - Risk willingness of organization",
                "Management Strategies - Risk response approaches",
                "Reporting - Communicating risk status",
            ],
            "business_impact_analysis": [
                "Business Impact Analysis (BIA) - Assessing consequences",
                "Recovery Time Objective (RTO) - Maximum downtime",
                "Recovery Point Objective (RPO) - Maximum data loss",
                "Mean Time to Recover (MTTR) - Average recovery time",
                "Mean Time Between Failures (MTBF) - System reliability",
            ],
            "risk_response_strategies": [
                "Risk Mitigation - Reducing risk impact or likelihood",
                "Risk Transference - Shifting risk to third parties (insurance)",
                "Risk Acceptance - Acknowledging and accepting risk",
                "Risk Avoidance - Eliminating risk entirely",
            ],
            "key_points": [
                "ALE = SLE × ARO (Annual Loss Expectancy formula)",
                "RTO and RPO drive recovery strategy",
                "Risk cannot be completely eliminated",
                "Choose appropriate response based on cost-benefit",
            ],
        },
        "third_party_risk": {
            "description": "Managing risks from third-party relationships",
            "vendor_management": [
                "Vendor Assessment - Evaluating supplier security",
                "Vendor Selection - Choosing appropriate partners",
                "Vendor Agreements - Contractual relationships",
                "Service Level Agreements (SLA) - Performance expectations",
                "Memorandum of Agreement (MOA) - Understanding between parties",
                "Memorandum of Understanding (MOU) - Non-binding agreements",
                "Master Service Agreement (MSA) - Framework contracts",
                "Statement of Work (SOW) - Specific work requirements",
                "Non-Disclosure Agreement (NDA) - Confidentiality protection",
                "Business Partnership Agreement (BPA) - Business relationships",
            ],
            "monitoring": [
                "Continuous Monitoring - Ongoing vendor oversight",
                "Questionnaires - Security assessment surveys",
                "Rules of Engagement - Testing boundaries",
                "Performance Reviews - Regular capability assessments",
            ],
            "key_points": [
                "Third parties extend your attack surface",
                "Contracts should include security requirements",
                "Regular monitoring prevents security degradation",
            ],
        },
        "compliance": {
            "description": "Compliance monitoring and reporting",
            "compliance_activities": [
                "Reporting - Regular compliance status updates",
                "Consequences - Penalties for non-compliance",
                "Monitoring - Continuous compliance verification",
                "Privacy - Data protection requirements",
                "Legal Implications - Regulatory consequences",
            ],
            "key_points": [
                "Compliance is legally mandated",
                "Non-compliance can result in fines and penalties",
                "Privacy regulations protect individual rights",
            ],
        },
        "audits_assessments": {
            "description": "Security audits and assessments",
            "audit_types": [
                "Attestation - Independent verification",
                "Internal Audits - Organization self-assessment",
                "Compliance Audits - Regulatory requirement checks",
                "Audit Committee - Executive oversight",
                "External Audits - Third-party independent review",
                "Regulatory Audits - Government compliance checks",
                "Independent Audits - Unbiased external assessment",
            ],
            "penetration_testing": [
                "Physical Penetration Testing - Physical security assessment",
                "Offensive Security - Attacker perspective testing",
                "Defensive Security - Defense capability testing",
                "Integrated Testing - Combined attack scenarios",
                "Known Environment - Full knowledge of systems",
                "Partial Knowledge - Limited system information",
                "Unknown Environment - No prior knowledge (black box)",
            ],
            "privacy_considerations": [
                "National/Global Regulations - Geographic data protection",
                "Data Ownership - Who controls the data",
                "Controller vs Processor - GDPR roles",
                "Right to be Forgotten - Data deletion rights",
                "Data Subject Rights - Individual privacy rights",
            ],
            "key_points": [
                "Audits provide independent verification",
                "Pen testing simulates real attacks",
                "Privacy regulations vary by jurisdiction",
            ],
        },
        "security_awareness": {
            "description": "Security awareness and training programs",
            "training_methods": [
                "Phishing Campaigns - Simulated attacks for training",
                "User Guidance - Security policy communication",
                "Insider Threat Training - Recognizing internal risks",
                "Password Management - Secure authentication practices",
                "Removable Media - Safe handling procedures",
                "Operational Security (OPSEC) - Information protection",
                "Reporting Procedures - Incident notification",
                "Monitoring - User activity surveillance",
                "Execution - Training program implementation",
            ],
            "key_points": [
                "Users are often the weakest link",
                "Regular training reduces human error",
                "Phishing awareness prevents social engineering",
                "Insider threats are particularly dangerous",
            ],
        },
    },
}