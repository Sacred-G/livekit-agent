import sys
sys.stdout.reconfigure(encoding='utf-8')

from domains import ALL_DOMAINS

print("=" * 60)
print("KNOWLEDGE BASE VERIFICATION")
print("=" * 60)

# Check domains
print(f"\nDomains loaded: {list(ALL_DOMAINS.keys())}")

for domain_id, domain_data in ALL_DOMAINS.items():
    topic_count = len(domain_data["topics"])
    print(f"\n{domain_id}: {domain_data['name']} ({domain_data['weight']})")
    print(f"  Topics: {topic_count}")
    print(f"  Topic names: {', '.join(list(domain_data['topics'].keys())[:3])}...")

# Check a specific topic
domain_1 = ALL_DOMAINS["domain_1"]
if "security_controls" in domain_1["topics"]:
    sec = domain_1["topics"]["security_controls"]
    print(f"\n\nSample topic: 'security_controls'")
    print(f"  Description: {sec['description'][:60]}...")
    print(f"  Fields: {list(sec.keys())}")
    if "key_points" in sec:
        print(f"  Key points count: {len(sec['key_points'])}")

print("\n" + "=" * 60)
print("SUCCESS: Comprehensive knowledge base is connected!")
print("=" * 60)
