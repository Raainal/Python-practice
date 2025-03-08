class rbi:
    def homeloan_ROI(self):
        print("Home loan rate of interest is 7.5%")

    def carloan_ROI(self):
        print("Car loan rate of interest is 8%")
    
class sbi(rbi):
    def homeloan_ROI(self):
        print("Home loan rate of interest is 7%")
        super().homeloan_ROI()
# Method overloading is not supported in Python. However, we can achieve method overloading by using default arguments.
obj=sbi()
obj.homeloan_ROI()
obj.carloan_ROI()
# Output: Home loan rate of interest is 7%
    