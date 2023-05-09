from django.db import models

class New_type(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Area(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Day_new(models.Model):
    title = models.CharField(max_length=500)
    comment = models.CharField(max_length=800)
    description = models.CharField(max_length=10000)
    img = models.ImageField(upload_to='images/')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Day_new_piece(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=10000, blank=True, null=True)
    img = models.ImageField(upload_to='images/', blank=True, null=True)
    day_new = models.ForeignKey(Day_new, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Actual(models.Model):
    title = models.CharField(max_length=500)
    comment = models.CharField(max_length=800)
    description = models.CharField(max_length=10000)
    img = models.ImageField(upload_to='images/')
    created = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Actual_piece(models.Model):
    img = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=10000, blank=True, null=True)
    actual = models.ForeignKey(Actual, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Intervyu(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=10000)
    img = models.ImageField(upload_to='images/')
    created = models.DateTimeField(auto_now_add=True)
    youtube_link = models.CharField(max_length=1000)
    talked = models.CharField(max_length=100)
    painter = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class Intervyu_piece(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=10000)
    img = models.ImageField(upload_to='images/')
    intervyu = models.ForeignKey(Intervyu, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Article(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=10000)
    img = models.ImageField(upload_to='images/')
    created = models.DateTimeField(auto_now_add=True)
    jurnalist = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class Article_piece(models.Model):
    img = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=10000)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

class Bisnes_new(models.Model):
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=10000)
    img = models.ImageField(upload_to='images/')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Bisnes_new_piece(models.Model):
    description = models.CharField(max_length=10000)
    img = models.ImageField(upload_to='images/')
    bisnes_new = models.ForeignKey(Bisnes_new, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
    
class Video_new(models.Model):
    title = models.CharField(max_length=500)
    comment = models.CharField(max_length=800)
    created = models.DateTimeField(auto_now_add=True)
    youtube_link = models.CharField(max_length=1000)
    new_type = models.ForeignKey(New_type, on_delete=models.CASCADE)
    jurnalist = models.CharField(max_length=100)
    interlocutor = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
class Video_new_piece(models.Model):
    img = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=10000)
    video_new = models.ForeignKey(Video_new, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Area_new(models.Model):
    title = models.CharField(max_length=500)
    comment = models.CharField(max_length=800)
    description = models.CharField(max_length=10000)
    img = models.ImageField(upload_to='images/')
    created = models.DateTimeField(auto_now_add=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Area_new_piece(models.Model):
    description = models.CharField(max_length=10000)
    img = models.ImageField(upload_to='images/')
    area_new = models.ForeignKey(Area_new, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
    
class Area_new_list(models.Model):
    title = models.CharField(max_length=500)
    comment = models.CharField(max_length=800)
    description = models.CharField(max_length=10000)
    img = models.ImageField(upload_to='images/')
    created = models.DateTimeField(auto_now_add=True)
    area = models.ForeignKey(Area, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Area_new_list_piece(models.Model):
    description = models.CharField(max_length=10000)
    img = models.ImageField(upload_to='images/')
    area_new_list = models.ForeignKey(Area_new_list, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
