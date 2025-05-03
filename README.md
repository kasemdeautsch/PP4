# ML.Bookings!
Wellcome to my Bookings Wep App!
This site is an imagin website of how a booking system would looks like,  
it is a Full-stack, responsive WebApp and built for Education purpose.    
  
![](/static/images/main.png)
The website contains a homepage with wellcome message and options to make booking or view  
The current bookings, after the user login, create, edit and delete their entries.

## Overview

ML.Bookings is a full-stack mobile-first desin working on most modern web browswes\
Built using Bootstrab and Django Framework.

It allows the users to register an account and login and book their Dine with time and date\
desiged with role-based functionality edit permissions, to give them full CRUD functionality\
on their bookings.

[Link to the live website](https://my-restaurent-6ec23ea949ae.herokuapp.com/)

## The Agile Methodology
The project was made using methodology of a gile as a working software and Github Issues  
to write User stories [Here!](https://github.com/kasemdeautsch/PP4/issues).

All user stories contain Acceptance Criteria and tasks to match these criteria, and some
were concedard as Epic,\
As I didn't know in the beginning which task to begin, then the vision
became to be appear as it was just a user story.

Also I used the MoSCoW Prioritisations method in putting these user stories in the track
so that making the most important\
'Must Have', 'Should Have', 'Could Have', 'Wont Have'.

As the ones I didn't have the feature done in that iteration I classified them as "Won't Have"\
because the important is to have the Minimum Viable Product (MVP).  
Scrrenshots of Project Kanban Board, Epic and user stories:
![](/static/images/project.png)
![](/static/images/user-stories.png)

The Agile Methodology was great way to write my code and organise it according to the importance\
So that the most needed features will work first of all like registration and login,\
I didn't work with time iteration, but that way helped me using the isses and project Kanban\
and milestones as well, when moving the tasks from 'todo' to 'in progress' then 'Done'\
Lastly some user stories couldn't make it and moved to "wont have" in Backlog.

## User Stories (UX)
**Strategy / Site Goals**:  
The site goal is to present an online Booking system that is a vailable to use from any device\
and enables users and guests to register an account and login to watch their Bookings\
after providing their contact details (E-mail address in this case) and have the apportunity\
to have control on their own Bookkings.
<hr/>

**Scope / User Stories:**  
With The user stories in the project mentioned as written and what the site users\
will expect from the website which is translated to these user stories.\
The content and features will come to live in later sections.


The user types includes the traditional user who will use the site to only book.\
And the Site Owner / Admin role and the Developer user stories will have below.

As Admin/Site Owner:  
 - As an admin I can view a list of reservations so that I can manage them. [#5](https://github.com/kasemdeautsch/PP4/issues/5)  
 - As an Admin I can create, update, and delete reservations so that The users see their own\
 reservations with updates. [#3](https://github.com/kasemdeautsch/PP4/issues/3)  

 As a User:  
 - As a new user I can register in the page so that I can access the reservations model. [#1](https://github.com/kasemdeautsch/PP4/issues/1)  
 - As a registered user I can log in to my account so that edit my reservations. [#4](https://github.com/kasemdeautsch/PP4/issues/4)  
 - As a user I can make a reservation on a specific date and time so that I can order quickly. [#2](https://github.com/kasemdeautsch/PP4/issues/2)  
 - As a logged in user I can see all my reservations so that I can track them. [#7](https://github.com/kasemdeautsch/PP4/issues/7)  
 - As a user I can cancel a reservation so that I can replan it. [#6](https://github.com/kasemdeautsch/PP4/issues/6)  
 - As a user I can receive a cancellation confirmation after cancelling one reservation so that,  
 I can know it hase been cancelled successfully. [#8](https://github.com/kasemdeautsch/PP4/issues/8)
 - As a user I can make reservation using different devices(eg. desktop, tablet, mobile),  
   so that I book freely. [#9](https://github.com/kasemdeautsch/PP4/issues/9)  
 - As a user I can view all my current reservations so that I can update them. 
 [#12](https://github.com/kasemdeautsch/PP4/issues/12)  

 - As a user I can see errors when something wrong happens with booking,  
 (eg. trying to book a table which is alredy reserved) so that I understand what the problem is. 
  [#11](https://github.com/kasemdeautsch/PP4/issues/11)  
 - As a user I can see available tables so that I book a reservation with a specific table. 
 [#10](https://github.com/kasemdeautsch/PP4/issues/10) 

Later on some features added by Developer that was not included in the domain  
but added some functionality to the App and give users better experience.  

As a Developper:  
- As an Admin I can Add fav-icons on the website tab so that the appearance of the site looks good and draw the guest's attention.[#13](https://github.com/kasemdeautsch/PP4/issues/13).
<hr/>

**Structure / (Organization, user-flow):**  
The website uses a consistence layout and few colours with responsivness on most known breakpoints.\
Navigation will be on top of the site with links to registration, login and logout displayed as burger menu on mobile\
and expanded on larger screens.

Main page will be in a card wellcome message, with buttons to manage resrvations for authorised users\
or asking them login/register to use the site.

Make Booking page will present a nice form for the user to make a booking with the needed fields and
some buttons.\
Edit Booking page will show the asked booking to edit and update.

We need fields like name, date, time,... to make the booking.\
Delete Booking page will show a "Modal" to warn the user and confirm if he is agree.

The Registration and Authintication pages are simple and describe their function clearly.

The Footer is displayed sticky on buttom and contains the different links for social media contacts and displayed in a new tab.\
The Header and Footer are the same for all pages.\
All pages use the same color (light broun) for consistency.

To accomplish the features needed, we need the following attributes:
+ user
+ name
+ date
+ time
+ emeil (for confirmation).
+ notes for any...


Database table:  

![](/static/images/erd.png)
<hr/>

**Skeleton / Wireframes-Prototype:**\
An initial design of the layout done by drawing the layout on paper and then using the "Balsamiq" translated
to a "mockup", this helped in Brainstorming me to imagine how the key contents will be placed and how the user
will interact with them.

**<u>Balsamiq Wireframes:</u>**

**Home Page**

![](/static/images/wireframes/home-mobile.png)\
![](/static/images/wireframes/home-desktop.png)\

**Booking List Page**

![](/static/images/wireframes/bookings-mobile.png)\
![](/static/images/wireframes/bookings-desktop.png)\

**Edit Bookings Page**

![](/static/images/wireframes/edit-mobile.png)\
![](/static/images/wireframes/edit-desktop.png)\


**Make Bookings Page**

![](/static/images/wireframes/make-mobile.png)\
![](/static/images/wireframes/make-desktop.png)\

**Signin Page**

![](/static/images/wireframes/signin-mobile.png)\
![](/static/images/wireframes/signin-desktop.png)\

**Signup Page**

![](/static/images/wireframes/signup-mobile.png)\
![](/static/images/wireframes/signup-desktop.png)\

**Signout Page**

![](/static/images/wireframes/signout-mobile.png)\
![](/static/images/wireframes/signout-desktop.png)

The **Delete Booking** page will load a modal for confirmation.
<hr/>

**Surface / Design choices:**  
The visual look of the website is simple:  
+ Color Scheme:\
  I used the white and black colors for most text and backgrounds, the colors (red,green yellow, blue)\
  used for buttons from bootstrab classes:
  ![](/static/images/wireframes/color-schem.png)
  The Footer and Header have the same color which is "bg-body-tertiary" from Bootstrap.
+ Typography:
  Poppins and sans-serif fonts were used in this site.

  <hr/>



## Features

**Existing Features**

- Navigation Bar:  
  Featured at the top of the page for all pages, with
  links to the home page and other pages.
  The Navbar is full-responsive and contains:
  - Hamburger button on mobile expands to show links to login/out and home page
  - Brand name styled and connect to home page
  - Expanded Navbar on desktop shows links to the authentication and home pages
  - The current logged in user in the right corner or a "not logged in" in case the user not logged in.
  - Relative link to "Logout" if the user is logged in or "Login" and "Register" when not logged in.
  - The links make it easy for the user to navigate freely from page to page without need to go back to\
    the previous page.  
    ![](/static/images/features/mobile-header.png)

    ![](/static/images/features/mobile-header-full.png)

    ![](/static/images/features/desktop-header.png)

    ![](/static/images/features/desktop-header2.png)

- Footer:  
  The footer is full responsive and placed at the buttom and repeated on all pages to allow consistence look.    
    - It leads to external links for social media for contacting.
      ![](/static/images/features/desktop-header2.png)

- Landing page:  
  The landing page is a wellcome message that takes less than the full page size.
  - It changes according to the user state.
  - For logged-in users it displayes a button to show all bookings related to this user,  
    and another one to book for a meal.
  - When not loggedin user visit he will be asked to login to book for a meal.
  - Added new feature to enable user to sign in direct from within the wellcome message.

    ![](/static/images/features/landing.png)

    ![](/static/images/features/landing2.png)

- Register:  
  The site provides a full responsive page for users to register an account.
  - It can be accessed from the navigation bar or as a link in the sign in page.
  - The registration pege is a responsive form.
  - It uses Django-allauth and settings for authentication with the fields:
    - Username.
    - Email(optional).
    - Password.
    - Password(repeat).
  - There is a button to signup using bootstrap effects with a hover over.
  - After registration the user is redirected to the main page.

    ![](/static/images/features/desktop-register.png)

    ![](/static/images/features/mobile-register.png)

- Login:  
  The login page is full responsive and can be accessed from the navbar on top.
  - It is accessed also from the main page if the user not logged in or from sign up page.
  - It uses Django-allauth and settings for authentication with the fields:
    - Username.
    - Password.
  - There is a button to sign in using bootstrap effects with a hover over.
  - After signing in the user is redirected to the main page.
  - A message shows after a successfull login under the navbar.

    ![](/static/images/features/mobile-signin.png)

    ![](/static/images/features/desktop-signin.png)

    ![](/static/images/features/signin-message.png)

- Logout:  
  The website provides a functionality for the logged-in users to logout.
  - The logout page is resposive.
  - It warns the user before logging out.
  - It can be accessed from the navbar only.
  - It is available only for logged-in users.
  - There is a button to signout using bootstrap effects with a hover over.
  - A message shows after logout under the navbar.

  ![](/static/images/features/signout.png)

  ![](/static/images/features/signout-message.png)

The register, login and logout pages are consistent and have the same look and appearance.
- **CRUD Functionality**  
  The website gives the users a full functionality on their own bookings to:  
  Create, Read, Update and Delete.

- Make Booking:  
  The "make booking" page is a full responsive form and enables users to book for a meal.
  - It is available only when user in logged in.
  - All Fields will validate the entry and show a descriptive message below when exist.
  - The name field accepts only letters with no spaces.

    ![](/static/images/features/name-error.png)

  - The date field has validation that accepts bookings within one month only,  
    it doesn't take past days like yesterday.

    ![](/static/images/features/date-error.png)

  - The time field has choices with the allowed timings to avoid un wanted options.

    ![](/static/images/features/time-choices.png)

  - The email field will validate to a correct email format.

    ![](/static/images/features/email-error.png)

  - The notes field has a validation to take text not longer than 600 characters.

    ![](/static/images/features/notes-error.png)
  
  - A general message will display over the form  shows if thre are errors in the operation:

    ![](/static/images/features/all-error.png)

  - The user has tow options in this page, either save the current transaction or go back  
    to home page when he wants to cancel the operation for any reason.

    ![](/static/images/features/back.png)

  - If the whole operation is valid a message will show that it was successfull and the user  
    will be redirected to the bookings page.

    ![](/static/images/features/success.png)

  - List of bookings:  
    The users can see their own Bookings by clicking the "My Bookings" button on the main page
    - Only the bookings related to the user currently logged in will show.

      ![](/static/images/features/landing2.png)

- Edit Booking:  
  The users can edit their own bookings by clicking the "Edit Booking" button.
  - When clicked the Booking page with the form appears.
  - The system will show the transaction which is saved in the database with all fields.
  - The booking will show in a new page.
  - The user updates the required fields and when satisfied will click the "Update" button.
  - The user can cancel the operation by clicking the "Back" button.

    ![](/static/images/features/edit-booking.png)

- Delete Booking:  
  The site provide a delete functionality by clicking the "Delete booking" button.
  - When clicked a modal will appear to warn the user.
  - User can confirm that by clicking the "Delete" button again.
  - User can cancel that by clicking the "close" button or "X".
  - If deleted, the booking will be erased from the databeas.
  - The user is redirected to the bookings page.
  - A message of successfully deletion will show.

    ![](/static/images/features/delete-modal.png)

    ![](/static/images/features/success-delete.png)

- Admin Panel:  
  The website provides the owner a way to access the database tables using the Django admin panel.  
  The Django admin panel is granted to the Suberuser who has credentials to access the admin page.  
  A number of customization is done by customizing the "Admin" page.  

  - The admin panel accessed by appending /admin/ to the end of the url in the URL bar.
  - the Superuser used as "Username" with the "Password" granted.
  - The other users with "staff" status cann't access the admin page.
  - Only the Superuser can access thae admin panel.
  - The admin panel lists all apps installed for "Authenticatin and Authorization" and "Booking".
  - The users and groups under "Authenticatin and Authorization" can be edited and changed.  
    by the owner who has the Superuser credentials.
  - The reservations model shows under the "Booking" app.
  - Reservations can be filtered by date or name, or searched by name.
  - The Superuser has full CRUD functionality to edit, update and delete the transactions.  
  - The time in the admin panel also has the same choices on time field which is  
    in the form for consistency
    
    ![](/static/images/features/admin-login.png)

    ![](/static/images/features/reservations.png)

    ![](/static/images/features/admin-edit.png)


**Features Left to Implement**
- I intend to expand the website to have the opportunity to reserve a table along with the booking.  
- The time choices don't check the current time to disallow booking in the past.  
- Customer feedback like review is intended to be considered in the future.  
- Forget password also is not present in this version.


## Technologies used

**Languages**

- [HTML5](https://www.w3schools.com/html/)
- [CSS](https://www.w3schools.com/css/css_intro.asp)
- [Javacript](https://www.w3schools.com/Js/)
- [Python](https://www.python.org/downloads/release/python-3811/)


**Libraries-Frameworks**

- [Django 4.2.18](https://www.djangoproject.com/) : The open-source framework used for this project.
- [django-allauth 0.57.2](https://django-allauth.readthedocs.io/en/latest/) : Set of applications for
  authentication with ready templates.
- [django-crispy-forms 2.3](https://pypi.org/project/django-crispy-forms/) : This package styles the form
  without the need of using css. 
- [crispy-bootstrap5 0.7](https://www.w3schools.com/css/css_intro.asp) : Renders the form using the 
  Bootstap5 form controls and clases.  
- [gunicorn 20.1.0](https://gunicorn.org/) : Python Http server to run the project on Heroku.
- [django-summernote 0.8.20.0](https://summernote.org/) : A robust text editor allowing rich text 
  with various formats  
  like headings and paragraphs.

- [postgreSQL](https://www.postgresql.org/) : Open source object-relational database.
- [psycopg2-binary 2.9.10](https://www.psycopg.org/docs/) : A database adapter to use 
  PostgreSQL commands from Python.
- [sqlparse 0.5.3](https://pypi.org/project/sqlparse/) : A library used to parse SQL queries
  in Python.
- [dj-database-url 0.5.0](https://pypi.org/project/dj-database-url/) : Utility to connect Django 
  to a database using a URL.

- [Heroku](https://www.heroku.com/) : Cloud service for hosting projects.
- [Bootstrap 5.3.3](https://getbootstrap.com/) : A framework used to build responsive websites.
- [whitenoise 5.3.0](https://whitenoise.readthedocs.io/en/latest/) : allow Heroku app to serve its
   own static files  
   without relying on any external file hosting services.  

The all list for required packages found in the ***requirements.txt*** file



## Testing
  - I tested the website and it works on different web browsers like Chrome, Firefox and Edge.
  - The web site is responsive and looks good on standard screen sizes using devtools device toolbar.
  - The header and navigation and text on all pages is readable and easy to understand.
  - I tested the Form and confirmed that it works and required fields fuction, the form will not
      accept to register without entering a valid Email address, the Register field works as well
      and when clicking on it the information sent to the corresponding web site and shows the details
      collected from user.
  - All links and the Form submission opens in a new tab.
  - All Images have the **alt** attribute for the purpose of impared visual users.
  - All links have the **Aria-label** attribute.
  - I included **mete tags** with **keywords** and **description** attribute to enable more
    SEO improvement.

**Bugs**
  - no bugs found.
  - I had a difficulty to make the background image of all pages extent along to cover
    the main element in it's section, also making the map in the home page responsive
    and solved by the assist of **Code Institute Tutor** and **Mentor** as well.

**Validator Testing**
  - HTML
    - I tested all pages and no errors were returned when passing through the official W3C validator
    ![](/media/index-page-validator.png)
    ![](/media/gallery-page-validator.png)
    ![](/media/history-page-validator.png)
    ![](/media/form-page-validator.png)
  - CSS 
    <p>
       <a href="http://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="http://jigsaw.w3.org/css-validator/images/vcss"
            alt="Valid CSS!" />
       </a>
    </p>
    
    - No errors were found when passing through the official (Jigsaw) validator
      ![](/media/css-code-%20validator.png)
  - Accesibility
    - Colors and fonts are accesible and readable using lighthouse in devtools.
      ![](/media/accessibility.png)
## Deployment

  - The site was deployed to GitHub pages. The steps to deploy are as follows:
    - In the GitHub repository, navigate to the Settings tab
    - From the source section drop-down menu, select the Master Branch
    - Once the master branch has been selected, the page provides the link to the deployed project.
    - The live link can be found [here](https://kasemdeautsch.github.io/Portfolio-1/).
## Credits
- Content
  - The text for the Home page was taken from Wikipedia Article A
  - Instructions on how to implement form validation on the Sign Up page was taken from Specific YouTube - Tutorial
  - The icons in the footer were taken from Font Awesome
  - The code for social media links was taken from **Love running Project**.
  - The Form dedign was taken from **Love running Project**.
  - The following websites ware used for problem solving.
    - **https://www.diffchecker.com/**.
    - **https://stackoverflow.com/**.
    - **https://www.w3schools.com/**.
    - **https://www.perplexity.ai/**.
    - **https://www.pexels.com/**.
    - **https://tinypng.com/**.

- Media
  - The photos in Gallery page from open source(Google search).
  - the background image of the home page is also.