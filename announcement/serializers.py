from rest_framework import serializers
from .models import Announcement
#defauld
class AnnouncementCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ['Property_status', 'created_by']
class AnnouncementListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'
#AttachSale
class AttachSaleSerializer(serializers.ModelSerializer): 
    price = serializers.IntegerField()

    class Meta:
        model = Announcement
        fields = ['price']
    
    def update(self, instance, validated_data):
        if instance.Property_status == "Property for sale":
            instance.price = validated_data.get('price', instance.price)
        else:
            raise serializers.ValidationError('Your announcement is not announcement about sale, it is about rent, please leave this page !!!')
        instance.save()
        return instance
#AttachRent
class AttachRentSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Announcement
        fields = ['price', 'ForRent_status']
    
    def update(self, instance, validated_data):
        if instance.Property_status == "Property for rent":
            instance.price = validated_data.get('price', instance.price)
            instance.ForRent_status = validated_data.get('ForRent_status', instance.ForRent_status)
        else:
            raise serializers.ValidationError('Your announcement is not announcement about rent, it is about sale, please leave this page !!!')
        instance.save()
        return instance

#AttachPropertyType
class AttachPropertyTypeSerializer(serializers.ModelSerializer):
    Price = serializers.IntegerField(allow_null=False, read_only=True)
    class Meta:
        model = Announcement
        fields = ['PropertyType_status', 'Price']
    
    def update(self, instance, validated_data):
        Price = instance.price
        
        if Price:
            instance.PropertyType_status = validated_data.get('PropertyType_status', instance.PropertyType_status)
        else:
            raise serializers.ValidationError('You need to set price, before seting property type !!')

        instance.save()
        return instance
#AttachPropertyTType_status
class AttachPropertyResidentialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = [ 'PropertyType_status','PropertyTType_status', 'area', 'Bedrooms', 'Bathrooms', 'Featuers']

    def update(self, instance, validated_data):
        instance.PropertyType_status = validated_data.get('PropertyType_status', instance.PropertyType_status)
        instance.PropertyTType_status = validated_data.get('PropertyTType_status', instance.PropertyTType_status)
        instance.area = validated_data.get('area', instance.area)
        instance.Bedrooms = validated_data.get('Bedrooms', instance.Bedrooms)
        instance.Bathrooms = validated_data.get('Bathrooms', instance.Bathrooms)
        instance.Featuers = validated_data.get('Featuers', instance.Featuers)
        if instance.PropertyType_status == 'Residential':
            instance.save()
            return instance
        else:
            raise serializers.ValidationError('Your property type is not Residential, please check your property type !!!')
        
class AttachPropertyRetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ['PropertyType_status', 'area', 'Bedrooms', 'Bathrooms', 'Featuers']

    def update(self, instance, validated_data):
        instance.PropertyType_status = validated_data.get('PropertyType_status', instance.PropertyType_status)
        instance.area = validated_data.get('area', instance.area)
        instance.Bedrooms = validated_data.get('Bedrooms', instance.Bedrooms)
        instance.Bathrooms = validated_data.get('Bathrooms', instance.Bathrooms)
        instance.Featuers = validated_data.get('Featuers', instance.Featuers)
        if instance.PropertyType_status == 'Retail':
            instance.save()
            return instance
        else:
            raise serializers.ValidationError('Your property type is not Retail, please check your property type !!!')

class AttachPropertyCommercialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ['PropertyType_status', 'area', 'Bedrooms', 'Bathrooms', 'Featuers']

        def update(self, instance, validated_data):
            instance.PropertyType_status = validated_data('PropertyType_status', instance.PropertyType_status)
            instance.area = validated_data.get('area', instance.area)
            instance.Bedrooms = validated_data.get('Bedrooms', instance.Bedrooms)
            instance.Bathrooms = validated_data.get('Bathrooms', instance.Bathrooms)
            instance.Featuers = validated_data.get('Featuers', instance.Featuers)
            if instance.PropertyType_status == 'Commercial':
                instance.save()
                return instance
            else:
                raise serializers.ValidationError('Your property type is not Commercial, please check your property type !!!')

class AttachPropertyLandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ['PropertyType_status', 'area']

        def update(self, instance, validated_data):
            instance.PropertyType_status = validated_data.get('PropertyType_status', instance.PropertyType_status)
            instance.area = validated_data.get('area', instance.area)
            if instance.PropertyType_status == 'Land':
                instance.save()
                return instance
            else:
                raise serializers.ValidationError('Your property type is not land, please check your property type !!!')

class AttachAnnouncementdescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ['Title', 'Description']
    
    def update(self, instance, validated_data):
        instance.Title = validated_data.get('Title', instance.Title)
        instance.Description = validated_data.get('Description', instance.Description)
        if instance.PropertyType_status == 'Residential' or instance.PropertyType_status == 'Retail' or instance.PropertyType_status == 'Commercial' or instance.PropertyType_status == 'Land':
            instance.save()
            return instance
        else:
            raise serializers.ValidationError("You can't complete this stape, becuse you haven't completed another one, please go back !!!")

class AttachLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ['Location']
    
    def update(self, instance, validated_data):
        instance.Location = validated_data.get('Location', instance.Location)
        if instance.PropertyType_status == 'Residential' or instance.PropertyType_status == 'Retail' or instance.PropertyType_status == 'Commercial' or instance.PropertyType_status == 'Land':
            instance.save()
            return instance
        else:
            raise serializers.ValidationError("You can't complete this stape, becuse you haven't completed another one, please go back !!!")
    
class AttachImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ['AnnouncementCoverImage', 'ElseImage', 'OtherDoc']
    
    def update(self,instance,validated_data):
        instance.AnnouncementCoverImage = validated_data.get('AnnouncementCoverImage', instance.AnnouncementCoverImage)
        instance.ElseImage = validated_data.get('ElseImage', instance.ElseImage)
        instance.OtherDoc = validated_data.get('OtherDoc', instance.OtherDoc)
        if instance.PropertyType_status == 'Residential' or instance.PropertyType_status == 'Retail' or instance.PropertyType_status == 'Commercial' or instance.PropertyType_status == 'Land':
            instance.save()
            return instance
        else:
            raise serializers.ValidationError("You can't complete this stape, becuse you haven't completed another one, please go back !!!")