#person={
    #"name": "Sir Nisper",
    #"Age": 23,
    #"email":"sirnisper@gmail.com"
    
    #}

#print(person["email"])

#add/print
#person["country"] = "Kenya"
#person["phone"] = "0746874327"

#Delete
# person["email"]

#rint(person)


class HashMap:
    def __init__(self,size):
        self.size=size
        self.table=[[] for _ in range(size)]
    def put(self,key,value):
        h=hash(key) % self.size# Get Index
        for pair in self.table[h]: #search in th bucket
            if pair[0] == key:
               pair[1]=value #update if key already exist
            return
        self.table[h].append([key,value]) #add new key-value pair
    def get(self,key):
        h=hash(key) % self.size
        for pair in self.table[h]:
            if pair[0] == key:
                return pair[1]
        return None
hm= HashMap(10)
hm.put("name","Sir Nisper")
hm.put("age", 23)

print(hm.get("name"))  # Output: Sir Nisper
print(hm.get("age"))   # Output: 23  
print(hm.get("email")) # Output: None (since "email" key does not exist) 