# Wannabe Healthy: Milestone 4 Project

<p align ="center">      
     <img src="assets/images/readme/images/"  alt="" />    
</p>
<br/>  

 
## Introduction <a name="introduction"></a>  

Wannabe Healthy is the 4th Project for the Code Institute and the Project is a Full Stack website using the Django Framework. The website's content deals with health related topics. It encompasses a Blog with various health categories and a Recipe section which concentrates on health enhancing recipes.

<br/>

[Visit the WannabeHealthy Site](https://.herokuapp.com/)  

[Visit the WannabeHealthy Repository](https://github.com/MHickey2/)

<br/>    

# Table of Contents <a name="toc"></a>

- [Wannabe Healthy: Milestone 4 Project](#wannabe-healthy-milestone-4-project)
  - [Introduction ](#introduction-)
- [Table of Contents ](#table-of-contents-)
  - [UX Strategy ](#ux-strategy-)
    - [The Business Goals of the Website: ](#the-business-goals-of-the-website-)
    - [The Target Customer: ](#the-target-customer-)
      - [Return to Table of Contents](#return-to-table-of-contents)
  - [User Stories  ](#user-stories--)
    - [As a website User I can...](#as-a-website-user-i-can)
    - [As a logged in User I can... ](#as-a-logged-in-user-i-can-)
    - [As a website superuser, I can …..    ](#as-a-website-superuser-i-can-----)
      - [Return to Table of Contents](#return-to-table-of-contents-1)
  - [Layout  ](#layout--)
  - [Colour  Scheme  ](#colour--scheme--)
  - [Typography    ](#typography----)
  - [Imagery    ](#imagery----)
  - [Wireframes    ](#wireframes----)
      - [Return to Table of Contents](#return-to-table-of-contents-2)
    - [Database Diagram](#database-diagram)
      - [Return to Table of Contents](#return-to-table-of-contents-3)
  - [Features  ](#features--)
    - [Home Page   ](#home-page---)
    - [Blog Section      ](#blog-section------)
    - [Blog Search   ](#blog-search---)
    - [Add Blog     ](#add-blog-----)
    - [Edit Blog     ](#edit-blog-----)
    - [Delete Blog     ](#delete-blog-----)
    - [Blog Detail Page      ](#blog-detail-page------)
    - [About Page    ](#about-page----)
    - [Recipes Page   ](#recipes-page---)
    - [Recipes Search   ](#recipes-search---)
    - [Add Recipe   ](#add-recipe---)
    - [Edit Recipe   ](#edit-recipe---)
    - [Delete Recipe   ](#delete-recipe---)
    - [Recipe Detail Page   ](#recipe-detail-page---)
    - [Signup Page   ](#signup-page---)
    - [Login  Page   ](#login--page---)
    - [Logout Page   ](#logout-page---)
    - [Profile Page   ](#profile-page---)
      - [Return to Table of Contents](#return-to-table-of-contents-4)
  - [Future Implementation  ](#future-implementation--)
      - [Return to Table of Contents](#return-to-table-of-contents-5)
  - [Tools and Technology  ](#tools-and-technology--)
    - [Language Used:](#language-used)
    - [Technology Used:](#technology-used)
      - [Django Packages](#django-packages)
      - [Return to Table of Contents](#return-to-table-of-contents-6)
  - [Testing  ](#testing--)
    - [Manual Testing   ](#manual-testing---)
      - [Feature being tested and Result](#feature-being-tested-and-result)
    - [User Story Testing](#user-story-testing)
      - [As a Website User I want to .....](#as-a-website-user-i-want-to-)
      - [As a logged in User I want to …...](#as-a-logged-in-user-i-want-to-)
      - [As a Superuser/Admin I want to …..](#as-a-superuseradmin-i-want-to-)
    - [General Testing   ](#general-testing---)
      - [Browser Testing](#browser-testing)
      - [Responsive Testing](#responsive-testing)
    - [Validation      ](#validation------)
      - [HTML Checker](#html-checker)
      - [Lighthouse Testing](#lighthouse-testing)
      - [Return to Table of Contents](#return-to-table-of-contents-7)
  - [Bugs and Issues  ](#bugs-and-issues--)
    - [Resolved ](#resolved-)
    - [Unresolved ](#unresolved-)
      - [Return to Table of Contents](#return-to-table-of-contents-8)
  - [Deployment ](#deployment-)
      - [Creating the Django app  ](#creating-the-django-app--)
    - [How to make a local Clone ](#how-to-make-a-local-clone-)
    - [How to fork a GitHub Repository ](#how-to-fork-a-github-repository-)
    - [Student Template ](#student-template-)
    - [Deploying to Heroku ](#deploying-to-heroku-)
      - [Return to Table of Contents](#return-to-table-of-contents-9)
  - [Credits ](#credits-)
      - [Return to Table of Contents](#return-to-table-of-contents-10)
  - [Acknowledgements ](#acknowledgements-)
      - [Return to Table of Contents](#return-to-table-of-contents-11)

----

## UX Strategy <a name="uxstrategy"></a>

<br/> 

### The Business Goals of the Website: <a name="businessgoals"></a>
- No commercial goals, but the site's goal is to to provide a resource for those seeking to improve their health.
  
  <br/> 

### The Target Customer: <a name="targetcustomer"></a>

Anyone with the desire to improve their health.

 <br/>  

 #### [Return to Table of Contents](#toc)

----

Site User

The user is really anyone who wants to gain a healthier lifestyle. They can not only view present blogs and recipes but can play more of an interactive role and contribute their own blogs and recipes.  In this way the stite will grow organically and will be open to evolving depending on the user interaction. There will also be a contact where users can recommend ideas for expanding the site.

Site Goals
The site allows the user to know the content of the site easily and can navigate through it easily.
The user will be able to use the search facility to find specific blogs by category and title.
The user when logged in will be able to contribute to the site in regards to blogs and recipes, they will also be able to like and comment on individual blogs and recipes.
The user will be able to add a profile to the site

<br>

## User Stories  <a name="userstories"></a>

<br>

### As a website User I can...<a name="websiteuser"></a>
1. Navigate around the site and easily view the type of content available.
2. View a collection of Blogs in the blog Section.
3. Search the blog section for particular categories or by title content.
4. Click on a blog item and view more indepth content of the selected blog.
5. Register for an account to avail of full features of the site.
6. View the number of likes on a blog.
7. View comments left for different blogs in the collection.
8. View a collection of Recipes in the Recipe Page.
9. Search through recipes for particular categories or by name in title.
10. Click on a Recipe to see full details of that recipe.
11. View the number of likes on a Recipe.
12. View any comments left on a Recipe. 

  

  <br/>

### As a logged in User I can... <a name="loggedinuser"></a>  
-
1. I can add a new post or a recipe.
2. I can like/unlike a blog or recipe on the site.
3. I can leave comments on particular blogs and recipes.
4. Update my Profile for the site by adding a Bio and Image.
5. I can edit a Blog or Recipe that I have submitted to the site.
6. I can delete a Recipe or Blog that I have submitted to the site.

 
 <br/>

### As a website superuser, I can …..    <a name="superuser"></a>

1. Create and publish a new blog or recipe.
2. Create draft recipes and blog posts that can be finalised later.
3. Create a new user, recipes, blogs and categories.
4. Delete user, blogs, recipes, categories and comments.
5. Can approve user's comments.

  <br/>  

#### [Return to Table of Contents](#toc)  
----
## Layout  <a name="layout"></a> 

<br/>

## Colour  Scheme  <a name="colourscheme"></a>


## Typography    <a name="typography"></a>

The 'Roboto' font is the main font used for the whole project  


<br>


## Imagery    <a name="imagery"></a>

<br>

 
## Wireframes    <a name="wireframes"></a>

<br>


<br>


 #### [Return to Table of Contents](#toc)
----

### Database Diagram
<br>

<p align ="center">      
     <img src="assets/images/readme/images/"  alt="database diagram" />    
</p>

<br/> 


 #### [Return to Table of Contents](#toc)
----

<br>

## Features  <a name="features"></a>

<br>

### Home Page   <a name="homepage"></a>

The home page has an intro image and a short paragraph of text explaining the purpose of
the site.  
  

<br>

<p align ="center">      
     <img src="assets/images/readme/images/"  alt="" />    
</p>

<br/> 

### Blog Section      <a name="blogsection"></a>

On the home page there is a blog section which holds a collection of blogs ordered with the most recent blog at the top. The pagination allows for the blogs to be distributed according to the number of blogs it contains.

<br>

<p align ="center">      
     <img src="assets/images/readme/images/"  alt="" />    
</p>

<br/> 

### Blog Search   <a name="blogsearch"></a>

The website user can use the search facility to find specific categories, that are presented to the user and they can also search by a name in the title.


<p align ="center">      
     <img src="assets/images/readme/images/"  alt="" />    
</p>

<br/> 

###  Add Blog     <a name="addblog"></a>

As a logged in User you can add a blog to the site, when you press on the add blog link it will take you to the add blog page, when this form is completed you will be redirected to the home page, where your new blog will be displayed.

<br>

<p align ="center">      
     <img src="assets/images/readme/images/"  alt="" />    
</p>

<br/> 

### Edit Blog     <a name="editblog"></a>

As a logged in User you will be able to see the edit button below your submitted blogs, when you use the edit button you will be redirected to the edit blog page, where you can update your blog, when the form is completed you will be redirected to the home page.

<br>

<p align ="center">      
     <img src="assets/images/readme/images/"  alt="" />    
</p>

<br/> 


###  Delete Blog     <a name="deleteblog"></a>

As a logged in User you will be able to see the delete button below your submitted blogs, when you use the delete button you will be redirected to the delete blog page, where you can delete your blog, when the form is completed you will be redirected to the home page.


<br>

<p align ="center">      
     <img src="assets/images/readme/images/"  alt="" />    
</p>

<br/>

### Blog Detail Page      <a name="blogdetailpage"></a>

When you select a blog, you will be redirected to the blog detail page, this page will show the full content for that specific blog. If you are a logged in user you can add a comment. This comment will have to be approved by the admin before it will be displayed on the site.

<br>

<p align ="center">      
     <img src="assets/images/readme/images/"  alt="" />    
</p>

<br/> 

###  About Page    <a name="aboutpage"></a>

The About Page again contains a brief synopsis of the site and contain information panels that display the main elements of the site. The accompanying links will take you to either the blog section or the recipe section of the site.
<br>

<p align ="center">      
     <img src="assets/images/readme/images/"  alt="" />    
</p>

<br/> 

###  Recipes Page   <a name="recipespage"></a>

On the Recipes page there is a collection of Recipes ordered with the most recent Recipe at the top. The pagination allows for the Recipes to be distributed according to the number of recipes in the collection.

<br>

<p align ="center">      
     <img src="assets/images/readme/images/"  alt="" />    
</p>

<br/> 

###  Recipes Search   <a name="recipessearch"></a>

The website user can use the search facility to find specific categories ie Breakfast, Lunch, Dinner, Dessert and Soup/Salad. You can also search according to a specific word in the title.

<br>

<p align ="center">      
     <img src="assets/images/readme/images/"  alt="" />    
</p>

<br/> 

###  Add Recipe   <a name="addrecipe"></a>

As a logged in User you can add a Recipe to the site, when you press on the add a Recipe  link it will take you to the 'add Recipe page', when this form is completed you will be redirected to the Recipes page, where your new Recipe will be displayed.


<br>

<p align ="center">      
     <img src="assets/images/readme/images/"  alt="" />    
</p>

<br/> 

###  Edit Recipe   <a name="editrecipe"></a>

As a logged in User you will be able to see the edit button below your submitted Recipe, when you use the edit button you will be redirected to the 'edit your Recipe page', where you can update your Recipe, when the form is completed you will be redirected to the Recipes page.

<br>

<p align ="center">      
     <img src="assets/images/readme/images/"  alt="" />    
</p>

<br/> 

###  Delete Recipe   <a name="deleterecipe"></a>

As a logged in User you will be able to see the delete button below your submitted Recipe, when you use the delete button you will be redirected to the delete Recipe page, where you can delete your Recipe, when the form is completed you will be redirected to the Recipes page.

<br>

<p align ="center">      
     <img src="assets/images/readme/images/"  alt="" />    
</p>

<br/> 

###  Recipe Detail Page   <a name="recipedetailpage"></a>

When you select a Recipe, you will be redirected to the Recipe detail page, this page will show the full content for that specific Recipe. If you are a logged in user you can add a comment. This comment will have to be approved by the admin before it will be displayed on the site.

<br>

<p align ="center">      
     <img src="assets/images/readme/images/"  alt="" />    
</p>

<br/> 

###  Signup Page   <a name="signuppage"></a>

On the Signup Page, a new user can sign up for the Wannabe Healthy website by filling out and submitting the form.

<br>

<p align ="center">      
     <img src="assets/images/readme/images/"  alt="" />    
</p>

<br/>

###  Login  Page   <a name="loginpage"></a>

A registered User can log in to the website by inputting the username and password and they will have full access to all the features of the site.
<br>

<p align ="center">      
     <img src="assets/images/readme/images/"  alt="" />    
</p>

<br/> 

###  Logout Page   <a name="logoutpage"></a>

In the Logout Page, the User can confirm that they want to exit the website.

<br>

<p align ="center">      
     <img src="assets/images/readme/images/"  alt="" />    
</p>

<br/>  

###  Profile Page   <a name="profilepage"></a>

On the Profile Page, the User can have access to their own profile information and can update their information for the site, including adding a bio and a profile image. The profile will be created when they register for the site.

<br>

<p align ="center">      
     <img src="assets/images/readme/images/"  alt="" />    
</p>

<br/> 


 #### [Return to Table of Contents](#toc)
----
 ## Future Implementation  <a name="future"></a>

 <br>

 

<br>

 #### [Return to Table of Contents](#toc)
----
 ## Tools and Technology  <a name="technology"></a>

### Language Used:

-   [Python 3.8.10](https://www.python.org/)
-   [HTML5](https://en.wikipedia.org/wiki/HTML5)        &nbsp; [CSS3](https://en.wikipedia.org/wiki/CSS)
-   [JavaScript](https://www.javascript.com/)
-   [Django](https://www.python.org/)

### Technology Used:

-   [Git:](https://git-scm.com/) used for version control, updated changes and commited changes and this in turn updated in Heroku 
-   [GitHub:](https://github.com/) is the respository for all the git pushes.
-   [Gitpod](https://gitpod.io/) was the IDE Editor
-   [Heroku:](https://heroku.com) used to deploy the application.
-   [Google Chrome Dev Tools](https://developer.chrome.com/docs/devtools/)
-   [Markdown](https://markdown-guide.readthedocs.io/en/latest/)
-   [Cloudinary](https://cloudinary.com/)
-   [PostgreSQL](https://www.postgresql.org/)
-   [Bootstrap](https://getbootstrap.com/)
-   [Draw.io](https://drawio-app.com/)
 
#### Django Packages

* [Gunicorn](https://gunicorn.org/)<br>
   As the server for Heroku
* [Cloudinary](https://cloudinary.com/)<br>
   Was used to host the static files and media
* [Dj_database_url](https://pypi.org/project/dj-database-url/)<br>
   To parse the database URL from the environment variables in Heroku
* [Psycopg2](https://pypi.org/project/psycopg2/)<br>
   As an adaptor for Python and PostgreSQL databases
* [Summernote](https://summernote.org/)<br>
   As a text editor
* [Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html)<br>
   For authentication, registration, account
   management
* [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)<br>
   To style the forms
 

 #### [Return to Table of Contents](#toc)
----
## Testing  <a name="testing"></a>
<br>

### Manual Testing   <a name="manual"></a>

<br>

#### Feature being tested and Result                                                    


- Start Screen displays when Heroku link is used.   :heavy_check_mark:

 


<br>

### User Story Testing<a name="userstorytesting"></a>

 <br/>

#### As a Website User I want to .....

- 
- 
- 

<br>

#### As a logged in User I want to …...  

-    
-         
- 

<br>

#### As a Superuser/Admin I want to …..    
- 
- 
- 
- 
 
- 


<br>

### General Testing   <a name="general"></a>

<br>

#### Browser Testing

The site was tested on Google Chrome, Firefox and Microsoft edge, and there seemed to be no issues on any of the browsers.

<br>


#### Responsive Testing

In regards to responsive testing

<br>

<p align ="center">      
     <img src="assets/images/readme/images/"  alt="Responsive Testing Image" />    
</p>
<br/> 

<br>

### Validation      <a name="validation"></a>

<br>

I used pep8 validation 
<p align ="center">  
    
     <img src="assets/images/readme/images/"  alt="" />    
</p>
<br/> 

<p align ="center">      
     <img src="assets/images/readme/images/"  alt="" />    
</p>
<br/> 

<br>

#### HTML Checker     


<p align ="center">      
     <img src="assets/images/readme/images/"  alt="HTML Validation" />    
</p>
<br/>


#### Lighthouse Testing


<p align ="center">      
     <img src="assets/images/readme/images/"  alt="lighouse testing specs" />    
</p>
<br/> 


 #### [Return to Table of Contents](#toc)
----

 ## Bugs and Issues  <a name="bugs"></a>

<br>

 ### Resolved <a name="resolved"></a>


 
 <br>

 ### Unresolved <a name="unresolved"></a>

 

<br>

 #### [Return to Table of Contents](#toc)
----


 ## Deployment <a name="deployment"></a>

 <br>

#### Creating the Django app  <a name="django-app"></a>

 ### How to make a local Clone <a name="clone"></a>
1. Navigate to the main page of the repository.
2. Click the green Code Button at top right of the repository.
3. Copy the url for the repository.
4. Open Git Bash and Change the current working directory to where you want the cloned directory.
5. Type git clone, and then paste the URL you previously copied using $ git clone. 
6. Pressing enter will then create your clone.  

<br/>  


### How to fork a GitHub Repository <a name="fork"></a>
1. Log into GitHub and go to the required Repository.
2. The Fork button is found at the top right corner of the page.
3. When you click this button you will have a copy of the repository in your own GitHub account.  

<br/>  


 ### Student Template <a name="studenttemplate"></a>
 This Template has been provided by the Code Institute and includes a number of tools to make life easier and has been used within this present site.    

<br/>

### Deploying to Heroku <a name="heroku"></a>
- After registering on the Heroku site, you can see the dashboard. You can select 'New' and then click 'Create new app'. You need to pick a unique name for your app, it will let you know if it is  to available to use.
- Select your region and create your app.
- Go to the settings tab and scroll until you find the config vars section and pick 'Reveal config vars',
in this case I added 'PORT' into the key field and added '8000' into the value field and click 'add'.
- If you have credentials, for your project, you must create another config vars called 'CREDS' and 
you would paste the JSON into the value field.
- You have to to the builldpacks section and click 'add buildpack'.
- In this case I added 'Python' and 'saved changes, and did the same with 'Node'.
- Next you go to the Deploy tab and you select 'github' and confirm connection to your GitHub Account.
- You search for your project repository and click to 'connect'.
- Under the deploy options, you can chose automatic deploys, this allow you to automatically deploy each
time you push to your Repository.
- To deploy, you would choose what branch you want to deploy and click on 'Deploy Branch'.
- It takes a little time to build your app but when it is ready you can open your app by using the link provided
  
<br> 

More information is available at [https://docs.github.com/en](https://docs.github.com/en), in regards to GitHub and is a great reference point for all GitHub queries.

 
#### [Return to Table of Contents](#toc)
----
 ## Credits <a name="credits"></a>
     

 I also used the following online resources:

- [Code Institute](https://codeinstitute.net/ie/)
- [Slack](https://slack.com/intl/en-ie/) 
- [Stack OverFlow](https://stackoverflow.com)
- [YouTube](https://www.youtube.com/)
- [W3Schools.com](https://www.w3schools.com/)

<br>

#### [Return to Table of Contents](#toc)
----
 ## Acknowledgements <a name="acknowledgements"></a>

 

<br>

 #### [Return to Table of Contents](#toc) 
----

 
