from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.text import slugify


STATUS = ((0, "Draft"), (1, "Published"))

recipe_categories = (
    ("Breakfast", "Breakfast"),
    ("Lunch", "Lunch"),
    ("Dinner", "Dinner"),
    ("Dessert", "Dessert"),
    ("Soup/Salad", "Soup/Salad")
)


difficulty_level = (
    ("Easy", 'Easy'),
    ("Medium", 'Medium'),
    ("Hard", 'Hard')
)    


class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    category = models.TextField(choices=recipe_categories)
    description = models.TextField(max_length=200, default="recipe")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipe_posts")
    created_on = models.DateTimeField(auto_now_add=True)
    featured_image = CloudinaryField('image', default='placeholder1')
    difficulty = models.TextField(choices=difficulty_level, default="easy")
    cooking_time = models.CharField(max_length=50, default=0)
    ingredients = models.TextField()
    method = models.TextField()
    likes = models.ManyToManyField(
        User, related_name='recipe_likes', blank=True)    
    status = models.IntegerField(choices=STATUS, default=0)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Recipe, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()
    
    def number_of_comments(self):
        return self.comments.count()
    
class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

    
    
