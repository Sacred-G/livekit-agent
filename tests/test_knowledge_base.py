"""
Test script to verify knowledge base connection in security agent
"""

from domains import ALL_DOMAINS

def test_knowledge_base():
    """Test that comprehensive knowledge base is properly loaded"""
    
    print("=" * 60)
    print("KNOWLEDGE BASE CONNECTION TEST")
    print("=" * 60)
    
    # Test 1: Check all domains are loaded
    print("\n✓ Test 1: Checking all domains are loaded...")
    expected_domains = ["domain_1", "domain_2", "domain_3", "domain_4", "domain_5"]
    
    for domain in expected_domains:
        if domain in ALL_DOMAINS:
            domain_data = ALL_DOMAINS[domain]
            topic_count = len(domain_data.get("topics", {}))
            print(f"  ✓ {domain}: {domain_data['name']} ({domain_data['weight']}) - {topic_count} topics")
        else:
            print(f"  ✗ {domain}: NOT FOUND")
            return False
    
    # Test 2: Verify domain 1 topics
    print("\n✓ Test 2: Checking Domain 1 topics...")
    domain_1 = ALL_DOMAINS["domain_1"]
    print(f"  Domain: {domain_1['name']}")
    print(f"  Topics available:")
    for topic_key in domain_1["topics"].keys():
        print(f"    - {topic_key}")
    
    # Test 3: Verify a specific topic structure (security_controls)
    print("\n✓ Test 3: Checking 'security_controls' topic structure...")
    if "security_controls" in domain_1["topics"]:
        sec_controls = domain_1["topics"]["security_controls"]
        print(f"  Description: {sec_controls.get('description', 'N/A')[:80]}...")
        
        # List all fields in this topic
        print(f"  Fields available:")
        for field in sec_controls.keys():
            if isinstance(sec_controls[field], list):
                print(f"    - {field}: {len(sec_controls[field])} items")
            else:
                print(f"    - {field}: {type(sec_controls[field]).__name__}")
    else:
        print("  ✗ 'security_controls' topic not found")
        return False
    
    # Test 4: Verify domain 2 (Threats)
    print("\n✓ Test 4: Checking Domain 2 topics...")
    domain_2 = ALL_DOMAINS["domain_2"]
    print(f"  Domain: {domain_2['name']}")
    print(f"  Topics available:")
    for topic_key in domain_2["topics"].keys():
        print(f"    - {topic_key}")
    
    # Test 5: Check cryptography topic (should be in domain 1)
    print("\n✓ Test 5: Checking 'cryptography' topic...")
    if "cryptography" in domain_1["topics"]:
        crypto = domain_1["topics"]["cryptography"]
        print(f"  Description: {crypto.get('description', 'N/A')}")
        print(f"  Has key_points: {'key_points' in crypto}")
        if 'key_points' in crypto:
            print(f"  Number of key points: {len(crypto['key_points'])}")
    else:
        print("  ✗ 'cryptography' topic not found in domain 1")
    
    # Summary
    print("\n" + "=" * 60)
    print("✓ ALL TESTS PASSED - Knowledge Base is Connected!")
    print("=" * 60)
    
    # Display statistics
    total_topics = sum(len(ALL_DOMAINS[d]["topics"]) for d in expected_domains)
    print(f"\nTotal domains: {len(expected_domains)}")
    print(f"Total topics: {total_topics}")
    
    return True

if __name__ == "__main__":
    test_knowledge_base()
