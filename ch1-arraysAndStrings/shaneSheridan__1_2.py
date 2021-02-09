# 1.2 - Check Permutation 
# Given two strings, write a method to decide if one is a permutation of the other.
# E.g. “abcd” is a permutation of “dabc”.

# Permuation strings must be:
# 1. the same lenth.
# 2. identical, either initially or when sorted, and assuming case sensitivity here. 
def is_permutation(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    if (is_identical(s1, s2)):
        return True
    
    s1Len = len(s1)
    s2Len = len(s2)
    if (s1Len != s2Len):
        return False
    
    s1 = sorted(s1)
    s2 = sorted(s2)
    if (is_identical(s1, s2)):
        return True
    
    return False

def is_identical(s1, s2):
    return True if (s1==s2) else False

# Test.
some_strings = [["abcd", "dabc"], ["abcd", "erf"], ["abcd", "erfg"], ["abcd", "abcd"], ["abcd", "DaBc"], ["abcd", "DaBc "], ["ab cd", "DaBc "]]
for s in some_strings:
    s1 = s[0]
    s2 = s[1]
    print(f"Checking if '{s1}' is a permutation of '{s2}'.")
    print(is_permutation(s1, s2)) 

