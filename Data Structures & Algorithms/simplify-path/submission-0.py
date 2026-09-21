class Solution:
    def simplifyPath(self, path: str) -> str:
        pathParts = path.split('/')
        print(pathParts)
        res = []

        for i, part in enumerate(pathParts):
            if part == "" or part == ".":
                continue
            elif part == "..":
                if res:
                    res.pop()
            else:
                res.append(part)
        if not res:
            return "/"

        return "/" + "/".join(res)