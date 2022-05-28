# Testing for the Animal Hostel Project

## User Story 

### As a site owner 
* I want the home page to display a rotating image of each animal so users will find the site interesting.  

#### Plan
- I will include a bootstrap carousel of the images loaded for each animal added to the database.

#### Implementation
- I created a branch for the user story - USER STORY: Rotating image display #1 Pull Request #25
- I added a template to the components folder for the carousel.
- I used the list of animal objects passed into the index.html template from the GuestList view to loop through
  each animal and display its image.
- If an animal had no image then the placeholder image is displayed instead.

#### Testing
- I displayed the page and confirmed that the images of the animals were displaying.
- I confirmed that the images were being displayed in order each one displaying for a short time .
- I confirmed that clisking on the arrows on the right and left caused the next image to be shown.
- I confirmed that the carousel indicators correctly indicated which image was showing.

#### Results
- All tests passed successfully

#### Verdict
- User story is complete

*****************************************************************************************************************

### As a site owner 
* I want the home page to explain its purpose so users will immediately get it.

#### Plan
- I will include a site description on the home page under the carousel.

#### Implementation
- I created a branch for the user story - USER STORY: Site description #2 Pull Request #28
- I added a template to the components folder for the site description.
- I added a text area explaning the sites purpose.
- I added a heading welcoming users to the site

#### Testing
- I displayed the page and confirmed that the site description was displayed.
- I confirmed that the heading and description displayed in an attractive and easy to read manner.
- I checked that the spelling was correct.

#### Results
- All tests passed successfully

#### Verdict
- User story is complete

*****************************************************************************************************************

### As a site user 
* I can view a list of animals so that I can select one to take home.

#### Plan
- On th home page I will display a bootstap card for each animal.
- Each card will display an image of the animal, the name and type of the animal and a slogan.
- The list will be maintained using django admin functionality 

#### Implementation
- I created a branch for the user story - USER STORY: View guest list #3 Pull Request #21
- I added the base template containing the Name, nav bar and footer
- I added the index template displaying an image and details for each animal/guest.
- I added a style sheet
- I added a view to display the index page passing in the list of animals
- I added a test_views file containing tests for the view guest list functionality
- I added two url.py files. One for the project and one for the app

#### Testing
- I ran the tests in the test_view file to confirm they passed.
- I confirmed that the heading was displayed in an attractive and easy to read manner.
- I confirmed that a card was displayed on the home page for each animal on the list.
- I confirmed that the name and type of each animal was displayed and correctly styled.
- I confirmed that the slogan for the animal was displayed correctly.
- I confirmed that four animals appeared in a row on a desktop screen and just one on a phone.
- I confirmed that the name and type were styled correctly in an orange container.

#### Results
- All tests passed successfully

#### Verdict
- User story is complete

*****************************************************************************************************************
### As a site user
* I can click on a guest so that I can read the full details about them.

#### Plan
- On the home page I will wrap each animal in a link which when clicked displays the guest_detail page.
- The guest detail page will display a large heading area half showing the animal name and slogan and the other
  showing the image of the animal.
- Underneath the heading the animal description will be displayed.
- Under that there will be a link to take the user to their offers page or to register if they are not signed in. 
- The list will be maintained using django admin functionality 

#### Implementation
- I created a branch for the user story - USER STORY: See detailed view of animal #5 Pull Request #23, #24, #26
- I added a new template for the detail view
- I added an url for detail view
- I added a view for detail view
- I added a test for detail view
- I added styling for detail view

#### Testing
- I ran the tests in the test_view file to confirm they passed.
- I confirmed that the heading was displayed as expected.
- I confirmed that the animal description was displayed as expected.
- I confirmed that there was a link under the animal description to the offers page if I was logged in and the register page otherwise.
- I confirmed that the slogan for the animal was displayed correctly.

#### Results
- All tests passed successfully

#### Verdict
- User story is complete

*****************************************************************************************************************
### As a site user
* I can register an account so that I can make offers on animals.

#### Plan
- On the navigation bar there will be a link to register an account.
- The link will take the user to the standard django register account functionality.
- This functionality will allow the user to register for an account. 

