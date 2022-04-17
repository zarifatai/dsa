class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for x in range(self.MAX)]
    

    def get_hash(self, key):
        total = 0
        for char in key:
            total += ord(char)
        return total % self.MAX

    
    def __getitem__(self, key):
        h = self.get_hash(key)
        if self.arr[h] is None:
            return
        
        for i in range(h, self.MAX):
            x = i % self.MAX
            element = self.arr[x]
            if element is None:
                return
            if element[0] == key:
                return element[1]
        # for k, v in self.arr[h]:
        #     if k == key:
        #         return v


    def __setitem__(self, key, value):
        h = self.get_hash(key)

        if self.arr[h] is None:
            self.arr[h] = (key, value)
        else:
            for i in range(h+1, self.MAX):
                x = i % self.MAX
                if self.arr[x] is None:
                    self.arr[x] = (key, value)
                    break
                if self.arr[x][0] == key:
                    self.arr[x] = (key, value)
                    break
            else:
                print("Hashmap is full!")


#        found = False
#        for idx, kv in enumerate(self.arr[h]):
#            k, v = kv
#            if k == key:
#                found = True
#                self.arr[h][idx] = (k, v)
#                break
#    
#        if not found:
#            self.arr[h].append((key, value))

t = HashTable()
t["test1"] = 1
t["test2"] = 2
t["test3"] = 3
t["test4"] = 4
t["test5"] = 5
t["test6"] = 6
t["test7"] = 7
t["test8"] = 8
t["test9"] = 1
t["test10"] = 2
t["test11"] = 3
# t["test12"] = 4
# t["test13"] = 5
# t["test14"] = 6
# t["test15"] = 7
# t["test16"] = 8
