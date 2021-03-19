## Stack data structure -- LIFO : last in - first out
## start with empty stack [] to navigate the browsers
[1, 2, 3]  #3 browers

browsing_session = []
##user navigates to sessions 1, 2, 3 -- add to list with append
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)

## if user presses the back button, it should remove the last item in the list
## use pop() to remove the last item from the list
#browsing_session.pop()
## set it to a variable to check the last item
last = browsing_session.pop()
print(last)
 
print(browsing_session)

 ## return the last item from the stack; add a label for clarity to redirect user to the last browser
print("redirect", browsing_session[-1])

## check to see if stack is empty or not; if it is empty, disable the back button
## empty arrays, lists, [] are falsy -- add "not" makes them true
if not browsing_session:  # if browsing session is empty = true
    print("disable")

## review order
browsing_session = []
browsing_session.append()  #add an item to the top of the stack
browsing_session.pop()     #remove an item on top of the stack 
if not browsing_session:  #check to see if stack is empty or not to make sure we don't get an error; if browsing session is not empty then get the item at the top of the stack
    browsing_session[-1]   #to get the item on the top of the stack

