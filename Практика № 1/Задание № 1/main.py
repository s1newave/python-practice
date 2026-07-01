s = "Pyth1abch2hon"

a, b = s.find("h"), s.rfind("h")
s = s[:a] + s[b:a:-1] + s[b:]

print(s)
