"""
LeetCode: 2026 01 04 16.26.34 Accepted Runtime 7ms Memory 17.2MB

Algorithm:
For each entry, split into visits count and domain. Split domain by '.' to get parts. For each possible subdomain (from each part index to end), join parts and add visits to counts map. This aggregates visits for all subdomains. Return formatted strings "count domain" for all entries.

Time Complexity: O(n^2)
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