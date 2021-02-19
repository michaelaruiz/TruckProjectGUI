
import tkinter as tk

from tkinter import *

from tkinter import ttk
import csv
import package
from distance import Distances
from hashTable import HashTable
from truck import Trucks
import datetime
from datetime import datetime



with open('WGUPSPackageFile1.csv', 'r') as csvfile:
    csv_file = csv.reader(csvfile, delimiter=',')  # reads the CSV package file
    list_of_packages = list(csv_file)
    # print(list_of_packages[0][0])
    pH = HashTable()  # 15 - creates a hashtable object by calling the HashTable class

    distances = Distances()
    trucks = Trucks()  # creates truck object by calling Trucks class

    # creates lists of each package attribute

    Package_IDs = []
    Addresses = []
    Cities = []
    States = []
    Zips = []
    Delivery_Deadlines = []
    Weight = []
    Notes = []
    Status = []
    Departure_time = []

    # reads the package csv and creates attributes for each package
    for row in list_of_packages:  # space time complexity is O(N)
        pid = row[0].strip()
        address = row[1]
        city = row[2]
        state = row[3]
        zipcode = row[4]
        deadline = row[5]
        weight = row[6]
        note = row[7]
        status = row[8]
        departure_time = row[9]

        # appends each value to respective lists
        Package_IDs.append(pid)
        Addresses.append(address)
        Cities.append(city)
        States.append(state)
        Zips.append(zipcode)
        Delivery_Deadlines.append(deadline)
        Weight.append(weight)
        Notes.append(note)
        Status.append(status)
        Departure_time.append(departure_time)

        p = package.Package(pid, address, city, state, zipcode, deadline,
                            weight, note)  # creates the package object using the package class

        pH.get(pid)  # look up the package by the id
        pH.insert(pid, p)  # inserts the packages into the hashtable

    # gets the package object using the ids using the hashtable and creates package objects for each

    # p37.status = 'At Hub'
    # print(p37)
    firstTruckTripPackages = [pH.get('1'), pH.get('7'), pH.get('8'), pH.get('10'), pH.get('11'), pH.get('12'),
                              pH.get('13'), pH.get('14'), pH.get('15'), pH.get('16'), pH.get('19'), pH.get('20'),
                              pH.get('29'), pH.get('30'), pH.get('34'), pH.get('37')]
    # print(p1.pid)
    # puts the packages into the first truck
    # print(packageHashTable.update_status('1', 'At HUB'))

    firstTruckTripPAddresses = []
    for item in firstTruckTripPackages:
        firstTruckTripPackageA = item.address
        firstTruckTripPAddresses.append(firstTruckTripPackageA)
        # creates a list of addresses of each package in the first truck
        # space time complexity of O(N)

    secondTruckTripPackages = [pH.get('3'), pH.get('6'), pH.get('18'), pH.get('25'), pH.get('26'), pH.get('31'),
                               pH.get('36'), pH.get('38'), pH.get('40')]
    # puts the package object into the second truck

    secondTruckTripPAddresses = []
    for item in secondTruckTripPackages:
        secondTruckTripPackageA = item.address
        secondTruckTripPAddresses.append(secondTruckTripPackageA)
        # creates a list of addresses of each package in the second truck
        # space time complexity of O(N)

    thirdTruckTripPackages = [pH.get('2'), pH.get('4'), pH.get('5'), pH.get('9'), pH.get('17'), pH.get('21'),
                              pH.get('22'), pH.get('23'), pH.get('24'), pH.get('27'), pH.get('28'), pH.get('32'),
                              pH.get('33'), pH.get('35'), pH.get('39')]
    # puts the package object into the third truck

    thirdTruckTripPAddresses = []
    for item in thirdTruckTripPackages:
        firstTruckSecondTripPackageA = item.address
        thirdTruckTripPAddresses.append(firstTruckSecondTripPackageA)
        # creates a list of addresses of each package in the second truck
        # space time complexity of O(N)

    first_location = 'HUB'

    # creates list of addresses from the optimized list of addresses from truck 1
    first_truck_delivery = trucks.shortest_distance_calculation_truck1_addresses(
        firstTruckTripPAddresses, firstTruckTripPackages, first_location)

    # creates list of addresses from the optimized list of addresses from truck 2
    second_truck_delivery = trucks.shortest_distance_calculation_truck2_addresses(
        secondTruckTripPAddresses, secondTruckTripPackages, first_location)

    # creates list of addresses from the optimized list of addresses from truck 3
    third_truck_delivery = trucks.shortest_distance_calculation_truck3_addresses(
        thirdTruckTripPAddresses, thirdTruckTripPackages, first_location)

    # lines 166-168 update each package departure time
