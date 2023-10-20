# https://leetcode.com/problems/reconstruct-itinerary/
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # Create an adjacency list ensuring every airport is a key
        adj = {airport: [] for ticket in tickets for airport in ticket}
        
        for src, dst in sorted(tickets, reverse=True):  # sort in reverse for using pop()
            adj[src].append(dst)
        
        itinerary = []
        
        def visit(airport):
            while adj.get(airport, []):  # use .get() to avoid KeyError
                visit(adj[airport].pop())
            itinerary.append(airport)
        
        visit("JFK")
        return itinerary[::-1]  # reverse the itinerary to get the correct order