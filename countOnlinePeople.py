# Short version
def online_count(people):
    return sum(1 for p in people.values() if p == 'online')

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
    "Taki": "online"
}

print(online_count(statuses))

# Long version 
def online_count(status_dict):
    online_num = 0
    for x in status_dict.values():
        if x == "online":
            online_num += 1
    return online_num