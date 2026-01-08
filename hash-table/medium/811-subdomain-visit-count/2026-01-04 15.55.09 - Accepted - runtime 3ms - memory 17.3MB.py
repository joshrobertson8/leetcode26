"""
LeetCode: 2026 01 04 15.55.09 Accepted Runtime 3ms Memory 17.3MB

Algorithm:
Use a hash table to store seen elements for O(1) lookup.

Time Complexity: O(n²)
Space Complexity: O(n)
"""

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        
        counts = {}
        
        for entry in cpdomains:
            visits, domain = entry.split()
            visits = int(visits)
            
            parts = domain.split(".")
            
            for i in range(len(parts)):
                subdomain = ".".join(parts[i:])
                
                if subdomain in counts:
                    counts[subdomain] += visits
                else:
                    counts[subdomain] = visits
        
        return [f"{count} {domain}" for domain, count in counts.items()]