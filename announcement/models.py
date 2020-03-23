from django.db import models
from users.models import User
# Create your models here.

class Announcement(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    ForSale = "Property for sale"
    ForRent = "Property for rent"
    Property_choices = [(ForSale, "Property for sale"), (ForRent, "Property for rent")]
    Property_status = models.CharField(verbose_name='Property type',max_length=30,null=False, blank=False, choices=Property_choices) 
    
    price = models.IntegerField(blank=True, null=True, verbose_name='Price', help_text='Set Price')
    
    
    
    Yes = "Yes"
    No = "No"
    OtherPeriods_choices = [(Yes, "Yes"), (No, "No")]
    OtherPeriods_status = models.CharField(verbose_name='Is available ? ', help_text="Property is also available for other rental periods (price is on request via chat or call)", max_length=30,null=True, blank=True, choices=OtherPeriods_choices)
    
    #Sale{
    Residential = 'Residential'
    Retail = 'Retail'
    Commercial = 'Commercial'
    Land = 'Land'
    PropertyType_choices = [(Residential , 'Residential'), (Retail, 'Retail'), (Commercial, 'Commercial'), (Land, 'Land')]
    PropertyType_status = models.CharField(verbose_name='Property type',max_length=30,null=True, blank=True, choices=PropertyType_choices )
    
    #Residental
    Apartment = 'Apartment'
    Villa = 'Villa'
    Duplex = 'Duplex'
    RestHouses = 'RestHouses'
    PropertyTType_choices = [(Apartment, 'Apartment'), (Villa, 'Villa'), (Duplex, 'Duplex'), (RestHouses, 'RestHouses')]
    PropertyTType_status = models.CharField(verbose_name='Property detail type',max_length=30,null=True, blank=True, choices=PropertyTType_choices )

    area = models.IntegerField(verbose_name='area', help_text='Set area', null=True, blank=True)
    Bedrooms = models.IntegerField(verbose_name='Bedrooms', null=True, blank=True)
    Bathrooms = models.IntegerField(verbose_name='Bathrooms', null=True, blank=True)
    Featuers = models.TextField(verbose_name='Mention features', max_length=1000, null=True, blank=True, help_text='Parking area, Shared pool, Security features, Pets allowed, Furnished, Private gym, Elevator, Air conditioning, Partially furnished, Shared gym, Garden, Private pool, Sports court')

    Title = models.CharField(verbose_name="Title", max_length=30,null=True, blank=True)
    Description = models.TextField(verbose_name="Description", max_length=1000, null=True, blank=True) 
    Location = models.CharField(verbose_name='Location', max_length=200, null=True, blank=True)

    AnnouncementCoverImage = models.FileField(null=True,blank=True,verbose_name='Announcement cover image', help_text='Please upload a cover image for your announcement to make your property more attractive for customers.')
    ElseImage = models.FileField(null=True,blank=True,verbose_name='OtherImage', help_text='Please upload other medias for your announcement to make your property more attractive for customers')
    OtherDoc = models.FileField(null=True,blank=True,verbose_name='Other documentations', help_text ='Floor plans, property license and any other information concerning to your property')

    #Rent
    Daily = "Daily"
    Weekly = "Weekly"
    Monthly = "Monthly"
    Yearly = "Yearly"
    ForRent_choices = [(Daily, "Daily"), (Weekly, "Weekly"), (Monthly, "Monthly"), (Yearly, "Yearly")]
    ForRent_status = models.CharField(verbose_name='Select rental frequency',max_length=30,null=True, blank=True, choices=ForRent_choices)