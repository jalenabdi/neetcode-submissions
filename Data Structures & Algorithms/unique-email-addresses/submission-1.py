class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        left = 0
        seen = set()
        for email in emails:
            local, domain = email.split("@")

            local = local.split("+")[0]

            local = local.replace(".", "")

            normalized_email = local + "@" + domain
            seen.add(normalized_email)
        
        return len(seen)
