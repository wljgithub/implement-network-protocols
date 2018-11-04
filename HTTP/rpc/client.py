import xmlrpc.client
import time

s = xmlrpc.client.ServerProxy('http://localhost:8000')
t=time.time()
print(s.pow(2,3))  # Returns 2**3 = 8
print(time.time()-t)
print(s.add(2,3))  # Returns 5
print(s.mul(5,2))  # Returns 5*2 = 10

# Print list of available methods
print(s.system.listMethods())

input()
print(s.add(2,3))  # Returns 5
print(s.mul(5,2))  # Returns 5*2 = 10

input()

