class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        i=0;j=len(people)-1;boat=0
        people.sort()
        while i<=j:
            if people[i]+people[j]<=limit:
                boat+=1
                i+=1;j-=1
            else:
                if people[j]<=limit:
                    boat+=1
                j-=1
        return boat

