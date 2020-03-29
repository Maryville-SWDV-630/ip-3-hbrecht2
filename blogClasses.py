class user: 
    def __init__(self, username, password): 
        self.username = username 
        self.password = password
    
    def getUsername(self): 
        username = input ('Enter username:')
        return username 

    def getPassword(self): 
        password = input ('Enter password: ')
        return password 

    def verifyLogin(self):
        #I am still working on this method for verifying the login information
        username = self.getUsername()
        password = self.getPassword()
        if password == self.password: 
            print ("You have successfully logged in.\n")
        else:
            print ("Password incorrect. Please try again.\n")
            self.verifyLogin()
            
class admin(user): 
    def __init__(self, username, password, adminNo, blogsWritten = []):
        super().__init__(username, password)
        self.adminNo = adminNo
        self.blogsWritten = blogsWritten
        
    def createBlogPost(self):
        title = input("What is the name of your blog post?")
        self.blogsWritten.append(title)
            
    def deleteBlogPost(self):
        title = input("What is the name of the blog post you would like to delete?")
        index = self.blogsWritten.index(title)
        self.blogsWritten.pop(index)

class reader(user):
    def __init__(self, username, password, readerNo, yourList = []):
        super().__init__(username, password)
        self.readerNo = readerNo
        self.yourList = yourList
        
    def addComment(self):
        comment = input("Commment here..")
        
    def addBlogToYourList(self):
        blogTitle = str(input("Which blog do you want to add to your list?"))
        self.yourList.append(blogTitle)
        
        
def main():
    author = admin("author1", "pass1", "9090")
    author.verifyLogin()
    author.createBlogPost()
    author.createBlogPost()
    author.deleteBlogPost()
    
    blogReader = reader("reader1", "pass2", "4040")
    blogReader.verifyLogin()
    blogReader.addComment()
    blogReader.addBlogToYourList()
    
main()
        

