
Back to the [README](README.md)

Testing has taken place continuously throughout the development of the project. When faults were detected they were fixed on an ongoing basis. These were fixed locally and commited to github on an ongoing basis. Faults fixed and outstanding can be found in the README.md

# Table of Contents <a name="toc"></a>
1. [Cross Browser Testing](#browsertesting)
2. [Responsive Testing](#responsivetesting)
3. [Validator Testing](#validatortesting)
     1. [W3C Validator](#w3c)
     2. [CSS Validator](#css)
     3. [Python](#python)
     4. [Lighthouse](#lighthouse)
     5. [Contrast Checker](#contrastchecker)
     6. [WAVE](#wave)
4. [Manual Testing](#manual)
5. [User Story Testing](#userstorytesting)  

#### [Return to README.md](README.md)
----


## Cross Browser Testing<a name="browsertesting"></a>

  The site was tested in Google Chrome, Microsoft Edge, Mozilla Firefox and Brave Browser on the Desktop.
  The site was tested on a Lenovo Laptop, and a Xiomai Redmie. 

<br/>


#### [Return to Table of Contents](#toc)

----
## Responsive Testing<a name="responsivetesting"></a>

   I regularly tested the responsiveness of the site using Google Chrome Developer tools, information on this can be found [here](https://developer.chrome.com/docs/devtools/). I also used Window Resizer and a Responsive Design Tester Application available in the Google Chrome Store. The devices I tested for are in the image below. 
     
#### [Return to Table of Contents](#toc)

----
## Validator Testing<a name="validatortesting"></a>

1. W3C Validator <a name="w3c"></a>

Using [https://validator.w3.org/](https://validator.w3.org/)   
There are more issues in the Bug section in the [README.md](README.md). The results of the HTML validation can be seen below:


<br/>

<p align ="center">      
     <img src="assets/images/readme/htmlcheck.jpg"  alt="HTML Validation results"/>   
</p>
<br/>  
  
2. Jigsaw CSS Validator   <a name="css"></a>
 

Using [https://jigsaw.w3.org/css-validator/](https://jigsaw.w3.org/css-validator/) 
The result can be seen below:

<br/>
<p align ="center">      
     <img src="assets/images/readme/"  alt="CSS Validation results"/>   
</p>
<br/>

3. Python Validation   <a name="python"></a>
  Python testing was done without the use of Pep8 as the site was down, instead an extension was added which highlighted errors and showed them in the problems panel within gitpod. Most errors related to long lines, but there were some syntax errors.


4. Lighthouse Testing


<p align ="center">      
     <img src="assets/images/readme/images/"  alt="lighouse testing specs" />    
</p>
<br/> 

5. Contrast Checker  <a name="contrastchecker"></a>
  
  Using [https://color.a11y.com/](https://color.a11y.com/)  See images Below.

<br/>
  <p align ="center">      
     <img src="assets/images/readme/contrast.jpg"  alt="contrast results"/>   
  </p>
  
  

6. Wave (Web Accesability Evaluation tool)   <a name="wave"></a>
  
  Using [WAVE](https://chrome.google.com/webstore/detail/wave-evaluation-tool/jbbplnpkjmmeebjpijfedlgcdilocofh), this is a web accesability tool developed by WebAIM.org. It provides visual feedback about the accessibility of your web content, it highlights any errors and gives you possible suggestions for improvements. 

  <br/>
  <p align ="center">      
     <img src="assets/images/readme/wave.jpg"  alt="wave test result"/>   
  </p>
  
 #### [Return to Table of Contents](#toc)
----

### 4. Manual Testing   <a name="manual"></a>


<h3 align ="center">      
    Feature being Tested and Result   
</h3>


### On the Site:
- Start Screen displays when Heroku link is used.   :heavy_check_mark:
- The index page displays correctly with the functionality expected for a user that is not logged in. :heavy_check_mark:
- The navbar displays correctly for a user that is not logged in, the account link in navbar is present.  :heavy_check_mark:
- The sign up link opens up the sign up form and allows a User to register for the site.  :heavy_check_mark:
- The Login Link opens up the login form and allows the User to login into the site.  :heavy_check_mark:
- The navbar displays the Profile link when the user has logged in.  :heavy_check_mark:
- The navbar displays the profile image of the logged in user in the navbar.  :heavy_check_mark:
- The navbar displays the Logout link when the user has logged in.  :heavy_check_mark:
- The add blog button is displayed when the User logs in.  :heavy_check_mark:
- The home page displays the collection of blogs (6 blogs per page) and pagination is working to display those in excess of that number.  :heavy_check_mark:
- The logged in user can see the edit and delete buttons for any blog they have submitted.  :heavy_check_mark:
- The Title and excerpt of each blog can be used as a link to the post_detail page of each blog, when used the User is redirected to this page successfully.  :heavy_check_mark:
- The Post_detail page displays correctly.  :heavy_check_mark:
- When the logged in user click the like button, they receive a message that they have liked a blog, if they press again, they receive a message that they have unliked the blog.  :heavy_check_mark:
- The comment form displays for a logged in user, and if they submit a comment, they receive a message that their comment is awaiting approval of the admin. When this is approved it is displayed within the comment section.  :heavy_check_mark:
- The like icon shows the number of likes the blog has received.  :heavy_check_mark:
- The comment icon shows the number of comments that the blog has received. :heavy_check_mark:
- The profile image and bio of the blog author displays correctly in the post_detail page.  :heavy_check_mark:
- In the home page, within each blog(that user has submitted) the edit button when used will open up the edit_post Form, when this form is submitted, any changes are updated within the blog post, and the user is redirected to the home page.  :heavy_check_mark:
- In the home page, within each blog(that user has submitted) the delete button when used will open up the delete_post Form, the title of the post is displayed and the user is asked whether they are sure they want to delete the post,if this is confirmed the blog post will be deleted and the user will be redirected to the home page.   :heavy_check_mark:
- The about page displays correctly.  :heavy_check_mark:
- The add recipe button displays correctly for the logged in user.  :heavy_check_mark:
- The recipes page displays the collection of recipes (6 recipes per page) and pagination is working to display those in excess of that number.  :heavy_check_mark:
- The logged in user can see the edit and delete buttons for any recipe they have submitted.  :heavy_check_mark:
- The 'see details' button directs the user to the recipe-detail page for each recipe.  :heavy_check_mark:
- The recipe_detail page displays correctly.  :heavy_check_mark:
- When the logged in user click the like button, they receive a message that they have liked a recipe, if they press again, they receive a message that they have unliked the recipe.  :heavy_check_mark:
- The comment form displays for a logged in user, and if they submit a comment, they receive a message that their comment is awaiting approval of the admin. When this is approved it is displayed within the comment section.  :heavy_check_mark:
- The like icon shows the number of likes the recipe has received.  :heavy_check_mark:
- The comment icon shows the number of comments that the recipe has received. :heavy_check_mark:
- The profile image and bio of the recipe author displays correctly in the recipe_detail page.  :heavy_check_mark:
- In the recipes page, within each recipe(that user has submitted) the edit button when used will open up the edit_recipe Form, when this form is submitted, any changes are updated within the recipe, and the user is redirected to the recipes page.  :heavy_check_mark:
- In the recipes page, within each recipe(that user has submitted) the delete button when used will open up the delete_recipe Form, the title of the recipe is displayed and the user is asked whether they are sure they want to delete the recipe,if this is confirmed the recipe will be deleted and the user will be redirected to the recipes page.  :heavy_check_mark:
- When the profile link in navbar is chosen the profile page displays correctly.  :heavy_check_mark:
- A Profile is created automatically when a User registers for the site.  :heavy_check_mark:
- The username of the new user is displayed in the profile page.
- A generic image is automatically generated until the user uploads an image of their own.  This can be displayed in the navbar profile image and blog/recipe detail pages, if user does not upload a new image of their own.  :heavy_check_mark:
- When user uses edit button on profile page, the edit_profile form is displayed and the user can add bio details and an image. THe user is then redirected back to the profile page, to see these changes. :heavy_check_mark:
- When the user uses the logout link the logout form is displayed and the user can logout, The user is asked whether they want to leave the site.  :heavy_check_mark:

### Admin Panel:
- Managed to create, update and delete data in all models, during the entire project, and all seems to be working as expected when logged in as the admin.  :heavy_check_mark:
- When a User comments on a post, Admin needs to approve before it is displayed on the site, this is working as expected, when logged in as the admin.  :heavy_check_mark:
- All required fields need to be filled in when posting a new recipe and blog, and the user is advised on these requirements when filling these forms.  :heavy_check_mark:  


  
#### [Return to Table of Contents](#toc)
----

<br>

### 5. User Story Testing<a name="userstorytesting"></a>

 <br/>

#### As a Website User I can....

1. Navigate around the site and easily view the type of content available.

**The Navbar is available on each page of the wbsite, it contains links to all areas in the site. There is introductory text on the home page, which clearly indicates the theme of the site, and the type of information that will be available within the site.**

2. View a collection of Blogs in the blog Section.

**The Home page contains a collection of blogs and they are classified in a selection of categories.**

3. Search the blog section for particular categories or by title content.

**Above the blogs, there is a search bar where the User can search by category type, or a word within a blog title.**

4. Click on a blog item and view more indepth content of the selected blog.

**When a User clicks on a blog, they are taken to the post_detail page, where they can see the full details of the Blog on a seperate page.**

5. Register for an account to avail of full features of the site.

**When a User registers on the site, they have access to full functionality within the site.  They are able to add,edit or delete a blog or recipe. They can like/unlike a blog/recipe, They can leave a comment for a blog/recipe. They will have their own Profile on the site and they can update the details within this profile.**

6. View the number of likes on a blog.

**Below individual blog posts there is a heart icon and a number which relates to the number of like that the blog has received. This can be seen on the home and the post_detail pages.**

7. View comments left for different blogs in the collection.

**The general User can see comments that have been added to any blog, when not logged in.** 

1. View a collection of Recipes in the Recipe Page.

**The Recipes page contains a collection of Recipes and they are classified in a number of categories including Breakfast, Lunch, Dinner, Desserts and Soups/Salad.**

9. Search through recipes for particular categories or by name in title.

**Above the recipes, there is a search bar where the User can search by category type, or a word within a Recipe title.**

10. Click on a Recipe to see full details of that recipe.

**When a User clicks on the 'see detail' button, they are taken to the recipe_detail page, where they can see the full recipe on a seperate page.**

11. View the number of likes on a Recipe.

**Below individual recipe posts there is a heart icon and a number which relates to the number of like that the recipehas received. This can be seen on the home and the recipe_detail pages.**

12.  View any comments left on a Recipe. 

**The general User can see comments that have been added to any recipe, when not logged in.** 


<br>

#### As a logged in User I can…...  

1. I can add a new post or a recipe.

**When logged in, a User can see the button for adding a blog, this is only visible to the logged in user. The button to add a recipe is also only visible to a logged in User. The User can either publish or draft a blog/recipe, if drafted, the addition will not be visible, until the status has been changed to published.**

2. I can like/unlike a blog or recipe on the site.

**As a logged in User you can like or unlike a blog or recipe and this will added to the number of like that the blog/recipe has.**

1. I can leave comments on particular blogs and recipes.

**As a logged in User you will be able to see the comment submission form under the blog/recipe in the post_detail page and the recipe_detail page. You can submit a comment, but it will not be added until the admin approves it, this is to ensure any comment is suitable for inclusion.**

4. I can update my Profile for the site by adding a Bio and Image.

**As a logged in User, the profile link is available within the navbar and their profile image will be displayed to the right of the navbar. They will be able to access the profile page and review the profile details. They will also be able to access the edit_profile page and be able to update their bio details and upload an image.**

5. I can edit a Blog or Recipe that I have submitted to the site.

**As a logged in User, they have access to an edit button below their blog in the blog sections, this allows them to update the details of the blog in the edit_post page. When this form is submitted they will be redirected to the home page and the changes will be applied. There is also an edit button below their submitted recipes, and this will allow them to access the edit_recipe page. When this form is submitted they will be redirected to the recipes page and the changes will be applied.**

6. I can delete a Recipe or Blog that I have submitted to the site.

**As a logged in User, they have access to an delete button below their blog in the blog section, this allows them to delete their blog in the delete_post page. When this form is submitted, their blog will be deleted.. There is also an delete button below their submitted recipes, and this will allow them to delete their recipe. When this form is submitted they will be redirected to the recipes page and the recipe will be deleted.**
<br>

#### As a Superuser/Admin I want to...

1. Create and publish a new blog or recipe.

**As an Admin you can publish a new blog or recipe for the site, initially before building the frontend this was how blogs were added to the site, but now any logged in user can add blogs/recipes.**

2. Create draft recipes and blog posts that can be finalised later.

**The Admin can either publish or draft a blog/recipe, if drafted, the addition will not be visible on the site, until the status has been changed to published.**

3. Create a new user, recipes, blogs and categories.
4. Delete user, blogs, recipes, categories and comments.
5. Can approve user's comments.



<br>

#### [Return to Table of Contents](#toc)
#### [Return to README.md](README.md)

----