#### Implementation
- I created a branch for the user story - USER STORY: USER STORY: Account registration #6 Pull Request ##22
- I added django allauth functionality in requirements.py file
- I added changes to settings.py for implementing allauth
- I added allauth urls in url.py
- I added styling changes in style.css
- I added all the account templates provided by allauth
- I added links changes on index and base templates to authentication pages

#### Testing
- I ran the app to see did the register link appear if I was not signed in.
- I created an account successfully and was able to login.
- I confirmed that I was able to logout successfully.
- I confirmed that the links to my offers appeared when signed in and changed to the register page when not.

#### Results
- All tests passed successfully

#### Verdict
- I notice that when a user registers using an email that two flash messages are sent but only one disappears and the other mains
until the user closes it. This should be investigated.

*****************************************************************************************************************

### As a site user
* I can make an offer to a guest so that I can give them a home

### Plan
- I will create a new page that displays an empty form for entering the offer details.
- The animals will be pre-loaded in a drop down available to be selected. There will also be a pre-loaded dropdown provided for basis.
- There will be a text area provided for entering the pitch.
- There will be an optional field to enter the number of weeks for fostering. The other fields will be mandatory.
- There will be a submit button and on clicking this button the offer details will be written to the database and the user returned to the My Offers page.

### Implementation
- I created a branch for the user story - USER STORY: USER STORY: USER STORY: Make an offer #7 Pull Request ##29
- I added new tests to test_views.py to test the Add Offer View, the template it is using and whether an offer could be added using it.
- I added a new view to views.py called OfferAdd.
- I added a new url pattern for the new page.
- I added a new template in templates/pages for offer_add.html
- I used the Django crispy forms app to display the form so I also added that to my settings.py and into my requirements.txt file  

### Testing
- I ran the app, went to my offers page and confirmed that when I clicked the 'Make an Offer' button it displayed the add offer page.
- I confirmed that there was a pre-populated drop down of animals names I could choose from.
- I confirmed that

I ran the automatic tests I had added to Views.test

I also performed the following manual end-to-end tests:-
* I confirmed that the heading and footer appeared correctly on the Make an Offer page.
* I confirmed that the drop down list for Animal contained the list of animals in the database.
* I confirmed that I could enter my pitch for why I would make a great owner for this animal.
* I confirmed that I could select an option for Adoption or Fostering and that I had to enter one.
* I confirmed that I could enter a number of weeks for fostering but not a negative number.
* I confirmed that when I clicked the Submit button that my offer appeared on the offers page with a flash message telling
  me my offer had been added successfully.
* I confirmed that if I tried to add a second offer for the same animal I was not allowed and got a flash message saying an offer
  already existed.

Results

- All tests passed successfully

Verdict

- I notice that it is also possible to add a number of weeks for adoption which shouldn't really be allowed.

*****************************************************************************************************************

### As a site user
* I can see my offers so that I can see the status of each one.

#### Plan
- On the navigation bar there will be a link to my offers page.
- The link will take the user to the offers page and display only the offers for the signed in user.
- This page will display the guest name, basis (Adoption or Fostering), Status (Pending, Approved, Rjected ) and an icon for delete.
- The animal name will be a link to the Edit Offer page.
- The delete icon will move to the next line on small screens.

#### Implementation
- I created a branch for the user story - USER STORY: View my offers #8 Pull Request ##27
- I added an Entity Relationship Diagram to the README.MD
- I added a new model - Offer
- I registered Offer with django Admin
- I created and ran the Migrations
- I added an automated test for the model
- I add a new OfferLIst view
- I added new tests for OfferList view
- I added a new url pattern to urls.py
- I added new templates for OfferView
- I added new styling declarations in style.css
- I added new components and layout folders containing elements of main pages

#### Testing
- I clicked the offers menu option to confirm that the offers page appeared.
- I confirmed that only my offers appeared.
- I confirmed that if I added, edited or deleted an offer that this was reflected on the offers page and a message appeared briefly.
- I confirmed that the links to my offers page all worked correctly.

#### Results
- All tests passed successfully

#### Verdict
- User story completed.

*****************************************************************************************************************

### As a site user
* I can edit my offers so that I can change the details.

#### Plan
- I will create a new page that displays an offer so it can be amended.
- The animal name should be displayed as a heading and should not be amendable.
- I should be able to amend the details displayed.
- A drop down option box should appear for Adoption or Fostering.
- The number of weeks should not be allowed to be negative.
- There will be a save button and on clicking this button the offer details will be written to the database and the user returned to the My Offers page.

