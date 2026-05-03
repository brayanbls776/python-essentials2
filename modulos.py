from platform import platform , machine , system , version, python_implementation, python_version_tuple, processor

print(python_implementation())

for atr in python_version_tuple():
    print(atr)


print(platform())
print(platform(1))
print(platform(0, 1))
print(machine())
print(system())
print(version())
print(processor())
 