trucks.update_package_departure_from_hub_time_first_truck(firstTruckTripPackages)
trucks.update_package_departure_from_hub_time_second_truck(secondTruckTripPackages)
trucks.update_package_departure_from_hub_time_third_truck(thirdTruckTripPackages)

# lines 167-169 update each package delivery time to the time they are delivered
trucks.update_package_delivery_time_first_truck(first_truck_delivery, firstTruckTripPackages, 'HUB')
trucks.update_package_delivery_time_second_truck(second_truck_delivery, secondTruckTripPackages, 'HUB')
trucks.update_package_delivery_time_third_truck(third_truck_delivery, thirdTruckTripPackages, 'HUB')





def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("600x500")
    login_screen.configure(bg='white')
    Label(login_screen, text="Please enter details below to login", bg='lightblue', width="300", height="2", font=("Baghdad", 13)).pack()
    Label(login_screen, text="").pack()
    # Label(text="Select Your Choice", bg="lightblue", width="300", height="2", font=("Baghdad", 13)).pack()
    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_login_entry
    global password_login_entry

    Label(login_screen, text="Username", bg='lightblue', font=("Baghdad", 13)).pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password", bg='lightblue', font=("Baghdad", 13)).pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show='*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()


# Implementing event on register button



def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    if username1 =="admin":
        if password1 == "admin":
            login_sucess()

        else:
            password_nr()

    else:
        user_nf()



def login_sucess():
    global top
    global gender_input
    global freq_input
    gender_input = StringVar()
    freq_input = StringVar()
    top = Toplevel(login_screen)
    top.title("Home")
    top.geometry("770x600")
    top.configure(bg='white')
    Label(top, text="Home", bg='lightblue', width="300", height="2", font=("Baghdad", 15, "bold")).pack()
    slabel1 = Label(top, text="Get Package Information", height=0, width=0, font=("Baghdad", 13))
    slabel1.configure(bg='aliceblue')
    slabel1.place(x=20, y=90)

    slabel2 = Label(top, text="Get Status of all packages at a specific time", height=0, width=0,
                    font=("Baghdad", 13))
    slabel2.configure(bg='aliceblue')
    slabel2.place(x=20, y=130)


    remote_button = Button(top, text="Get", width=11, height=1, command=get_package)
    remote_button.pack(padx=5, pady=20)
    remote_button.place(x=400, y=90)
    remote_button.configure(bg="#ffdddd", background='red')

    mc_cons_button = Button(top, text="Status", width=10, height=1, command=package_status)
    mc_cons_button.pack(padx=5, pady=20)
    mc_cons_button.place(x=400, y=130)
    mc_cons_button.configure(bg="#ffdddd", background='red')

    exit_button = Button(top, text="Exit", command=end_ls)
    exit_button.pack(padx=5, pady=100)
    exit_button.place(x=550, y=385)


