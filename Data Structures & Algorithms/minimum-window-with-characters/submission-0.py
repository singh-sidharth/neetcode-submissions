class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_length = len(s)
        t_length = len(t)
        res = ""
        if s_length < t_length:
            return res
        # Count all characters of t
        t_count = Counter(t)
        required_chars = len(t_count)
        # Intializeing
        s_count = defaultdict(int)
        formed_chars = 0
        minL = s_length + 1
        i, j = 0, 0
        left = 0
        right = 0
        # Sliding window
        while right < s_length:
            # Add a character from window
            s_count[s[right]] += 1
            # Count the required characters in t
            if s[right] in t_count and s_count[s[right]] == t_count[s[right]]:
                formed_chars += 1
            # Contract the left window till it is valid
            while left <= right and formed_chars == required_chars:
                if (right - left + 1) < minL:
                    minL = right - left + 1
                    i = left
                    j = right
                s_count[s[left]] -= 1
                # Reduce the required character if it is taken out from left window
                if s[right] in t_count and s_count[s[left]] < t_count[s[left]]:
                    formed_chars -= 1
                left += 1
            right += 1

        return "" if minL == s_length + 1 else s[i : j + 1]