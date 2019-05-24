from django.db import models

class Person(models.Model):
    """Abstract class, represents a person."""
    
    name = models.CharField(max_length=100)
    email = models.EmailField()

    class Meta:
        abstract = True
        ordering = ['name']

    def __str__(self):
        """Representation of object, person name."""

        return self.name

    def save(self, *args, **kwargs):
        """Capitalize name attribute and then save."""
        
        self.name = " ".join([i.capitalize() for i in self.name.split()])
        super(Person, self).save(*args, **kwargs)