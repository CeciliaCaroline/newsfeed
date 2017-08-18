class application (object):
    def __init__(self ) :
        self.users=[] 
        

     def adduser(self,user):
         self.users.append(user)
          

         return "User added succesfully"
    
    def updateuser(self,id,user):
            self.users[id]= user
         return "User updated succesfully"


          




