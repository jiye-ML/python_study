text = "Monty Python's Flying Circus"
print("upper", "=>", text.upper())

print("lower", "=>", text.lower())
print("split", "=>", text.split())
print("join", "=>", text.join(text.split()))
print("replace", "=>", text.replace("Python", "Java"))
print("find", "=>", text.find("Python"), text.find( "Java"))
print("count", "=>", text.count("n"))