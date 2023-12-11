#Name: Afsana Nawrozi
#Prog Purpose: This program reads in a hotel data file, performs calculations, and creates an HTML file for the results

import datetime

############ define rate tuples ############

#            SR  DR  SU
#             0   1   2
ROOM_RATES = (195,250,350)

#           s-tax   occ-tax
#              0      1
TAX_RATES = (0.065,0.1125)
 
########### define files and list ############
infile = "emerald.csv"
outfile = "emerald-web-page.html"

guest = [] 

############ define program functions ############
def main():
    read_in_guest_file()
    perform_calculations()
    open_out_file()
    create_output_html()
            
def read_in_guest_file():
    guest_data = open(infile, "r")
    guest_in   = guest_data.readlines()
    guest_data.close()

    #### split the data and insert into list called: guest
    for i in guest_in:
        guest.append(i.split(","))
        

def perform_calculations():
    global grandtotal
    grandtotal=0
    
    for i in range(len(guest)):
            room_type = str(guest[i][2])
            num_nights = int(guest[i][3])

            if room_type =="SR":
                subtotal = ROOM_RATES[0] * num_nights
#STUDENTS: COMPLETE THESE elif AND else statements
            elif room_type == "DR":
                subtotal = ROOM_RATES[1] * num_nights
            elif room_type == "SU":
                subtotal = ROOM_RATES[2] * num_nights

            else:
                print(f"Invalid room type for guest {i+1}: {room_type}")
                subtotal = 0 
                
                
#STUDENTS: COMPLETE THESE CALCULATIONS

            sales_tax  = subtotal * TAX_RATES[0]
            occupancy_tax = subtotal * TAX_RATES[1]
            total     = subtotal + sales_tax + occupancy_tax
            grandtotal += total
        
#STUDENTS: ADD THE REST OF THE append statements after this one       
            guest[i].append(subtotal)
            guest[i].append(sales_tax)
            guest[i].append(occupancy_tax)
            guest[i].append(total)

def open_out_file():    
    global f
    f = open(outfile, 'w')
    f.write('<html> <head><title> Emerald Beach Hotel & Resort </title>\n')
    f.write('<style> td{text-align: right} </style> </head>\n')
    f.write('<body style ="background-image: url(wp-beach.png); background-color: #E6D3B3; ">\n')
    
def create_output_html():
    global f
    
    currency="8,.2f"
    today = str(datetime.datetime.now())
    day_time = today[0:16]

    tr = '<tr><td>'
    td = '</td><td>'
    endtr = '</td></tr>\n'

    f.write('\n<table border="3" style ="background-color: #7995AB;  font-family: arial; margin: auto;">\n')
    f.write('<tr><td colspan = 8 style=text-align:center>\n')
    f.write('<h2>Emerald Beach Hotel & Resort</h2></td></tr>')
    f.write('<tr><td colspan=8>'+day_time)
    f.write('<tr><th>Last Name</th><th>First Name</th><th>Room Code</th><th>Nights</th><th>Suntotal</th><th>Sales Tax</th><th>Occupancy Tax</th><th>Total</th></tr>\n')
    
    for i in range(len(guest)):
        f.write(tr + guest[i][0] + td + guest[i][1] + td + guest[i][2] + td + guest[i][3] + td +
        (f"{float(guest[i][4]):{currency}}" if len(guest[i]) > 4 else '') + td +
        (f"{float(guest[i][5]):{currency}}" if len(guest[i]) > 5 else '') +
        td + (f"{float(guest[i][6]):{currency}}" if len(guest[i]) > 6 else '') +
        td + (f"{float(guest[i][7]):{currency}}" if len(guest[i]) > 7 else '') + endtr)
    f.write  ('<tr><td colspan=7>'
                  f"Grand Total</td><td>{grandtotal:{currency}}</td></tr>\n")  
    f.write('</table><br />')

    f.write("</body></html>")
    f.close()
    print('Open ' + outfile + ' to view data.')

##call on main program to execute##
main()
