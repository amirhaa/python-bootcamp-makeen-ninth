# We have URegisteredUser and RegisteredUser and Admin in our site.

# All type of user can view blog posts, but only registered and admin users can write comments and also only admins can delete comments.

# Model an object oriented design that users can view posts, comments and delete comments.

# Note: we should print out each user's username and name in each comment.

# Note: If user cannot comments or cannot delete a comment prints and error to him/her and inform that cannot do the action.

class User:

    def __init__(self, name, username):
        self.name = name
        self.username = username

    def view_posts(self): return True

    def write_comment(self, comment): return comment

    def delete_comment(self): return False

class UnRegisteredUser(User):
    
    def write_comment(self, comment): return "Sorry, you cannot do this action"

class RegisteredUser(User):

    def write_comment(self, comment):
        return f"{super().write_comment(comment)}\nwrited by {self.name} @{self.username}"

class Admin(RegisteredUser):
    def delete_comment(self):
        return True


# p1 = RegisteredUser(name="Mana", username="Manash")
# print(p1.write_comment(":)))))"))
# p2 = UnRegisteredUser(name= "Ali", username="Alish")
# print(p2.write_comment("Hey"))
# p3 = Admin(name="Amir", username="Amir12")
# print(p3.write_comment("Nice"))
# print(p3.delete_comment())
# print(p2.delete_comment())

        