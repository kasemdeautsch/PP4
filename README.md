# ML.Bookings!
Wellcome to my Bookings Wep App!
This site is an imagin website of how a booking system would looks like,  
it is a Full-stack, responsive WebApp and built for Education purpose.    
  
![](/static/images/main.png)
The website contains a homepage with wellcome message and options to make booking or view  
The current bookings, after the user login, create, edit and delete their entries.

<h1 id="table">Table of contents</h1>

- [Overview](#over)
- [The Agile Methodology](#agile)
- [User Stories (UX)](#user)
- [Features](#Features)
- [Technologies Used](#Techno)
- [Testing](#testing)
- [Bugs](#bugs)
- [Deploying](#deploy)
- [Forking the repository](#fork)
- [Cloning the repository](#clone)
- [Credits](#credits)

<h2 id="over">Overview</h2>

ML.Bookings is a full-stack mobile-first desin working on most modern web browswes  
Built using Bootstrab and Django Framework.

It allows the users to register an account and login and book their Dine with time and date  
desiged with role-based functionality edit permissions, to give them full CRUD functionality  
on their bookings, 

The name in Heroku has the word'restaurent' instead 'restaurant' and it was a mistake, I didn't  
change it and was confused that it will break something in GitHub.
[Link to the live website](https://my-restaurent-6ec23ea949ae.herokuapp.com/)

<u>[Back To Top](#table)</u>

<h2 id="agile">The Agile Methodology</h2>

The project was made using methodology of a gile as a working software and Github Issues  
to write User stories [Here!](https://github.com/kasemdeautsch/PP4/issues).

All user stories contain Acceptance Criteria and tasks to match these criteria, and some
were considered as Epic,\
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

The Agile Methodology was great way to write my code and organise it according to the importance,\
so that the most needed features will work first of all like registration and login,\
I didn't work with time iteration, but that way helped me using the isses and project Kanban\
and milestones as well, when moving the tasks from 'todo' to 'in progress' then 'Done'\
Lastly some user stories couldn't make it and moved to "wont have" in Backlog.

<u>[Back To Top](#table)</u>
<h2 id="user">User Stories (UX) Five Planes</h2>

**1. Strategy / Site Goals:**  
The site goal is to present an online Booking system that is a vailable to use from any device\
and enables users and guests to register an account and login to watch their Bookings\
after providing their contact details (E-mail address in this case) and have the apportunity\
to have control on their own Bookkings.
<hr/>

**2. Scope / User Stories:**  
A Brainstorm comes to mind and think of what possible features the  site users\
will expect from the website which is translated to 'user stories'.\
The content and features will come to live now.

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

**3. Structure / (Organization, user-flow):**  
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

**4. Skeleton / Wireframes-Prototype:**  
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

![](/static/images/wireframes/signout-mobile.png)  
![](/static/images/wireframes/signout-desktop.png)  

The **Delete Booking** page will load a modal for confirmation.
<hr/>

**5. Surface / Design choices:**  
The visual look of the website is simple:  
+ Color Scheme:  
  I used the white and black colors for most text and backgrounds, the colors (red,green yellow, blue)\
  used for buttons from bootstrab classes:
  ![](/static/images/wireframes/color-schem.png)
  The Footer and Header have the same color which is "bg-body-tertiary" from Bootstrap.
+ Typography:
  Poppins and sans-serif fonts were used in this site.  
<u>[Back To Top](#table)</u>
<hr/>

<h2 id="Features">Features</h2>

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
<hr/>

- Footer:  
  The footer is full responsive and placed at the buttom and repeated on all pages to allow consistence look.    
    - It leads to external links for social media for contacting.
      ![](/static/images/features/footer.png)
<hr/>

- Landing page:  
  The landing page is a wellcome message that takes less than the full page size.
  - It changes according to the user state.
  - For logged-in users it displayes a button to show all bookings related to this user,  
    and another one to book for a meal.
  - When not loggedin user visit he will be asked to login to book for a meal.
  - Added new feature to enable user to sign in direct from within the wellcome message.

    ![](/static/images/features/landing.png)

    ![](/static/images/features/landing2.png)
<hr/>

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
<hr/>

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
<hr/>

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
<hr/>

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

  - The time field has choices with the allowed timings to avoid unwanted options.

    ![](/static/images/features/time-choices.png)

  - The email field will validate to a correct email format.

    ![](/static/images/features/email-error.png)

  - The notes field has a validation to take text not longer than 600 characters.

    ![](/static/images/features/notes-error.png)
  
  - A general message will display over the form  shows if there are errors in the operation:

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

  - Added new feature to avoid duplication in the booking by ensuring the uniqeness of the fields:  
    'name', 'date', 'time',

    ![](/static/images/features/duplicate.png)

<hr/>

- Edit Booking:  
  The users can edit their own bookings by clicking the "Edit Booking" button.
  - When clicked the Booking page with the form appears.
  - The system will show the transaction which is saved in the database with all fields.
  - The booking will show in a new page.
  - The user updates the required fields and when satisfied will click the "Update" button.
  - The user can cancel the operation by clicking the "Back" button.

    ![](/static/images/features/edit-booking.png)
<hr/>

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
<hr/>

- Admin Panel:  
  The website provides the owner a way to access the database tables using the Django admin panel.  
  The Django admin panel is granted to the Suberuser who has credentials to access the admin page.  
  A number of customization is done by customizing the "Admin" page.  

  - The admin panel accessed by appending /admin/ to the end of the url in the URL bar.
  - the Superuser uses his "Username" with the "Password" granted.
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

- Messages framework:  
  Added new functionality for messages using the tags setting to apply Bootstrap appropriate class  
  to messages according to the message tag (success/error).

  ![](/static/images/features/success-message.png)

  ![](/static/images/features/error-message.png)
<hr/>

**Features Left to Implement**
- I intend to expand the website to have the opportunity to reserve a table along with the booking.  
- The time choices don't check the current time to disallow booking in the past.  
- Customer feedback like review is intended to be considered in the future.  
- Forget password also is not present in this version.

<u>[Back To Top](#table)</u>
<hr/>

<h2 id="Techno">Technologies used</h2>

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

**Tools used**

- [W3C Validator](https://validator.w3.org/) Html code validator.
- [W3C Css Validator](https://jigsaw.w3.org/css-validator/) Css code validator.
- [Python Linter](https://pep8ci.herokuapp.com/) Code Institute Python Linter.
- [GitHub](https://github.com/) Cloud based for hosting repository.

- [Am I responsive](https://ui.dev/amiresponsive) Tool to check site responsiveness.

- [TinyPng](https://tinypng.com/) image compressor to reduce size.

- [Coolors](https://coolors.co/2f6690-3a7ca5-d9dcd6-16425b-81c3d7) Color palette generator.

- [Google fonts](https://fonts.google.com/) Using fonts from google.

- [Font Awesom](https://fontawesome.com/) Icons.

- [Balsamiq](https://balsamiq.com/product/) Wireframes.
- [JsHint](https://jshint.com/) Javascript code debugger.
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/) Color ontrast checker.

<u>[Back To Top](#table)</u>
<hr/>

<h2 id="testing">Testing</h2>

  All testing can be found in [TESTING.md](/TESTING.md).

  <u>[Back To Top](#table)</u>
  <hr/>

<h2 id="bugs">Bugs</h2>
  Fixed Bugs:  

  - The name field was accepting any name without constraints, and was fixed by applying a validator  
    to accept only alphabets that raises an error when the user enters a name that contains numbers or spaces:

    ```Python
    def validate_name(value):
      if not value.isalpha():
        raise ValidationError(
            _('%(value)s is not allowed!, name can contain only letters and no spaces.'),
            params={'value': value},
            )
    ```

  - The time field in the admin caused some conflicts as it has no choices like the one applied to the
    field in forms,  
    and the admin has the ability to choose some time that is not defined in the list,
    The solutions was to apply the same concept and customize the admin panel
    we also used a function (strptime) to parse the entry to a time object.

    ```Python
    class ReservationAdminForm(forms.ModelForm):
        time = forms.ChoiceField(choices=Reservation.time.field.choices, widget=forms.Select)
        class Meta:
            model = Reservation
            fields = '__all__'
        def clean_time(self):
            timestr = self.cleaned_data['time']
            tt = datetime.datetime.strptime(timestr, "%H:%M:%S").time()
            for time_obj, display in Reservation.time.field.choices:
                if time_obj == tt:
                    return time_obj
            raise forms.ValidationError(f"Invalid time choice: {tt}")
    ```
  
  - The notes field was taking infinite characters, to solve this we add a ready validator to allow only
    fixed character length:  
    
    ```Python
    notes = models.TextField(blank=True, null=True, validators=[MaxLengthValidator(600)])
    ```
    <hr/>

  Unfixed Bugs:

  - The time in the form accepts a past time and it was not handeled, it is better to the user 
    not to choose the current time, as this issue will be handelled in the future.
  - Also date in admin is not validated as the admin can choose past date, the solution for now not to choose
    previous dates as this will be handled in future iteration.

<u>[Back To Top](#table)</u>
<hr/>

<h2 id="deploy">Deploying</h2>

After Django project was created and database tables as well, we migrated these tables to the databese, as the **db.sqlite3** database that comes with django only working for developement enviroment and not suitable for production server like "Heroku",
Heroku offers a "sqlite" database with some charge, for our project we used an instance of PostgreSQL 
which is a cloude based Database hosted on [CI Database](https://dbs.ci-dbs.net/).
provided by Code Intitute for free.

**Steps for deploying:**

**Create Heroku App**  
  1. Login to heroku and create new app.
  2. Give the app a unique name and select the a region closeset to you.
  3. Click on 'Create new app'.

**Create a PostgreSQL Datebase**  

  1. Login to [https://dbs.ci-dbs.net/.](https://dbs.ci-dbs.net/.)
  2. Enter email address in the input field
  3. Click submit.
  4. Receive the database link in the email.  

**Create the env.py file**  

  After the databese is created we need to connect it to the project.
  In order to keep the database hidden we need to create an enviroment variable in the 'env.py' file
  and add this file to '.gitignore' so it is not pushed to Github.  
  1. Use the next code to set value of the DATABASE_URL constant to the URL in the email you received
     from PostgreSQL.
  

   ```python
    import os
    os.environ.setdefault(
    "DATABASE_URL", "copiedURL")
   ```
  2. In the 'env.py' also create a SECRET_KEY using any string you like or use any 
  [Secret key generator](https://secretkeygen.vercel.app/).  
  As Django needs a SECRET_KEY to encrypt session cookies:

  ```python
    import os
    os.environ.setdefault("SECRET_KEY", "value_created")
   ```
**Modify settings.py**  

  1. Use the following code to connect the 'settings.py' file to 'env.py' file and import it only when it 
  exists:
  ```python
    import os
    import dj_database_url
    if os.path.isfile('env.py'):
        import env
   ```
  2. Reference the SECRET_KEY in 'settings.py' to the one generated lately and remove the old value:  

  ```python
      SECRET_KEY = os.environ.get("SECRET_KEY")
  ```  
  3. The 'DATABASES' variable in 'settings.py' connects the django applications to a default db.sqlite3
     datebase which is already created and not suitable for a production enviroment.  
     Using the dj_database_url import done before, connect this variable to the one in 'env.py':

  ```python
    # Database
    # https://docs.djangoproject.com/en/4.2/ref/settings/#databases

    # DATABASES = {
    #    'default': {
    #        'ENGINE': 'django.db.backends.sqlite3',
    #        'NAME': BASE_DIR / 'db.sqlite3',
    #    }
    # }

    DATABASES = {
        'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
    }
   ```  
  don't forget to add the default'db.sqlite3' database to '.gitignore' file if used before.  

  4. save all the files and migrate the database to the ''PostgreSQL' database by running  
    The '**python3 manage.py migrate**' command from terminal.

**Connect the database to Heroku**

  1. From heroku dashboard select the project app and click on 'Settings'.
  2. Click on 'Reveal config vars' and add the 'DATABASE_URL' with the value of the coppied
    URL from the database instance created  on CI database.
  3. Add the variable 'SECRET_KEY' and it's value from 'env.py' or a value from your choice.

**Setup Templates dir**

  In 'settings.py' file add the following code under 'BASE_DIR' 
  `TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')`

  Add the 'BASE_DIR' to 'DIRS' in the 'TEMPLATES' variable list
  ```python
      TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
  ```

**Setup the Allowed hosts**

  Also add the '.herokuapp.com' to the list of allowed hosts:  
  `ALLOWED_HOSTS = ['.herokuapp.com']` Note the '`.`'

**Create the Proccess file and necessary directories**

 1. Create the needed 'media','static' and 'templates' directories in top level of the project
    next to manage.py.
 2. Create a file named 'Procfile' without any extention in the same level.
 3. Add the following command to the 'Procfile':
    `web: gunicorn Myproject_name.wsgi`
    - 'web' tells heroku this is a process that accepts an Http traffic.
    - 'gunicorn' is the server used.
    - 'wsgi' stands for web services gateway interface, is a standard that allows Python to integrate
       with web services.
  4. Push to Github.

**Initial Deploy**

 1. From Heroku dashboard go to 'Deploy' tab.
 2. Choose 'GitHub' for deployment mehtod and search for the repositorry from the list
    (type the repo name and choose it in the field).
 3. Select 'Deplopy branch' for manual deployment.
 4. when the Build is finished it should say that the deployment is successful.
 5. Open the app then the page will open and you will see a text says 
    'the install worked successfully' from Django.

**Later Deploy**

 1. Set `DEBUG = False`.
 2. Commit and push to GitHub.
 3. In heroku choose the app and go to settings tab then click on 'reveal config vars'.
 4. Delete 'DISABLE_COLLECTSTATIC' variable.
 5. Deploy your app as in the previous step.
 6. When the build is finished click on 'View' to see the app in the browser
    you can click on 'Open App' in the top of the page also.

<u>[Back To Top](#table)</u>
<hr/>

<h2 id="fork">Forking the repository</h2>

To fork the repository in GitHub
1. Click on this [link](https://github.com/kasemdeautsch/PP4) to open the repository.
2. In the top right-hand corner click on fork.
3. This will take you to your own repository to a fork with the same name as the original branch.

<u>[Back To Top](#table)</u>
<hr/>
<h2 id="clone">Cloning the repository</h2>

1. Go to the [repository](https://github.com/kasemdeautsch/PP4) in GitHub.
2. Click on the green 'code' button in the right, select HTTPs and copy the link.
3. In your IDE change the current directory to the one you want to create this clone in
   or create a new directory under some name.
4. Type git clone, and paste the link you copied and press Enter to create a local cloan.

Information about creating and managing repositories is [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)

<u>[Back To Top](#table)</u>
<hr/>

<h2 id="credits">Credits</h2>

**Code**

I used the following walkthroughs to get my project done and shaped.

- Firstly Thanks to Code Institue 'I think Therefor I Blog' project:  
  Thanks for the course designing and the material given in this course, I realy liked this course 
  as it explains everything in details.  
  The header and the card idea inspired from this project

- Secondly the student project [Restaurant](https://github.com/Pramilashanmugam/Restaurant)
  this project inspired me a lot and I used it to write my documentation as I was confused
  what to write in my README file, and helped me in creating the needed table fields 
  in the reservations.

Sites I visited alway for problem solving:

- [Django documentation](https://docs.djangoproject.com/en/4.2/)
- [Bootstrap documentation](https://getbootstrap.com/)
- [Django Allauth ](https://django-allauth.readthedocs.io/en/latest/)
- [Google ](https://www.google.com)
- [Balsamiq](https://balsamiq.com/wireframes/)
- The amazing AI tool [Perplexity](https://www.perplexity.ai/)
- [slack members](https://app.slack.com/)


**Persons**
- All Code Institute staff.
- My mentor Rory Patric for the help and guiding.
- My facilitator Kristyna for informations I need.
- All tutors, specially Roman, Rebecca, Oisin.
- All my famiy members.

<u>[Back To Top](#table)</u>
<hr/>
