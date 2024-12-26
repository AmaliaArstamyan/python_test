from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    rate = models.FloatField(default=0.0)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def update_rating(self, new_rating):
        self.rate = (self.rate * self.quantity + new_rating) / (self.quantity + 1)
        self.quantity += 1
        self.save()

# Lecture model
class Lecture(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lectures')
    title = models.CharField(max_length=255)
    duration = models.PositiveIntegerField(help_text="Duration in minutes")
    content = models.TextField()

    def __str__(self):
        return f"{self.title} ({self.course.title})"

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # In practice, use Django's User model or hashed passwords

    def __str__(self):
        return self.username

class Age(models.Model):
    age_range = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.age_range

