# Demonstrate how to access and perform operations on a main file
#run the MODULE of MAIN FILE and import mainfile as a library 

import mainprog as x 
x.create("kamalesh",25)
x.create("src",70,3600) 
x.read("kamalesh")
x.read("src")
x.create("kamalesh",50)
x.modify("kamalesh",55)
x.delete("kamalesh")
t1=Thread(target=(create or read or delete),args=(key_name,value,timeout))
t1.start()
t1.sleep()
t2=Thread(target=(create or read or delete),args=(key_name,value,timeout))
t2.start()
t2.sleep()
#and so on upto tn