def package_status():
    global tree
    global time_status_entry

    win = tk.Toplevel(top)
    win.title("Get Status of All Packages")
    win.geometry("550x500")
    win.configure(bg='White')

    tree = ttk.Treeview(win, selectmode='browse')
    tree.pack(side='left')
    tree.place(x=200,y=200)

    vsb = ttk.Scrollbar(win, orient="vertical", command=tree.yview)
    vsb.pack(side='right', fill='y')
    vsb.place(x=404,y=200, height=200)

    tree.configure(yscrollcommand=vsb.set)

    tree["columns"] = ("1", "2")
    tree['show'] = 'headings'
    tree.column("1", width=100, anchor='c')
    tree.column("2", width=100, anchor='c')

    tree.heading("1", text="ID")
    tree.heading("2", text="Status")

    time_status_label = Label(win, text="Enter time(in 'HH:MM:SS Format)", height=0, width=0, font=("Baghdad", 13))
    time_status_label.configure(bg='lightblue')
    time_status_label.place(x=35, y=100)

    time_status_entry = Entry(win, width=20, bg="white")
    time_status_entry.pack()
    time_status_entry.place(x=250, y=100)


    myButton = Button(win, text='enter', command=get_package_statuses)
    myButton.pack()
    myButton.place(x=250, y=130)

def get_package_statuses():
    global p_time
    p_time = time_status_entry.get()

    user_input_input_time = p_time
    convert_user_input_time = datetime.strptime(user_input_input_time,
                                                '%H:%M:%S')  # converts time inputted to datetime
    for p in firstTruckTripPackages:  # checks status of the first truck
        departure_time = p.departure_time
        delivery_time = p.delivery_time
        if departure_time >= convert_user_input_time:  # checks if package is at the HUB
            p.status = 'At HUB'
            tree.insert("",'end',text="L2",values=(str(p.pid), str(p.status)))
        elif delivery_time <= convert_user_input_time:  # checks if package has been delivered
            p.status = 'Delivered'
            tree.insert("",'end',text="L2",values=(str(p.pid), str(p.status)))
        elif departure_time <= convert_user_input_time < delivery_time:  # checks if package is in transit
            p.status = 'In transit'
            tree.insert("",'end',text="L2",values=(str(p.pid), str(p.status)))
    for p in secondTruckTripPackages:  # checks status of the second truck
        departure_time = p.departure_time
        delivery_time = p.delivery_time
        if departure_time >= convert_user_input_time:  # checks if package is at the hub
            p.status = 'At HUB'
            tree.insert("",'end',text="L2",values=(str(p.pid), str(p.status)))
        elif delivery_time <= convert_user_input_time:  # checks if package has been delivered
            p.status = 'Delivered'
            tree.insert("",'end',text="L2",values=(str(p.pid), str(p.status)))
        elif departure_time <= convert_user_input_time < delivery_time:  # checks if package is in transit
            p.status = 'In transit'
            tree.insert("",'end',text="L2",values=(str(p.pid), str(p.status)))
    for p in thirdTruckTripPackages:  # checks status of third truck
        departure_time = p.departure_time
        delivery_time = p.delivery_time
        if departure_time >= convert_user_input_time:  # checks if package is at the hub
            p.status = 'At HUB'
            tree.insert("",'end',text="L2",values=(str(p.pid), str(p.status)))
        elif delivery_time <= convert_user_input_time:  # checks if package has been delivered
            p.status = 'Delivered'
            tree.insert("",'end',text="L2",values=(str(p.pid), str(p.status)))
        elif departure_time <= convert_user_input_time < delivery_time:  # checks if package is in transit
            p.status = 'In transit'
            tree.insert("",'end',text="L2",values=(str(p.pid), str(p.status)))




def get_package():
    global root1
    global clicked1
    global id_entry
    global time_label
    global time_entry
    root1 = Toplevel(top)
    root1.title("Get Package Information")
    root1.geometry("550x500")
    root1.configure(bg='White')
    # Label(top1, text=" Screen").pack()
    slabel1 = Label(root1, text="Enter Package ID", height=0, width=0, font=("Baghdad", 13))
    slabel1.configure(bg='lightblue')
    slabel1.place(x=35, y=65)


    id_entry = Entry(root1, width=20, bg="white")
    id_entry.pack()
    id_entry.place(x=250, y=65)

    time_label = Label(root1, text="Enter time (in 'HH:MM:SS Format)", height=0, width=0, font=("Baghdad", 13))
    time_label.configure(bg='lightblue')
    time_label.place(x=35, y=100)

    time_entry = Entry(root1, width=20, bg="white")
    time_entry.pack()
    time_entry.place(x=250, y=100)


    myButton = Button(root1, text='enter', command=get_package_information)
    myButton.pack()
    myButton.place(x=250, y=130)

