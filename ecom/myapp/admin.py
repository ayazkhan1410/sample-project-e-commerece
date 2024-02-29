from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(CustomUser)
class AdminCustomUser(admin.ModelAdmin):
    list_display = [
        "email",
        "phone",
        "address",
        "user_profile",
                    ]
    search_fields = ['email']
    list_per_page = 10

@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = [
        "category",
        "is_active",
    ]
    search_fields = ['category']
    list_per_page = 10
    
@admin.register(Company)
class AdminCompany(admin.ModelAdmin):
    list_display = [
        "company",
        "category",
        "is_active"
    ]
    search_fields = ['company']
    list_per_page = 10

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = [
        "category",
        "company",
        "product_name",
        "product_description",
        "orignal_price",
        "discount_percentage",
        "discounted_price",
        "warranty",
        "product_image",
        "is_stock",
        "is_active",
        "slug"
    ]
    search_fields = ['product_name']
    list_per_page = 10

@admin.register(Contact)
class AdminContact(admin.ModelAdmin):
    list_display = [
        "name",
        "email",
        "subject",
        "message"
    ]
    search_fields = ['email']
    list_per_page = 10

@admin.register(FeatureProductImage)
class AdminFeatureProductImage(admin.ModelAdmin):
    list_display = [
        "product",
        "image"
    ]
    search_fields = ['product']
    list_per_page = 10

@admin.register(ProductDescription)
class AdminProductDescription(admin.ModelAdmin):
    list_display = [
        "product",
        "feature",
        "product_description",
        "product_image"
    ]
    search_fields = ['product']
    list_per_page = 10
    
@admin.register(AdditionalInformation)
class AdminAdditionalInformation(admin.ModelAdmin):
    list_display = [
        "product",
        "feature",
        "product_description1",
        "product_description2",
        # "product_image"
    ]
    search_fields = ['product']
    list_per_page = 10

@admin.register(StayInTouch)
class AdminStayInTouch(admin.ModelAdmin):
    list_display = [
        'email'
    ]
    search_fields= ['email']
    list_per_page = 10

@admin.register(Cart)
class AdminCart(admin.ModelAdmin):
    list_display = [
        "user",
        "product",
        "quantity",
        "is_ordered",
        "total_price"
    ]
    search_fields = ["user"]
    list_per_page = 10

@admin.register(ShippingAddress)
class AdminShippingAddress(admin.ModelAdmin):
    list_display = [
        "first_name",
        "last_name",
        "company",
        "area_code",
        "primary_phone",
        "street_address",
        "zip_code"
    ]
    search_fields = ['first_name']
    list_per_page = 10