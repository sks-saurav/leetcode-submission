class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        email_to_name = {}

        def get_parent(u):
            if parent[u] != u:
                parent[u] = get_parent(parent[u])
            return parent[u]

        def union(u, v):
            pu = get_parent(u)
            pv = get_parent(v)
            if pu != pv:
                parent[pu] = pv

        for ac in accounts:
            name = ac[0]
            for email in ac[1:]:
                if email not in parent:
                    parent[email] = email
                email_to_name[email] = name

        for ac in accounts:
            first_email = ac[1]
            for next_email in ac[2:]:
                union(first_email, next_email)

        buckets = defaultdict(list)
        for email in parent:
            root = get_parent(email)
            buckets[root].append(email)

        ans = []
        for root, emails in buckets.items():
            ans.append([email_to_name[root]] + sorted(emails))

        return ans