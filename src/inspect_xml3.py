particle = root[0]

print("Track length:", particle.attrib)

print("\nChildren:")

for child in particle:
    print(child.tag)
    print(child.attrib)
    break
