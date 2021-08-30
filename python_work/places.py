places = ["greece", "argentina", "japan", "brazil", "italy"]
print(places)

#sort() = permanently rearranges list alphabetically
#sort()reverse=True = permanently rearranges list alphabetically backwards

#sorted() = arranges list in alphabetical order temporarily.
print(sorted(places))
print(places)

#reverse() = reverse the order of the list temporarily. Use it again to go back to original list
places.reverse()
print(places)

# len() = gives you the length of a list
print(len(places))

print(places[6])