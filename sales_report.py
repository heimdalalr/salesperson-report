"""Generate sales report showing total melons each salesperson sold."""


salespeople = [] # creates an empty list for sales people
melons_sold = [] #creates and empty list for melons sold

f = open('sales-report.txt') #variable f opens the sales-report document
for line in f: #loops the file opened with variable f
    line = line.rstrip() #returns a copy of the string by removing the trailing characters specified as argument
    entries = line.split('|') #split method divides a string into a list

    salesperson = entries[0] #sales people are in the 0 index of the list
    melons = int(entries[2]) #amount of melons sold are in the third index of the list

    if salesperson in salespeople:
        position = salespeople.index(salesperson) #index method returns the value of the first occurence of salesperson in salespeople

        melons_sold[position] += melons #
    else:
        salespeople.append(salesperson) #otherwise adds salesperson to end of list salespeople
        melons_sold.append(melons) #otherwise adds melons sold to end of list melons


for i in range(len(salespeople)): #i declares the reproducibility of the legnth of sales people
    print(f'{salespeople[i]} sold {melons_sold[i]} melons') #prints from the list of salespeople to the amount of melons sold
