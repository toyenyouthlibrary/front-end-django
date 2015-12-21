class User:
    @staticmethod
    def create(username, firstname, lastname, address, phone, email, birth):
        user = User()
        user.username = username
        user.firstname = firstname
        user.lastname = lastname
        user.address = address
        user.phone = phone
        user.birth = birth
        user.email = email

        return user

    """
    TODO: Parse JSON and return a User object
    """
    @staticmethod
    def parse(json):
        return User()
