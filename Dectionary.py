def main():
    #Student={'name':"benlaiter djamel",'Age':25,'Salire':0}#name.... is Key
    Student=dict(name="benlaiter djamel",Age=25,Salire=0)
    Student['name']="moumen"
    Student['Domaine']="informatique"
    print(Student)
    del Student['name']
    print(Student['Age'])
    print(Student,type(Student))
    Student.clear()
    print(Student)
if __name__ == '__main__':main()