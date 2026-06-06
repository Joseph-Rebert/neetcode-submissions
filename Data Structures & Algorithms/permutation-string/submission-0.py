class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        target = {}
        counts = {}

        # Build target hashmap from s1
        for c in s1:
            target[c] = target.get(c, 0) + 1

        # Build initial window in s2 with same size as s1
        for i in range(len(s1)):
            counts[s2[i]] = counts.get(s2[i], 0) + 1

        # Check first window
        if counts == target:
            return True

        # Slide the window
        l = 0

        for r in range(len(s1), len(s2)):
            # Add new right character
            counts[s2[r]] = counts.get(s2[r], 0) + 1

            # Remove old left character
            counts[s2[l]] -= 1

            if counts[s2[l]] == 0:
                del counts[s2[l]]

            l += 1

            # Compare window with target
            if counts == target:
                return True

        return False
            