#### Implementation
- I created a branch for the user story - USER STORY: Edit my offers #9 Pull Request ##32
- I added a new view for editing an offer
- I added a new url pattern for edit function
- I added new tests for edit offer function
- I added a new template for edit offer

#### Testing
- I clicked the name of the animal in one of my offers and it took me to the edit offer page.
- I confirmed that the correct details appeared on the screen and that the animal name was not amendable.
- I confirmed that I was able to change all the other details except user which did not appear as I could only select my own.
- I confirmed that when I clicked the save button my changes were saved and I was returned to the offers page and received 
  a flash success message.

#### Results
- All tests passed successfully

#### Verdict
- User story completed.

*****************************************************************************************************************

### As a site user
* I can delete my offers so that I can rescind my offer.

#### Plan
- I will create a new page that displays an offer so it can be deleted.
- The animal details should be displayed as disabled and should not be amendable.
- There will be a delete button and on clicking this button the offer will be deleted from the database and the user returned to the My Offers page.

#### Implementation
- I created a branch for the user story - USER STORY: Delete my offers #10 Pull Request #33
- I added new automatic tests for delete offer function
- I added a new view for delete offer function
- I added a new url pattern
- I added  new template

#### Testing
- I clicked the delete icon of the animal in one of my offers and it took me to the delete offer page.
- I confirmed that the correct details appeared on the screen and that they were not amendable.
- I confirmed that when I clicked the delete button my offer was deleted and I was returned to the offers page and received 
  a flash success message.

#### Results
- All tests passed successfully

#### Verdict
- User story completed.

*****************************************************************************************************************

### As a site administrator
* I can add, view, update and delete animals so that I can maintain the list.

#### Plan
- I will register the animal model to the django administration so it can be maintained by the administrator.
- The animals should appear and can be added, amended or deleted from this screen.
- An image of the animal should be able to be loaded.

#### Implementation
- I created a branch for the user story - USER STORY: Manage guest list #11 Pull Request ##17
- I added the animal model to models.py
- I added a test for the creation of an animal in test_models.py
- I registered the animal model on the admin.py
- I added the migration for the animal model

#### Testing
- I signed on as administrator and went to the admin page.
- I confirmed that the animal model appeared on the screen.
- I confirmed that when I clicked the animal model I was able to add an animal and edit and delete them. 

#### Results
- All tests passed successfully

#### Verdict
- User story completed.

*****************************************************************************************************************
### As a site administrator
* I can add, view, update and delete animal types so that I can maintain them.

#### Plan
- I will register the animal types model to the django administration so it can be maintained by the administrator.
- The animal types should appear and can be added, amended or deleted from this screen.

#### Implementation
- I created a branch for the user story - USER STORY: Manage animal type list #12 Pull Request #14
- I added the animal type model to models.py
- I added a test for the creation of an animal type in test_models.py
- I registered the animal type model on the admin.py
- I added the migration for the animal type model

#### Testing
- I signed on as administrator and went to the admin page.
- I confirmed that the animal model appeared on the screen.
- I confirmed that when I clicked the animal model I was able to add an animal and edit and delete them. 

#### Results
- All tests passed successfully

#### Verdict
- User story completed.

*****************************************************************************************************************

### As a site administrator
* I can approve or reject offers so that I can find the right home for each guest.

#### Plan
- I will register the offers model to the django administration so it can be maintained by the administrator.
- The offers should appear and can be added, amended or deleted from this screen.
- The offer has a status field which can be set to Pending, Approved or Rejected

#### Implementation
- This user story was implemented as part of another user story- USER STORY: View my offers #8 Pull Request #27
- The offer model was registered with django Admin

#### Testing
- I signed on as administrator and went to the admin page.
- I confirmed that the offer model appeared on the screen.
- I confirmed that when I clicked the offer model I was able to see all the offers and the status field. 

#### Results
- All tests passed successfully

#### Verdict
- User story completed.

****************************************************************************************************************
### As a site user 

* I can filter the list of animals so that I can see only the relevant ones.


#### Verdict
- This User story did not get implemented and is still outstanding.



