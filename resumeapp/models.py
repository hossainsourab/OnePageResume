from django.db import models
import time


# Create your models here.

class ContactInformation(models.Model):
    name = models.CharField(max_length=200)
    profile_picture = models.ImageField(upload_to='profile picture')
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class PreviousEmployment(models.Model):
    company_name = models.CharField(max_length=250)
    designation = models.CharField(max_length=250)
    start_date = models.DateField()
    completion_date = models.DateField()
    job_description = models.TextField()
    is_current = models.BooleanField(default=False)

    def job_date_range(self):
        return ''.join(['(', self.formatted_start_date(),
                        '-', self.formatted_end_date(), ')'])

    def full_start_date(self):
        return self.start_date.strftime("%Y-%m-%d")

    def full_end_date(self):
        if (self.is_current == True):
            return time.strftime("%Y-%m-%d", time.localtime())
        else:
            return self.completion_date.strftime("%Y-%m-%d")

    def formatted_start_date(self):
        return self.start_date.strftime("%b %Y")

    def formatted_end_date(self):
        if (self.is_current == True):
            return "Current"
        else:
            return self.completion_date.strftime("%b %Y")

    def __str__(self):
        return self.company_name

    def __unicode__(self):
        return ' '.join([self.company_name, self.job_date_range()])


# class ProfessionalSkills(models.Model):
#     description = models.TextField()

class Education(models.Model):
    name_university = models.CharField(max_length=250)
    degree = models.CharField(max_length=250)
    start_date = models.DateField()
    completion_date = models.DateField()
    description = models.TextField()
    is_current = models.BooleanField(default=False)

    def edu_date_range(self):
        return ''.join(['(', self.formatted_start_date(),
                        '-', self.formatted_end_date(), ')'])

    def full_start_date(self):
        return self.start_date.strftime("%Y-%m-%d")

    def full_end_date(self):
        if (self.is_current == True):
            return time.strftime("%Y-%m-%d", time.localtime())
        else:
            return self.completion_date.strftime("%Y-%m-%d")

    def formatted_start_date(self):
        return self.start_date.strftime("%b %Y")

    def formatted_end_date(self):
        if (self.is_current == True):
            return "Current"
        else:
            return self.completion_date.strftime("%b %Y")

    def __str__(self):
        return self.name_university

    def __unicode__(self):
        return ' '.join([self.name_university, self.edu_date_range()])


class ProfessionalSkills(models.Model):
    description = models.TextField(
        'Description',
    )

    def __str__(self):
        return f"Id: {self.id}"

    def __unicode__(self):
        return f"Id: {self.id}"


class SoftwareData(models.Model):
    skills = models.ForeignKey(
        ProfessionalSkills,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='softwardata'
    )

    software = models.CharField(max_length=200)

    def __str__(self, *args, **kwargs):
        return f"Id: {self.id} software: {self.software}"

    def __unicode__(self, *args, **kwargs):
        return f"Id: {self.id} software: {self.software}"


class LanguagesData(models.Model):
    skills = models.ForeignKey(
        ProfessionalSkills,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='languagesdata'
    )

    languages = models.CharField(max_length=200)

    def __str__(self, *args, **kwargs):
        return f"Id: {self.id} languages: {self.languages}"

    def __unicode__(self, *args, **kwargs):
        return f"Id: {self.id} languages: {self.languages}"
