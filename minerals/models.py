from django.db import models


# class Group(models.Model):
#     name = models.CharField(max_length=255)


class Mineral(models.Model):
    name = models.CharField(max_length=255)
    image_filename = models.CharField(max_length=255)
    image_caption = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    formula = models.CharField(max_length=255, blank=True)
    strunz_classification = models.CharField(max_length=255, blank=True)
    color = models.CharField(max_length=50, blank=True)
    crystal_system = models.CharField(max_length=255, blank=True)
    unit_cell = models.CharField(max_length=255, blank=True)
    crystal_symmetry = models.CharField(max_length=255, blank=True)
    cleavage = models.CharField(max_length=255, blank=True)
    mohs_scale_hardness = models.CharField(max_length=255, blank=True)
    luster = models.CharField(max_length=255, blank=True)
    streak = models.CharField(max_length=255, blank=True)
    diaphaneity = models.CharField(max_length=255, blank=True)
    optical_properties = models.CharField(max_length=255, blank=True)
    refractive_index = models.CharField(max_length=255, blank=True)
    crystal_habit = models.CharField(max_length=255, blank=True)
    specific_gravity = models.CharField(max_length=255, blank=True)
    # group = models.ForeignKey(Group)
    group = models.CharField(max_length=255)

    def __str__(self):
        return self.name
