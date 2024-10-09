def generate_parenthesis(n):
    def backtrack(s='', left=0, right=0):
        if len(s) == 2 * n:
            result.append(s)
            return
        if left < n:
            backtrack(s+'(', left+1, right)
        if right < left:
            backtrack(s+')', left, right+1)

    result = []
    backtrack()
    return ",".join(result)


A = int(input("Enter number of pair parenthesis(es): "))
print("All possible parenthesis(es)")
print(generate_parenthesis(A))