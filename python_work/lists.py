lists = ["carol", "jack", "bondes"]
print("Hey " + lists[0].title() + " Come to my dinner?" )
print("Hey " + lists[1].title() + " Come to my dinner?" )
print("Hey " + lists[2].title() + " Come to my dinner?" )

not_coming = "jack" 
lists.remove("jack")
print(not_coming.title() + " isn't coming")

print(lists)
lists.insert(1, "tijuana")
print(lists)