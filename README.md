# Wannabe Healthy: Milestone 4 Project

<p align ="center">      
   <img src="media/readme/wannaberesp.png"  alt="AmIResponsive" />       
</p>
<br/>  

 
# Introduction <a name="introduction"></a>

Wannabe Healthy is the 4th Project for the Code Institute and the Project is a Full Stack website using the Django Framework. The website's content deals with health related topics. It encompasses a Blog with various health categories and a Recipe section which concentrates on health enhancing recipes.  When logged in a User can add, edit or delete their own submitted Blog/Recipe. A logged in User can like/unlike a post or recipe or add comments for either. A logged in User can also view and Update their own Profile with an uploaded image and a Bio. 

<br/>

[Visit the WannabeHealthy Site](https://.herokuapp.com/)  

[Visit the WannabeHealthy Repository](https://github.com/MHickey2/)

<br/>  

# Table of Contents <a name="toc"></a>

- [Wannabe Healthy: Milestone 4 Project](#wannabe-healthy-milestone-4-project)
- [Introduction ](#introduction-)
- [Table of Contents ](#table-of-contents-)
  - [1. UX Strategy ](#1-ux-strategy-)
    - [1. The Business Goals of the Website: ](#1-the-business-goals-of-the-website-)
    - [2. The Target Customer: ](#2-the-target-customer-)
      - [Return to Table of Contents](#return-to-table-of-contents)
  - [2. User Stories  ](#2-user-stories--)
    - [1. As a website User I can...](#1-as-a-website-user-i-can)
    - [2. As a logged in User I can... ](#2-as-a-logged-in-user-i-can-)
    - [3. As a website superuser, I can …..    ](#3-as-a-website-superuser-i-can-----)
  - [3. Agile Methodology](#3-agile-methodology)
      - [Return to Table of Contents](#return-to-table-of-contents-1)
  - [3. Design  ](#3-design--)
    - [1. Colour  Scheme  ](#1-colour--scheme--)
    - [2. Typography    ](#2-typography----)
    - [3. Imagery    ](#3-imagery----)
    - [4. Website Structure    ](#4-website-structure----)
    - [5. Wireframes    ](#5-wireframes----)
      - [Return to Table of Contents](#return-to-table-of-contents-2)
  - [4. Database Diagram](#4-database-diagram)
      - [Return to Table of Contents](#return-to-table-of-contents-3)
  - [5. Features  ](#5-features--)
    - [1. Home Page   ](#1-home-page---)
    - [2. Blog Section      ](#2-blog-section------)
    - [3. Blog Search   ](#3-blog-search---)
    - [4. Add Blog     ](#4-add-blog-----)
    - [5. Edit Blog     ](#5-edit-blog-----)
    - [6. Delete Blog     ](#6-delete-blog-----)
    - [7. Blog Detail Page      ](#7-blog-detail-page------)
    - [8. About Page    ](#8-about-page----)
    - [9. Recipes Page   ](#9-recipes-page---)
    - [10. Recipes Search   ](#10-recipes-search---)
    - [11. Add Recipe   ](#11-add-recipe---)
    - [12. Edit Recipe   ](#12-edit-recipe---)
    - [13. Delete Recipe   ](#13-delete-recipe---)
    - [14. Recipe Detail Page   ](#14-recipe-detail-page---)
    - [15. Profile Page   ](#15-profile-page---)
    - [16. Edit Profile  Page   ](#16-edit-profile--page---)
    - [17. Signup Page   ](#17-signup-page---)
    - [18. Login Page   ](#18-login-page---)
    - [19. Logout Page   ](#19-logout-page---)
      - [Return to Table of Contents](#return-to-table-of-contents-4)
  - [6. Future Implementation  ](#6-future-implementation--)
      - [Return to Table of Contents](#return-to-table-of-contents-5)
  - [7. Tools and Technology  ](#7-tools-and-technology--)
    - [Language Used:](#language-used)
    - [Technology Used:](#technology-used)
      - [Django Packages](#django-packages)
      - [Return to Table of Contents](#return-to-table-of-contents-6)
  - [8. Testing  ](#8-testing--)
  - [9. Bugs and Issues  ](#9-bugs-and-issues--)
    - [Resolved ](#resolved-)
    - [Unresolved ](#unresolved-)
      - [Return to Table of Contents](#return-to-table-of-contents-7)
  - [10. Deployment ](#10-deployment-)
      - [Creating the Django app  ](#creating-the-django-app--)
    - [How to make a local Clone ](#how-to-make-a-local-clone-)
    - [How to fork a GitHub Repository ](#how-to-fork-a-github-repository-)
    - [Student Template ](#student-template-)
    - [Deploying to Heroku ](#deploying-to-heroku-)
      - [Return to Table of Contents](#return-to-table-of-contents-8)
  - [Credits ](#credits-)
      - [Return to Table of Contents](#return-to-table-of-contents-9)
  - [Acknowledgements ](#acknowledgements-)
      - [Return to Table of Contents](#return-to-table-of-contents-10)

----


## 1. UX Strategy <a name="uxstrategy"></a>
----

<br/> 

### 1. The Business Goals of the Website: <a name="businessgoals"></a>
- No commercial goals, but the site's goal is to to provide a resource for those seeking to improve their health and learn about health topics.
  
  <br/> 

### 2. The Target Customer: <a name="targetcustomer"></a>

Anyone with the desire to improve their health.
Anyone who wants to improve their Diet with healthy Recipes.

 <br/>  

 #### [Return to Table of Contents](#toc)

----

Site User

The user is really anyone who wants to gain a healthier lifestyle. They can not only view present blogs and recipes but can play more of an interactive role and contribute their own blogs and recipes.  In this way the stite will grow organically and will be open to evolving dependg on the latest health trends. 

Site Goals
The site allows the user to know the content of the site easily and can navigate through it easily.
The user will be able to use the search facility to find specific blogs by category and title.
The user when logged in will be able to contribute to the site in regards to blogs and recipes, they will also be able to like and comment on individual blogs and recipes.
The user will be able to maintain a profile on the site and they can update their Profile details and Users can learn more about them.

<br>

## 2. User Stories  <a name="userstories"></a>

<br>

### 1. As a website User I can...<a name="websiteuser"></a>
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

### 2. As a logged in User I can... <a name="loggedinuser"></a> 

1. I can add a new post or a recipe.
2. I can like/unlike a blog or recipe on the site.
3. I can leave comments on particular blogs and recipes.
4. I can update my Profile for the site by adding a Bio and Image.
5. I can edit a Blog or Recipe that I have submitted to the site.
6. I can delete a Recipe or Blog that I have submitted to the site.

 
 <br/>

### 3. As a website superuser, I can …..    <a name="superuser"></a>

1. Create and publish a new blog or recipe.
2. Create draft recipes and blog posts that can be finalised later.
3. Create a new user, recipes, blogs and categories.
4. Delete user, blogs, recipes, categories and comments.
5. Can approve user's comments.

  <br/> 

## 3. Agile Methodology

The project was developed using Agile Methodology and it was by use of the GitHub Projects functionality within the GitHub Repository. The issues can be found [Here](https://github.com/MHickey2/Wannabe-Healthy/issues) and this is the link for the [WannabeProject Board](https://github.com/users/MHickey2/projects/1)

<br/> 

#### [Return to Table of Contents](#toc)  
----

## 3. Design  <a name="design"></a> 

<br/>

### 1. Colour  Scheme  <a name="colourscheme"></a>

The colour scheme has primarily a green colour, research has shown that green has a strong link with health related topics and it also relates to nature and I felt it was a natural choice for the content of the site.

<br>

### 2. Typography    <a name="typography"></a>

Google Fonts were used within the website. The 'Roboto' font is the main font used for the whole project, both for regular text and headings. Sans serif is the fallback font in case other font is not available. See below for example of font in use.

The font color was #313131, which is a good font to help counter eye strain.

The main title for the site and the navbar links use the 'Abril Fatface' font, A font it displays both neutrality and a strong presence on the page which helps to attract reader attention with the measured tension of its curves, good color and high contrast.

Other Fonts were used within the Recipe Details Section and the main heading use the Marhey Font, as they gave a certain quirky touch to the Recipes.


<br>


### 3. Imagery    <a name="imagery"></a>

The Logo was created on a Logo Website, as the theme was health related, I used predominantly green in the logo iteself and the logo had a strong influence on the overall website theme going forward.

The imagery of the site focuses on a healthy theme, the images were souced from the Pexels site and supplement either the blog or the recipe. The images are all self sourced, but the user can update images to supplement their own blog/recipe.

There are also images sporadically throughout the site, The home page has an image of a healthy woman, conveying a person with a healthy lifestyle. The about page again, shows a healthy woman living her best life and the information panels show images focuses on the main themes within the site.

<br>

### 4. Website Structure    <a name="structure"></a>

The website follows the standard website structure. The Logo and the website name are on the left hand side, and the naigation to the right, on the top of all pages. Within the Account Nav Link the user can either register or login to the site. When the user logs in they can see the Profile link and the logout button. The logged in user's image will also be visible. When the website is on smaller screens, there is a hamburger meu, with dropdown navigation items. The footer element is also available on all pages, with site information, contact details and social media icons.
 
 The website consists of the following Pages:
 - The Home Page, with an introduction to the site and holds the blog section and the search bar.
 - The Post Detail Page, that shows the information for individual blogs.
 - The Add Post Page, which is a form that allows the logged in User to add a blog.
 - The Edit Post Page, which is a form that allows the user to edit their own post.
 - The Delete Post Page, which is a form that allows the user to delete their own post.
 - The About Page, which gives more information on the site and specific panels that shows information on main topics.
 - The Recipe Page, with an introduction to Recipes and holds the recipe section and the search bar.
 - The Recipe Detail Page, that shows the information for individual Recipes.
 - The Add Recipe Page, which is a form that allows the logged in User to add a Recipe.
 - The Edit Recipe Page, which is a form that allows the user to edit their own Recipe.
 - The Delete Recipe Page, which is a form that allows the user to delete their own Recipe.
 - The Profile Page, which contains profile information on the registered User.
 - The Edit Profile Page, which contains a form that allows the User to add/update their profile information.
 - The Sign Up Page, consists of a form where a new user can register for the site.
 - The LogIn Page, consists of a form where the user can login to the site.
 - The logout Page, consists of a form where the user can logout of the site.

### 5. Wireframes    <a name="wireframes"></a>

The Wireframes for the site were created in Figma, I concentrated on the standard websize and the mobile size. The midlevel sizes were generally in keeping with the main websize but just on a smaller scale. The Wireframes can be found below:

<details>
  <summary>1. Home Page Wireframes</summary>
  <p align="center">
     <img src="assets/readme/wireframes/Home Page Wireframes.png"  alt="Home Page Wireframe" />    
</p>
</details>

<details>
  <summary>2. Add Post Page Wireframe</summary>
  <br/>
<p align="center">
  <img src="assets/readme/wireframes/Add Post Wireframes.png" alt="Add Post Page Wireframe"/>
</p>
</details>

<details>
  <summary>3. Edit Post Page Wireframe</summary>
  <br/>
<p align="center">
  <img src="assets/readme/wireframes/Edit Post Wireframes.png" alt="Edit Post Page Wireframe" />
</p>
</details>

<details>
  <summary>4. Delete Page Wireframe</summary>
  <br/>
<p align="center">
  <img src="assets/readme/wireframes/Delete Post Wireframes.png" alt="Delete Page Wireframe" />
</p>
</details>

<details>
  <summary>4. Post Detail Page</summary>
  <br/>
<p align="center">
  <img src="assets/readme/wireframes/Post Detail Wireframes.png" alt="Post Detail Page Wireframe" />
</p>
</details>

<details>
  <summary>4. About Page</summary>
  <br/>
<p align="center">
  <img src="assets/readme/wireframes/About Page Wireframes.png" alt="About Page Wireframe" />
</p>
</details>

<details>
  <summary>4. Recipes Page</summary>
  <br/>
<p align="center">
  <img src="assets/readme/wireframes/Recipes Page Wireframes.png" alt="Recipes Page Wireframe" />
</p>
</details>

<details>
  <summary>4. Add Recipe Page</summary>
  <br/>
<p align="center">
  <img src="assets/readme/wireframes/Add Recipe Page Wireframes.png" alt="Add Recipe Page Wireframe" />
</p>
</details>

<details>
  <summary>4. Edit Recipe Page</summary>
  <br/>
<p align="center">
  <img src="assets/readme/wireframes/Edit Recipe Page Wireframes.png" alt="Edit Recipe Page Wireframe" />
</p>
</details>

<details>
  <summary>4. Delete Recipe Page</summary>
  <br/>
<p align="center">
  <img src="assets/readme/wireframes/Delete Recipe Page Wireframes.png" alt="Delete Recipe Page Wireframe" />
</p>
</details>

<details>
  <summary>4. Recipe Detail Page</summary>
  <br/>
<p align="center">
  <img src="assets/readme/wireframes/Recipe Detail Page Wireframes.png" alt="Recipe Detail Page Wireframe" />
</p>
</details>

<details>
  <summary>4. Profile Page</summary>
  <br/>
<p align="center">
  <img src="assets/readme/wireframes/Profile Page Wireframes.png" alt="Profile Page Wireframe" />
</p>
</details>

<details>
  <summary>4. Edit Profile Page</summary>
  <br/>
<p align="center">
  <img src="assets/readme/wireframes/Edit Profile Page Wireframes.png" alt="Edit Profile Page Wireframe" />
</p>
</details>

<details>
  <summary>4. Registration Page</summary>
  <br/>
<p align="center">
  <img src="assets/readme/wireframes/Registration Page Wireframes.png" alt="Registration Page Wireframe" />
</p>
</details>

<details>
  <summary>4. Login Page</summary>
  <br/>
<p align="center">
  <img src="assets/readme/wireframes/Login Page Wireframes.png" alt="Login Page Wireframe" />
</p>
</details>

<details>
  <summary>4. Logout Page</summary>
  <br/>
<p align="center">
  <img src="assets/readme/wireframes/Logout Page Wireframes.png" alt="Logout Page Wireframe" />
</p>
</details>


 #### [Return to Table of Contents](#toc)
----

## 4. Database Diagram
<br>

<p align ="center">      
     <img src="media/readme/"  alt="database diagram" />    
</p>

<br/> 


 #### [Return to Table of Contents](#toc)
----

<br>

## 5. Features  <a name="features"></a>

There are features common to all pages in the site and these are foundin the base.html page. These include:

- The Logo and Site Title:

<br>

<p align ="center">      
     <img src="assets/readme/images/logotitle.png"  alt="Logo and Title" />    
</p>

<br/> 
  

- The Navigation Bar:
  The navigation exists in different forms, for a general user the navigation contains home, about, recipes and an account dropdown with register and login options. For a logged in user the naviation contains, home, about, recipes, profile and logout. When logged in you will also see your profile picture to the right of the other options.

  <br>

<p align ="center">      
     <img src="assets/readme/images/navbar.png"  alt="Navbar" />    
</p>

<br/> 

  Ons smaller screens, there is a hamburger menu where the navigation items appear in a collapsable dropdown menu.

<br>

<p align ="center">      
     <img src="assets/readme/images/navmobile.png"  width="300" height="250" alt="navbar mobile" />    
</p>

<br/> 

- The Footer:
  The Footer contains a blurb on the site, some contact details and social media icons, also the copyright information on the WannabeHealthy site. 

 <br>

<p align ="center">      
     <img src="assets/readme/images/footer.png"  alt="footer" />    
</p>

<br/> 

<br>

### 1. Home Page   <a name="homepage"></a>

The home page has an introductory image and a short paragraph of text explaining the purpose of
the site, helping the user find out the theme of the site up front. 
  
<br>

<p align ="center">      
     <img src="assets/readme/images/intro.png"  alt="Intro to Site" />    
</p>

<br/> 

### 2. Blog Section      <a name="blogsection"></a>

On the home page there is a blog section which holds a collection of blogs ordered with the most recent blog at the top. The pagination allows for the blogs to be distributed according to the number of blogs it contains.

<br>

<p align ="center">      
     <img src="assets/readme/images/blog1.png"  width="700" height="700" alt="blog section" />    
</p>

<br/> 

### 3. Blog Search   <a name="blogsearch"></a>

The website user can use the search facility to find specific categories, and they can also search by a word in the title.
If there are results, they will be displayed to the user and if not the user will be given the message that there are no results, they can either search again or they can return to the home page blog display.


<p align ="center">      
     <img src="assets/readme/images/blogsearch.png"  alt="blogsearch" />    
</p>

<br/> 

<p align ="center">      
     <img src="assets/readme/images/noresults.png"  alt="search no results" />    
</p>

<br/> 

###  4. Add Blog     <a name="addblog"></a>

As a logged in User you can add a blog to the site, when you press on the add blog link it will take you to the add blog page, when this form is completed you will be redirected to the home page, where your new blog will be displayed.

<br>

<p align ="center">      
     <img src="assets/readme/images/add post.png"  alt="add post button" />    
</p>

<br/> 

<p align ="center">      
     <img src="assets/readme/images/addpost1.jpg" width="500" height="500"  alt="add post form" />    
</p>

<br/> 

### 5. Edit Blog     <a name="editblog"></a>

As a logged in User you will be able to see the edit button below your submitted blogs, when you use the edit button you will be redirected to the edit blog page, where you can update your blog, when the form is completed the user will be redirected to the home page.

<br>

<p align ="center">      
     <img src="assets/readme/images/editbutton.png"  alt="edit button" />    
</p>

<br/> 

<p align ="center">      
     <img src=""  alt="edit form" />    
</p>

<br/> 


###  6. Delete Blog     <a name="deleteblog"></a>

As a logged in User you will be able to see the delete button below your submitted blogs, when you use the delete button you will be redirected to the delete blog page, where you can delete your blog, when the form is completed you will be redirected to the home page and your blog will be deleted.


<br>

<p align ="center">      
     <img src="media/readme/"  alt="" />    
</p>

<br/>

### 7. Blog Detail Page      <a name="blogdetailpage"></a>

When you select a blog, you will be redirected to the blog detail page, this page will show the full content for that specific blog. If you are a logged in user you can add a comment. This comment will have to be approved by the admin before it will be displayed on the site. You can also like/unlike the post. You will also be able to see the Profile Picture and Bio for the Author of the Post.

<br>

<p align ="center">      
     <img src="media/readme/"  alt="" />    
</p>

<br/> 

###  8. About Page    <a name="aboutpage"></a>

The About Page again contains a brief synopsis of the site and contain information panels that display the main elements of the site. The accompanying links will take you to either the blog section or the recipe section of the site.
<br>

<p align ="center">      
     <img src="media/readme/"  alt="" />    
</p>

<br/> 

###  9. Recipes Page   <a name="recipespage"></a>

On the Recipes page there is a collection of Recipes ordered with the most recent Recipe at the top. The pagination allows for the Recipes to be distributed according to the number of recipes in the collection.

<br>

<p align ="center">      
     <img src="media/readme/"  alt="" />    
</p>

<br/> 

###  10. Recipes Search   <a name="recipessearch"></a>

The website user can use the search facility to find specific categories ie Breakfast, Lunch, Dinner, Dessert and Soup/Salad. You can also search according to a specific word in the title.If there are results, they will be displayed to the user and if not the user will be given the message that there are no results, they can either search again or they can return to the recipes page.

<br>

<p align ="center">      
     <img src="media/readme/"  alt="" />    
</p>

<br/> 

###  11. Add Recipe   <a name="addrecipe"></a>

As a logged in User you can add a Recipe to the site, when you press on the add a Recipe  link it will take you to the 'add Recipe page', when this form is completed you will be redirected to the Recipes page, where your new Recipe will be displayed.


<br>

<p align ="center">      
     <img src="media/readme/"  alt="" />    
</p>

<br/> 

###  12. Edit Recipe   <a name="editrecipe"></a>

As a logged in User you will be able to see the edit button below your submitted Recipe, when you use the edit button you will be redirected to the 'edit your Recipe page', where you can update your Recipe, when the form is completed you will be redirected to the Recipes page and your updated recipe will be displayed.

<br>

<p align ="center">      
     <img src="media/readme/"  alt="" />    
</p>

<br/> 

###  13. Delete Recipe   <a name="deleterecipe"></a>

As a logged in User you will be able to see the delete button below your submitted Recipe, when you use the delete button you will be redirected to the delete Recipe page, where you can delete your Recipe, when the form is completed you will be redirected to the Recipes page and your recipe will be deleted.

<br>

<p align ="center">      
     <img src="media/readme/"  alt="" />    
</p>

<br/> 

###  14. Recipe Detail Page   <a name="recipedetailpage"></a>

When you select a Recipe, you will be redirected to the Recipe detail page, this page will show the full content for that specific Recipe. If you are a logged in user you can add a comment. This comment will have to be approved by the admin before it will be displayed on the site. You can also like/unlike the Recipe. You can also see the Profile Picture and Bio for the Author of the Recipe.

<br>

<p align ="center">      
     <img src="media/readme/"  alt="" />    
</p>

<br/> 

###  15. Profile Page   <a name="profilepage"></a>

On the Profile Page, the User can have access to their own profile information. The profile will be automatically created when they register for the site. Initially the user will have a generic photo.


<br>

<p align ="center">      
     <img src="media/readme"  alt="" />    
</p>

###  16. Edit Profile  Page   <a name="editprofile"></a>

The logged in user can access the Edit Profile Page and can upload an image and add a Bio to their Profile. 
<br>

<p align ="center">      
     <img src="media/readme/"  alt="" />    
</p>



###  17. Signup Page   <a name="signuppage"></a>

On the Signup Page, a new user can sign up for the Wannabe Healthy website by filling out and submitting the form. On registering they will be assigned a Profile for the site.

<br>

<p align ="center">      
     <img src="media/readme"  alt="" />    
</p>

<br/>

###  18. Login Page   <a name="loginpage"></a>

A registered User can log in to the website by inputting the username and password and they will have full access to all the features of the site. 
<br>

<p align ="center">      
     <img src="media/readme"  alt="" />    
</p>

<br/> 

###  19. Logout Page   <a name="logoutpage"></a>

In the Logout Page, the User can confirm that they want to exit the website.

<br>

<p align ="center">      
     <img src="media/readme/"  alt="" />    
</p>

<br/>  



 #### [Return to Table of Contents](#toc)
----
 ## 6. Future Implementation  <a name="future"></a>

 <br>

 The site in it's present form offers a basic blog and recipe site, which is a good foundation but could be developed further to offer more options to the user. Within in the blog area, I would like to add some features in future iterations such as adding favourites and highlighting the blogs that have received the most likes. In regards to the recipes, there are a number of extra optionns I would like to introduce including vegetarian, and vegan options, the present recipes are not categorised in this way. I would like to introudce more interaction into the site, possibly using a forum where users can document their own experiences when adopting a vegetarian/vegan lifestyle. This would increase the social aspect of the site and would fully utilize the social media platforms fully. 
 
 The present profiles could be expanded to include more information, such as the user's own links so that users can also interact with each other outside of the site. At present there is no contact page and this would also be introduced, to encourage users to contact the web owner with messages, and it would be hoped their interaction would help the site owner to develop new ideas based on this suggestions. 

 The about page mentions relaxation as a factor, so I would like to add a section on the site dedicated to relaxation techniques and offering resources to the user in relation to stress relief and mindfulness.

 

<br>

 #### [Return to Table of Contents](#toc)
----
 ## 7. Tools and Technology  <a name="technology"></a>

### Language Used:

-   [Python 3.8.10](https://www.python.org/)
-   [HTML5](https://en.wikipedia.org/wiki/HTML5)    
-   [CSS3](https://en.wikipedia.org/wiki/CSS)
-   [JavaScript](https://www.javascript.com/)
-   [Django](https://www.python.org/)

### Technology Used:

-   [Am I Responsive](http://ami.responsivedesign.is/) was used to create the multi-device mock-up above.
-   [Bootstrap v5.2.3](https://getbootstrap.com/)
-   [Git:](https://git-scm.com/) used for version control, updated and commited changes (this in turn updated in Heroku). 
-   [GitHub:](https://github.com/) is the respository for all the git pushes.
-   [Gitpod](https://gitpod.io/) was the IDE Editor.
-   [Heroku:](https://heroku.com) used to deploy the application.
-   [Google Chrome Dev Tools](https://developer.chrome.com/docs/devtools/)
-   [Markdown](https://markdown-guide.readthedocs.io/en/latest/)
-   [Cloudinary](https://cloudinary.com/) - used for images for the site.
-   [Elephant SQL](https://www.elephantsql.com/) – deployed project on Heroku uses an Elephant SQL database. 
-   [Draw.io](https://drawio-app.com/) - used for the database diagram.
-   [Iconify.Design](https://iconify.design/) -Icons used for the site
-   [Favicon.io](https://favicon.io) for making the site favicon.
-   [tinyPNG](https://tinyjpg.com/) for image compression.
-   [Figma]()- used for making the wireframes for the site.

#### Django Packages

* [Gunicorn](https://gunicorn.org/) - As a server for Heroku
* [Cloudinary](https://cloudinary.com/) - Was used to host the static files and media
* [Dj_database_url](https://pypi.org/project/dj-database-url/) - To parse the database URL from the environment variables in Heroku
* [Psycopg2](https://pypi.org/project/psycopg2/) - As an adaptor for Python and PostgreSQL databases
* [Summernote](https://summernote.org/) - As a text editor for adding content
* [Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html) - For authentication, registration, account
   management
* [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) - To style the forms used in the site
 

 #### [Return to Table of Contents](#toc)
----

## 8. Testing  <a name="testing"></a>
<br>

Go to the [TESTING SECTION](TESTING.md)

 ## 9. Bugs and Issues  <a name="bugs"></a>

<br>

 ### Resolved <a name="resolved"></a>


 
 <br>

 ### Unresolved <a name="unresolved"></a>

 

<br>

 #### [Return to Table of Contents](#toc)
----


 ## 10. Deployment <a name="deployment"></a>

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

 - All Recipes and Recipe Images came from [Lidl Recipes Ireland](https://recipes.lidl.ie/)
 - All images for the site, including blog images come from [Pexel]()
 - The logo and Favicon were built with online tools
 - All Blog content was self produced
 
     

 I also used the following online resources:

- [Create a Simple Blog with Python and Django with Codemy](https://www.youtube.com/playlist?list=PLCC34OHNcOtr025c1kHSPrnP18YPB-NFi)
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

 
