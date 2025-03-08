class rbi:
    def homeloan(self):
        print("tske loan")
    def roi(self):
        print("roi is good")
class cbi:
    def homeloan(self):
        print("take loan")
    def roi(self):
        print("roi is bad")
class sbi(rbi,cbi):
    def homeloan(self):
        print("dont taek")
    def roi(self):
        print("roi is 45")
obj=sbi()
obj.homeloan()
obj.roi()