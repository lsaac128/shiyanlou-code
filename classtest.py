class UserData:
    def __init__(self, age, name):
        self._name = name
        self.age = age

    def __repr__(self):
        return 'ID:{} Name:{}'.format(self.age, self._name)


class NewUser(UserData):
    group = 'shiyanlou-louplus'
    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    @classmethod
    def get_group(cls):
        return cls.group

    @staticmethod
    def format_userdata(id, name):
#        print("{}'s id is {}".format(name, id))
        return "{}'s id is {}".format(name, id)


if __name__ == '__main__':
    print(NewUser.get_group())
    print(NewUser.format_userdata(109,'Lucy'))
