import csv
field_name=['No','Company','Car model']
car=[
    {'No':1,'Company':'Ferrari','Car model':'GH'},
    {'No':2,'Company':'BMW','Car model':'X5'},
    {'No':3,'Company':'Maruti Suzuki','Car model':'Swift'},
    {'No':4,'Company':'Audi','Car model':'RS7'},
    {'No':5,'Company':'Toyota','Car model':'Fortuner'}
]
with open('car.csv','w',newline='') as csvfile:
    write=csv.DictWriter(csvfile,fieldnames=field_name)
    write.writeheader()
    write.writerows(car)
with open('car.csv',newline='')as csvfile:
    d=csv.reader(csvfile)
    for r in d:
        print(','.join(r))
        print(r)