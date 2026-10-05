#Rho at sea level
Rho = 1.225 

#temp at 0km
t0 = 15+273

#pressure at sea level
p0 = 101.325 * 1000

# 
R = 287

# 
g = 9.81

#lapse rate
L = -0.0065 

#solving the temp change
#tropshere end 11km
# return means give the calcuated value back to what called the func

def temp(h):
    if h <= 11000: #is alt less then or equal to 11km
        return t0 + L * h #calcuates temp to 11km
    return t0 + L * 11000 #calcuates temp at 11km
    
# ^^ this func works by saying if height is below 11km then use return t0 + L * h and if its higher use return t0 + L * 11000 which means 
# all alts above 11km get sent back to the 11km return because the temp is constant above 11km

#i tried running t_in in the first eq but cuz its after a return it wont run
    
def pres(h): # we can combine the pressure calc for 11km and under and 11km and above into one
    if h <= 11000:
        return p0 * ((temp(h))/t0) ** (-(g)/(L*R)) #this calcuates the pressure up too 11km 
    else:
        p_in = pres(11000) # intial value of pressure at 11km
        T_in = temp(11000) # intial value of temp for 11km
        return p_in * (2.71828 ** (-g * (h - 11000) / (R * T_in))) #2.71828 = (e) eulers number 
        
# basicly this one works buy using same if below 11km use first eq and if above use second equation that retuns the number for pressure at 11km
# p_in and t_in are needed they store the intial value of each at 11km for the second equation as pressure decreases exponetily 
# so they are needed here so they stay in the loop

def density(h):
    T = temp(h) #means run the func using h
    P = pres(h) #means run the func using h
    return P / (R * T)
    

# f-string for formating the vars as spec in breif
header = (
    f"{'Altitude (m)':>12}" # 12 is the width and in f string > means align to the right 
    f"{'Temperature (K)':>18}"
    f"{'Pressure (Pa)':>18}"
    f"{'Density (kg/m³)':>20}"
)
table = [header] # creates a list containing the header

for altitude in range(0, 20001, 1000): # we used numpy origionaly using np.arange but all this does is start at 0 and go to 200000 increasing by 1000 each time
    T = temp(altitude) # holds Temp array
    P = pres(altitude) # holds Pressure array
    rho = density(altitude) # holds density array
    
    line = (                        # this sets one row of the table according to the widths provided 
        f"{altitude:>12}"
        f"{T:>18.2f}" # .2f shows it as a floating point numb with 2dp
        f"{P:>18.2f}"
        f"{rho:>20.4f}"
    )

    table.append(line) # adds the row to the end of the table list thefore repeats untill all the data given by the range command 
    # which has been calcuated into the components is finished

print("\n".join(table))  # joins (.join(table)) each row with a new line "\n" and prints the table using print 

# whatever is before (.join(table)) is put between each item 

with open("isa_atmosphere_question_1.txt", "w") as file_1: 
    file_1.write("\n".join(table))
    #open generates a file called ("isa_atmosphere_question_1.txt") if it doesnt already exist "W" means write mode so tells pytjon to write into the file
     #if the file already exists "w" will overide
    # as file basicly calls the file that u just opened file so thats how u refer to it in this workspace
    # with closes the file after the data is written in so we dont have to write file.close()
    # write works the same way as print is write all the data to the file and we use the same format ("\n".join(table)