# Testing for the Animal Hostel Project

## User Story 

### Make an offer             
- As a <b>Site User</b> I can <b>make an offer to a guest </b>so that<b> I can give them a home</b>

### Plan
- I will create a new page that displays an empty form for entering the offer details.
- The animals will be pre-loaded in a drop down available to be selected. There will also be a pre-loaded dropdown provided for basis.
- There will be a text area provided for entering the pitch.
- There will be an optional field to enter the number of weeks for fostering. The other fields will be mandatory.
- There will be a submit button and on clicking this button the offer details will be written to the database and the user returned to the �My Offers� page.

### Implementation
- I added new tests to test_views.py to test the Add Offer View, the template it is using and whether an offer could be added using it.
- I added a new view to views.py called OfferAdd.
- I added a new url pattern for the new page.
- I added a new template in templates/pages for offer_add.html
- I used the Django crispy forms app to display the form so I also added that to my settings.py and into my requirements.txt file  

### Testing
- I ran the new form through the HTML Validator.
- I ran it through the CSS Validator.

I ran the automatic tests I had added to Views.test

I also performed the following manual end-to-end tests:-
* I confirmed that the heading and footer appeared correctly on the Make an Offer page.
* I confirmed that the drop down list for Animal contained the list of animals in the database.
* 
Results

- All tests passed successfully

Verdict

- User story is complete