# def getID():
#     global id
#     global p_time
#     id = id_entry.get()
#     p_time = time_entry.get()



def get_package_information():
    global id
    global p_time
    id = id_entry.get()
    p_time = time_entry.get()
    # myLabel = Label(root1, text='hi').pack()
    for package_id_input in firstTruckTripPackages:  # gets package information from each package in truck 1
        if package_id_input.pid == id:#
            departure_time = package_id_input.departure_time
            delivery_time = package_id_input.delivery_time
            user_input_time = p_time
            convert_user_input_time = datetime.strptime(user_input_time, '%H:%M:%S')
            if departure_time >= convert_user_input_time:  # checks if package is at hub and then sets
                # value in hashtable
                package_id_input.status = 'At HUB'
                # myLabel = Label(root1, text='hi').pack()
                myLabel = Label(root1, text='Package ID: ' + str(package_id_input.pid) + '\n' + 'Address: ' + str(package_id_input.address) + '\n' + 'City: '+
                                            str(package_id_input.city) + '\n' + 'State: ' + str(package_id_input.state) + '\n' + 'Zipcode: ' +
                                            str(package_id_input.zip_code) + '\n' +
                                            'Deadline: ' + str(package_id_input.deadline) + '\n' + 'Weight: '+ str(package_id_input.weight) + '\n' + 'Notes: ' +
                                            str(package_id_input.note) + '\n' + 'Status: '+ str(package_id_input.status) + '\n' + 'Departure Time: ' +
                                            str(package_id_input.departure_time) + '\n' + 'Delivery Time: ' + str(package_id_input.delivery_time))
                myLabel.pack()
                myLabel.place(x=150, y=160)
            elif departure_time <= convert_user_input_time:  # checks if package is in transit
                # then sets in hashtable
                if convert_user_input_time < delivery_time:
                    package_id_input.status = 'In transit'
                    myLabel = Label(root1, text='Package ID: ' + str(package_id_input.pid) + '\n' + 'Address: ' + str(package_id_input.address) + '\n' + 'City: '+
                                                str(package_id_input.city) + '\n' + 'State: ' + str(package_id_input.state) + '\n' + 'Zipcode: ' +
                                                str(package_id_input.zip_code) + '\n' +
                                                'Deadline: ' + str(package_id_input.deadline) + '\n' + 'Weight: '+ str(package_id_input.weight) + '\n' + 'Notes: ' +
                                                str(package_id_input.note) + '\n' + 'Status: '+ str(package_id_input.status) + '\n' + 'Departure Time: ' +
                                                str(package_id_input.departure_time) + '\n' + 'Delivery Time: ' + str(package_id_input.delivery_time))
                    myLabel.pack()
                    myLabel.place(x=150, y=160)
                else:  # checks if package is delivered and then sets value in hashtable
                    package_id_input.status = 'Delivered'
                    myLabel = Label(root1, text='Package ID: ' + str(package_id_input.pid) + '\n' + 'Address: ' + str(package_id_input.address) + '\n' + 'City: '+
                                                str(package_id_input.city) + '\n' + 'State: ' + str(package_id_input.state) + '\n' + 'Zipcode: ' +
                                                str(package_id_input.zip_code) + '\n' +
                                                'Deadline: ' + str(package_id_input.deadline) + '\n' + 'Weight: '+ str(package_id_input.weight) + '\n' + 'Notes: ' +
                                                str(package_id_input.note) + '\n' + 'Status: '+ str(package_id_input.status) + '\n' + 'Departure Time: ' +
                                                str(package_id_input.departure_time) + '\n' + 'Delivery Time: ' + str(package_id_input.delivery_time))
                    myLabel.pack()
                    myLabel.place(x=150, y=160)
    for package_id_input in secondTruckTripPackages:  # gets package information from each package in truck 1
        if package_id_input.pid == id:#
            departure_time = package_id_input.departure_time
            delivery_time = package_id_input.delivery_time
            user_input_time = p_time
            convert_user_input_time = datetime.strptime(user_input_time, '%H:%M:%S')
            if departure_time >= convert_user_input_time:  # checks if package is at hub and then sets
                # value in hashtable
                package_id_input.status = 'At HUB'
                # myLabel = Label(root1, text='hi').pack()
                myLabel = Label(root1, text='Package ID: ' + str(package_id_input.pid) + '\n' + 'Address: ' + str(package_id_input.address) + '\n' + 'City: '+
                                            str(package_id_input.city) + '\n' + 'State: ' + str(package_id_input.state) + '\n' + 'Zipcode: ' +
                                            str(package_id_input.zip_code) + '\n' +
                                            'Deadline: ' + str(package_id_input.deadline) + '\n' + 'Weight: '+ str(package_id_input.weight) + '\n' + 'Notes: ' +
                                            str(package_id_input.note) + '\n' + 'Status: '+ str(package_id_input.status) + '\n' + 'Departure Time: ' +
                                            str(package_id_input.departure_time) + '\n' + 'Delivery Time: ' + str(package_id_input.delivery_time))
                myLabel.pack()
                myLabel.place(x=150, y=160)
            elif departure_time <= convert_user_input_time:  # checks if package is in transit
                # then sets in hashtable
                if convert_user_input_time < delivery_time:
                    package_id_input.status = 'In transit'
                    myLabel = Label(root1, text='Package ID: ' + str(package_id_input.pid) + '\n' + 'Address: ' + str(package_id_input.address) + '\n' + 'City: '+
                                                str(package_id_input.city) + '\n' + 'State: ' + str(package_id_input.state) + '\n' + 'Zipcode: ' +
                                                str(package_id_input.zip_code) + '\n' +
                                                'Deadline: ' + str(package_id_input.deadline) + '\n' + 'Weight: '+ str(package_id_input.weight) + '\n' + 'Notes: ' +
                                                str(package_id_input.note) + '\n' + 'Status: '+ str(package_id_input.status) + '\n' + 'Departure Time: ' +
                                                str(package_id_input.departure_time) + '\n' + 'Delivery Time: ' + str(package_id_input.delivery_time))
                    myLabel.pack()
                    myLabel.place(x=150, y=160)
                else:  # checks if package is delivered and then sets value in hashtable
                    package_id_input.status = 'Delivered'
                    myLabel = Label(root1, text='Package ID: ' + str(package_id_input.pid) + '\n' + 'Address: ' + str(package_id_input.address) + '\n' + 'City: '+
                                                str(package_id_input.city) + '\n' + 'State: ' + str(package_id_input.state) + '\n' + 'Zipcode: ' +
                                                str(package_id_input.zip_code) + '\n' +
                                                'Deadline: ' + str(package_id_input.deadline) + '\n' + 'Weight: '+ str(package_id_input.weight) + '\n' + 'Notes: ' +
                                                str(package_id_input.note) + '\n' + 'Status: '+ str(package_id_input.status) + '\n' + 'Departure Time: ' +
                                                str(package_id_input.departure_time) + '\n' + 'Delivery Time: ' + str(package_id_input.delivery_time))
                    myLabel.pack()
                    myLabel.place(x=150, y=160)
    for package_id_input in thirdTruckTripPackages:  # gets package information from each package in truck 1
        if package_id_input.pid == id:
            departure_time = package_id_input.departure_time
            delivery_time = package_id_input.delivery_time
            user_input_time = p_time
            convert_user_input_time = datetime.strptime(user_input_time, '%H:%M:%S')
            if departure_time >= convert_user_input_time:  # checks if package is at hub and then sets
                # value in hashtable
                package_id_input.status = 'At HUB'
                # myLabel = Label(root1, text='hi').pack()
                myLabel = Label(root1, text='Package ID: ' + str(package_id_input.pid) + '\n' + 'Address: ' + str(package_id_input.address) + '\n' + 'City: '+
                                            str(package_id_input.city) + '\n' + 'State: ' + str(package_id_input.state) + '\n' + 'Zipcode: ' +
                                            str(package_id_input.zip_code) + '\n' +
                                            'Deadline: ' + str(package_id_input.deadline) + '\n' + 'Weight: '+ str(package_id_input.weight) + '\n' + 'Notes: ' +
                                            str(package_id_input.note) + '\n' + 'Status: '+ str(package_id_input.status) + '\n' + 'Departure Time: ' +
                                            str(package_id_input.departure_time) + '\n' + 'Delivery Time: ' + str(package_id_input.delivery_time))
                myLabel.pack()
                myLabel.place(x=150, y=160)
            elif departure_time <= convert_user_input_time:  # checks if package is in transit
                # then sets in hashtable
                if convert_user_input_time < delivery_time:
                    package_id_input.status = 'In transit'
                    myLabel = Label(root1, text='Package ID: ' + str(package_id_input.pid) + '\n' + 'Address: ' + str(package_id_input.address) + '\n' + 'City: '+
                                                str(package_id_input.city) + '\n' + 'State: ' + str(package_id_input.state) + '\n' + 'Zipcode: ' +
                                                str(package_id_input.zip_code) + '\n' +
                                                'Deadline: ' + str(package_id_input.deadline) + '\n' + 'Weight: '+ str(package_id_input.weight) + '\n' + 'Notes: ' +
                                                str(package_id_input.note) + '\n' + 'Status: '+ str(package_id_input.status) + '\n' + 'Departure Time: ' +
                                                str(package_id_input.departure_time) + '\n' + 'Delivery Time: ' + str(package_id_input.delivery_time))
                    myLabel.pack()
                    myLabel.place(x=150, y=160)
                else:  # checks if package is delivered and then sets value in hashtable
                    package_id_input.status = 'Delivered'
                    myLabel = Label(root1, text='Package ID: ' + str(package_id_input.pid) + '\n' + 'Address: ' + str(package_id_input.address) + '\n' + 'City: '+
                                                str(package_id_input.city) + '\n' + 'State: ' + str(package_id_input.state) + '\n' + 'Zipcode: ' +
                                                str(package_id_input.zip_code) + '\n' +
                                                'Deadline: ' + str(package_id_input.deadline) + '\n' + 'Weight: '+ str(package_id_input.weight) + '\n' + 'Notes: ' +
                                                str(package_id_input.note) + '\n' + 'Status: '+ str(package_id_input.status) + '\n' + 'Departure Time: ' +
                                                str(package_id_input.departure_time) + '\n' + 'Delivery Time: ' + str(package_id_input.delivery_time))
                    myLabel.pack()
                    myLabel.place(x=150, y=160)



def password_nr():
    global incorrect_password
    incorrect_password = Toplevel(login_screen)
    incorrect_password.title("Success")
    incorrect_password.geometry("150x100")
    Label(incorrect_password, text="Invalid Password ").pack()
    Button(incorrect_password, text="OK", command=destroy_pnr).pack()


# Designing popup for user not found

def user_nf():
    global incorrect_user
    incorrect_user = Toplevel(login_screen)
    incorrect_user.title("Success")
    incorrect_user.geometry("150x100")
    Label(incorrect_user, text="User Not Found").pack()
    Button(incorrect_user, text="OK", command=destroy_ius).pack()


def end_ls():
    top.destroy()


def destroy_pnr():
    incorrect_password.destroy()


def destroy_ius():
    incorrect_user.destroy()


def main_screen1():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("600x500")
    main_screen.title("Would you like to Login?")
    main_screen.configure(bg='white')
    Label(text="Select Your Choice", bg="lightblue", width="300", height="2", font=("Baghdad", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command=login).pack()

    main_screen.mainloop()


if __name__ == "__main__":
    main_screen1()