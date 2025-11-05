"""
Test script to verify scripted lesson is accessible in the knowledge base
"""

from domains import ALL_DOMAINS

def test_scripted_lesson():
    """Test that scripted lesson for security_controls in domain_1 is available"""
    
    print("=" * 70)
    print("SCRIPTED LESSON TEST")
    print("=" * 70)
    
    # Check domain 1 exists
    print("\n✓ Test 1: Checking domain_1 exists...")
    if "domain_1" not in ALL_DOMAINS:
        print("  ✗ domain_1 not found!")
        return False
    
    domain_1 = ALL_DOMAINS["domain_1"]
    print(f"  ✓ Domain found: {domain_1['name']}")
    
    # Check security_controls topic exists
    print("\n✓ Test 2: Checking 'security_controls' topic exists...")
    if "security_controls" not in domain_1["topics"]:
        print("  ✗ 'security_controls' topic not found!")
        return False
    
    sec_controls = domain_1["topics"]["security_controls"]
    print(f"  ✓ Topic found: {sec_controls['description']}")
    
    # Check scripted_lesson field exists
    print("\n✓ Test 3: Checking 'scripted_lesson' field exists...")
    if "scripted_lesson" not in sec_controls:
        print("  ✗ 'scripted_lesson' field not found!")
        print(f"  Available fields: {list(sec_controls.keys())}")
        return False
    
    scripted_lesson = sec_controls["scripted_lesson"]
    print(f"  ✓ Scripted lesson found!")
    print(f"  Length: {len(scripted_lesson)} characters")
    print(f"  Preview: {scripted_lesson[:150]}...")
    
    # Verify content
    print("\n✓ Test 4: Verifying lesson content...")
    expected_phrases = [
        "detective controls",
        "corrective controls",
        "deterrent controls",
        "compensating controls",
        "directive controls"
    ]
    
    found_phrases = []
    for phrase in expected_phrases:
        if phrase in scripted_lesson.lower():
            found_phrases.append(phrase)
            print(f"  ✓ Contains '{phrase}'")
        else:
            print(f"  ✗ Missing '{phrase}'")
    
    # Summary
    print("\n" + "=" * 70)
    if len(found_phrases) == len(expected_phrases):
        print("✅ ALL TESTS PASSED - Scripted Lesson is Ready!")
        print("=" * 70)
        print("\nTo use the scripted lesson, say:")
        print("  'Deliver scripted lesson on security controls from domain 1'")
        print("\nOr use the function:")
        print("  deliver_scripted_lesson(domain='domain_1', topic='security_controls')")
        return True
    else:
        print(f"⚠️  Some phrases missing ({len(found_phrases)}/{len(expected_phrases)} found)")
        print("=" * 70)
        return False

if __name__ == "__main__":
    test_scripted_lesson()
