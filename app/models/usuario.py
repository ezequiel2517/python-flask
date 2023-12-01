class Usuario:
    def __init__(self, user_id, users_following):
        self.user_id = user_id
        self.users_following = users_following

    def countSeguidores(self):
        return len(self.users_following)
