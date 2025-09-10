class Person :
    """
    Class Person untuk membuat object Person
    """
    name = "Joni"
    age = 20
    def __init__(self, nama):
        self.nama = nama
        self.introduce()
        
    def __del__(self):
        print(f"Object {self.nama} is being destroyed")
        
    def introduce(self):
        print(f"Hi my name is {self.nama}")
    
    def introduceAgain(self):
        self.introduce()
        print("nice to meet you")

class Employee:
    def __init__(self,name,age,employeeId,salary):
        self.name = name
        self.age = age
        self.employeeId = employeeId
        self.__salary = salary
        
    def getSalary(self):
         return self.__salary
    
    def working(self):
        return(f"{self.name} is working")   

class Manager(Employee):
    def __init__(self,name,age,emploteeId,salary,department):
        super().__init__(name, age, emploteeId, salary)
        self.department = department
    
    def working(self):
        return(f"{self.name} is managing the {self.department} department")
    
class Karyawan:
    def __init__(self, nama, gaji):
        self.nama = nama
        self.gaji = gaji

    def tampilkan_info(self):
        print(f"Nama: {self.nama}, Gaji: {self.gaji}")
        
class Rekening:
    def __init__(self, saldo):
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, saldo_baru):
        if saldo_baru > 0:
            self.__saldo = saldo_baru
        else:
            print("Saldo harus lebih dari 0")

if __name__ == "__main__":
    
    r = Rekening(10000)
    print(r.get_saldo())       
    r.set_saldo(20000)
    print(r.get_saldo())       
    r.set_saldo(-5000)        

    employee1 = Employee("John",25,1234,5000)
    print(employee1.name)
    print(employee1.getSalary())
    print(employee1.working())
    manager1 = Manager("David",30,5432,10000,"IT")
    print(manager1.working())
    print(Person.name)        
    print(Person.__dict__)
    print(Person.__doc__)
    print(Person.__name__)
    person1 = Person("John")
    person1 = Person("David")
    print(person1.nama)
    person1.introduce()
    person1.introduceAgain()
    del person1
    person2 = Person("David")
    