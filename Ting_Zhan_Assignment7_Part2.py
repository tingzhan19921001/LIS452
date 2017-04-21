# A sample program to open and read historical stock price files
# downloaded from Yahoo! Finance and compute statistics.
# These are in VERY SIMPLE CSV file format.


# the file name we want to open:
from graphics import *

def main():

    input_file_name = 'YHOO-1-year.csv'

# Define the expected data columns in file order:
    columns = ['Date','Open','High','Low','Close','Volume','Adj Close']

# Now open the file in read text mode:
    file = open(input_file_name, 'r')

# The file opened. Read the first line which should be the CSV column names:
    header_line = file.readline().strip()   # The strip gets rid of extra whitespace characters
    
    header_values = header_line.split(',')  # Split it at the commas
    
    if header_values != columns:
        print("The format of the input file doesn't match what we expected. It contained:\n",
              header_line, "\nQuitting.")
        exit()

# define empty list we'll be building:
    dates = []
    adjusted_close = []
    high_price = []
    low_price = []


# The rest of the file should be data rows. Let's loop through it to the end:
    for line in file:
    # Check for possible blank line:
        if len(line.strip()) < 1:
            continue  # skip it so we don't cause an error trying to parse it

    # Split the line at commas and assign to sensible variable names.
        (date_text, open_price, high, low, close, volume, adj_close) = line.split(',')
    
    # Remember the date_text value by adding it to a list:
        dates.append(date_text)
        dates.reverse()
        
        adjusted_close.append(float(adj_close))
        adjusted_close.reverse()
        
        high_price.append(float(high))
        high_price.reverse()
        low_price.append(float(low))
        low_price.reverse()

    file.close()# close the input file

    
    win = GraphWin('part2',800,800)#set up the canvas where we could print
    win.setBackground('white') #make the background white
    win.setCoords(-5,150,26,190) #set up coordinates
    Line(Point(0,160),Point(25,160)).draw(win) #draw horizontal line
    Line(Point(0,160),Point(0,190)).draw(win) #draw vertical line

    for i in range(len(dates)-1):
            line1 = Line(Point(i,adjusted_close[i]),Point(i+1,adjusted_close[i+1])) #line up the points
            line1.setFill('black') #fill with black color
            line1.draw(win) #draw the line
            line2 = Line(Point(i,high_price[i]),Point(i+1,high_price[i+1]))
            line2.setFill('red') #fill color with red
            line2.draw(win) #draw the line
            line3 = Line(Point(i,low_price[i]),Point(i+1,low_price[i+1]))
            line3.setFill('blue') #fill color with blue
            line3.draw(win)


    Text(Point(0,159), min(dates)).draw(win) #label the date at the position
    Text(Point(len(dates),159), max(dates)).draw(win)
    Text(Point(-1,max(adjusted_close+high_price+low_price)),round(max(adjusted_close+high_price+low_price),2)).draw(win)
    # find the largest day(the latest day), then round it to 2 decimals
    Text(Point(-1,min(adjusted_close+high_price+low_price)),round(min(adjusted_close+high_price+low_price),2)).draw(win)
    #Text(Point(len(dates)+5, 159),'Date Range').draw(win)
    #Text(Point(0,185),'Price').draw(win)
main()        





