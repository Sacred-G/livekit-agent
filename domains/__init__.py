"""
Security+ Domains Package
=========================
Organized knowledge base and lessons by CompTIA Security+ exam domains.
"""

from .domain_1.knowledge import DOMAIN_1_KNOWLEDGE
from .domain_2.knowledge import DOMAIN_2_KNOWLEDGE
from .domain_3.knowledge import DOMAIN_3_KNOWLEDGE
from .domain_4.knowledge import DOMAIN_4_KNOWLEDGE
from .domain_5.knowledge import DOMAIN_5_KNOWLEDGE

# Consolidated knowledge base for easy access
ALL_DOMAINS = {
    "domain_1": DOMAIN_1_KNOWLEDGE,
    "domain_2": DOMAIN_2_KNOWLEDGE,
    "domain_3": DOMAIN_3_KNOWLEDGE,
    "domain_4": DOMAIN_4_KNOWLEDGE,
    "domain_5": DOMAIN_5_KNOWLEDGE,
}

__all__ = [
    "DOMAIN_1_KNOWLEDGE",
    "DOMAIN_2_KNOWLEDGE",
    "DOMAIN_3_KNOWLEDGE",
    "DOMAIN_4_KNOWLEDGE",
    "DOMAIN_5_KNOWLEDGE",
    "ALL_DOMAINS",
]