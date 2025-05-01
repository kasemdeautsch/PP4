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

**Structure / (layout, user-flow)**  
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

**Skelton / Wireframes:**\
An initial design of the layout done by drawing the layout on paper and then using the "Balsamiq" translated
to a "mockup", this helped in Brainstorming me to imagine how the key contents will be placed and how the user
will interact with them.



## Features

**Existing Features**

- Navigation Bar
  - Featured at the top of the page for all pages, with
    links to the main page (Home) and otherpages.
  - The other navigations to the right: Home, History, Gallery, Contacts, and all linking to 
    different pages of the website.
  - The navigation is in a color that contrasts with the background.
  - The navigation shows clearly the name of the website to make it easy to navigate the other
    pages.
    ![](/media/header.png)
- The Header
  - The Header contains the Navigation Bar and the logo which is a Heading with the site name: SYRIA HOME 
   on the left which leads to landing home page, and the rest links to the right.
- The footer
  - The footer includes links to the social media sites which should lead to social media chanels of this 
      website, The links will open to a new tab to allow easy navigation for the user.
  - The value of the footer is that it encourages users to keep connected via social media.
     ![](/media/footer.png)
- The Gallery
  - the gallery page displays photos of most cities in Syria and the most sites that people visits.
  - The page is usefull so that it contains the places that can the visitor visits when he is there.
    ![](/media/gallery.png)
- The Signup page
  - this page allows the user to sign up to the website so that they become a member.
      for further informations.
  - It aquires the user to enter his email address and full name.
    ![](/media/signup.png)

**Features Left to Implement**
- This website is basic and ment to be more developed and contains several media and content
  however I hadn't more time.
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