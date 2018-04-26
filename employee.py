class Employee:
    def __init__(self, eid, name, pay):
        self.eid=eid
        self.name=name
        self.pay=pay
    def __repr__(self):
        return "employee: id: {}; name: {};paid: {}".format(self.eid,self.name,self.pay)

if __name__== '__main__':
    e1=Employee('1001','nguyen van teo',10000)
    print(e1)
