total_seats=[1,2,3,4,5,6,7,8,9,10]
ticket_price=200

while True:
    print("------ BUS TICKET BOOKING SYSTEM ------\n")
    print("1. Book Ticket")
    print("2. View Seat Availability")
    print("3. Cancel Ticket")
    print("4. Exit")
    choices=[1,2,3,4]
    ch=int(input("\nEnter your choice: "))
    if(ch not in choices):
        print("Invalid choice")
        continue

    if(ch==1):
        passenger_name=input("Enter passenger name: ")
        age=int(input("enter passenger age: "))
        print("\nAvailable seats: ")
        for i in range(1,len(total_seats)+1):
            if(i in total_seats):
                print(i,end=" ")
        seat_number=int(input("\nEnter Seat Number: "))
        if(seat_number in total_seats):
            if(age>=60):
                ticket_price*=0.8
                print("\nSenior citizen discount applied.")
                total_seats.remove(seat_number)
                print("\nTicket Booked Successfully")
                print("Seat Number: ",seat_number)
                print("Final Ticket Price: ",ticket_price)

            else:
                ticket_price=200
                total_seats.remove(seat_number)
                print("\nTicket Booked Successfully")
                print("Seat Number: ",seat_number)
                print("Final Ticket Price: ",float(ticket_price))
        else:
            print("\nSeat not available. Please choose another seat.")

    elif(ch==2):
        print("\nAvailable seats: ")
        for i in total_seats:
                print(i,end=" ")
        print("\n")

    elif(ch==3):
        seat_number=int(input("\nEnter Seat Number to cancel: "))
        if(seat_number>0 and seat_number<=10):
            if(seat_number not in total_seats):
                total_seats.append(seat_number)
                print("\nTicket Cancelled Successfully")
            else:
                print("\nSeat number not booked. Cannot cancel.")
        else:
            print("\nInvalid seat number. Please enter a valid seat number.")

    elif(ch==4):
        print("Thank you for using Bus Ticket Booking system")
        break




