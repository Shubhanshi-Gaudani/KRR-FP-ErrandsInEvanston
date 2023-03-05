import tkinter as tk
window = tk.Tk()

#making all the GUI components
title = tk.Label(text="🎼 Evanston Task Planner 🚗", width=20, height=3, font=("Arial", 20))
title.pack()

#description of functionality
desc = tk.Label(text="This program helps you minimize distance as you perform your tasks and go around Evanston.", width=100, height=2, font=("Arial", 10))
desc.pack()

#amenity classes
classes = tk.Label(text="Here are the kinds of places you can go to: ['school', 'place_of_worship', 'library', 'fuel', 'restaurant', 'pharmacy', 'fast_food', 'cinema', 'pub', 'cafe', 'car_rental', 'bank', 'dentist', 'spa', 'bar', 'post_office', 'parking', 'atm', 'brewery', 'animal_shelter', 'doctors', 'clinic', 'money_transfer', 'theatre', 'music_school', 'police', 'ice_cream', 'kindergarten', 'dance_theater', 'salon', 'social_facility', 'veterinary', 'parking_entrance', 'nursing_home', 'bicycle_rental', 'charging_station', 'arts_centre']", width=100, wraplength=700, height=5, font=("Arial", 10))
classes.pack()

#entering categories
category_entry_label = tk.Label(text="Please enter up to five types of places you would like to go to from the list above, separated by semicolons.", height = 2, font=("Helvetica", 10))
categories = tk.Entry(width=100)
category_entry_label.pack()
categories.pack()
#entering address
location_entry_label = tk.Label(text="What is your current location? A sample answer would be: '1228 Davis St.'", font=("Helvetica", 10), height=2)
location = tk.Entry(width=100)
location_entry_label.pack()
location.pack()
#submit button
submit_button = tk.Button(text="Plan my day!",width=25)
submit_button.pack()
#results
result_label = tk.Label(text="Results:", font=("Helvetica", 10), height=2)
result = tk.Text(width=100)
result_label.pack()
result.pack()

#entry.get() pulls from input box, entry.insert() pushes text to it
#event
def handle_click(event):
    print('worked')
    location_input = location.get()
    categories_input = categories.get() 
    try:
        #call whatever function does the calculation from the KB!!!
        #need to parse category input into a list of categories. we've asked for input to be separated by semicolons.
        categories_input = categories_input.split(';')
        print(categories_input)
        output = 'trying to insert\na new line' #this will be the output of the function
        result.insert('1.0',output)
    except:
        result.insert('1.0','There seems to be an error in your input. Please check that the formatting is appropriate.')

submit_button.bind("<Button-1>", handle_click)

window.mainloop()