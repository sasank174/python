class Mother:
    def color(self):
        print("Color Is From Mother ")

class Father:
    def height(self):
        print("Height Is From Father ")

class Son(Mother,Father):
    def qualifications(self):
        self.color()
        self.height()
        print("Qualifications From Son ")

'''Calling '''
s=Son()
s.qualifications()
