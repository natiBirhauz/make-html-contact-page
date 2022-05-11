import names
import random as r
import string
for i in range (0,100):
    print ("<tr>")
    print ("<td>"+names.get_full_name()+"<td>")
    print("<td>05" + str(r.choice([0, 2, 4]))+ str(r.randint(0000000, 9999999)).zfill(7)+"</td>")
    print("<td>"+''.join(r.choice(string.ascii_letters) for _ in range(7)) + r.choice(["@gmail.com","@yahoo.com"])+"</td>")
    print ("</tr>")