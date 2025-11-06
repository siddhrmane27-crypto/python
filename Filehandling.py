f = open("demo.txt", "w")  
f.write("My name is Abhishek...")
f.close()


f = open("demo.txt", "r") 
data = f.read()
print("File have :", data)
f.close()


f = open("demo.txt", "a")
f.write("I am an Engineering Student...")
f.close()



