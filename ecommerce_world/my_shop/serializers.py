from rest_framework import serializers
from my_shop.models import ProductsDetails, ProductCartDetails, ProductBuyDetails


class UsersProductSerializers(serializers.ModelSerializer):

    class Meta:
        model = ProductsDetails
        fields = ('ProductId', 'ProductName', 'Description', 'Price', 'Quantity', 'Category', 'CompanyName', 'ProductImage')


class ProductSerializers(serializers.ModelSerializer):

    ProductImage = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = ProductsDetails
        fields = ('ProductId', 'UserId', 'ProductName', 'Description', 'Price', 'Quantity', 'Category', 'CompanyName', 'ProductImage', 'AddedTime', 'ModifiedTime')


class ProductSerializersPut(serializers.ModelSerializer):

    class Meta:
        model = ProductsDetails
        fields = ('ProductId', 'UserId', 'ProductName', 'Description', 'Price', 'Quantity', 'Category', 'CompanyName', 'AddedTime', 'ModifiedTime')


class ProductCartSerializers(serializers.ModelSerializer):

    class Meta:
        model = ProductCartDetails
        fields = ('CartId', 'UserId', 'Email', 'PhoneNumber', 'ProductId', 'ProductName', 'Description', 'TotalPrice', 'TotalQuantity', 'Category', 'CompanyName', 'CartProductAddedTime', 'CartProductModifiedTime')


class ProductBuySerializers(serializers.ModelSerializer):

    class Meta:
        model = ProductBuyDetails
        fields = ('TrackingId', 'UserId', 'ProductIds', 'TotalPrice', 'TotalQuantity', 'Email', 'PhoneNumber', 'Address', 'State', 'District', 'Pincode', 'ProductTrackingStatus', 'OrderConfirm', 'Otp', 'BuyProductAddedTime', 'BuyProductModifiedTime')


class TrackAllOrderDetailsSerializers(serializers.ModelSerializer):

    class Meta:
        model = ProductBuyDetails
        fields = ('TrackingId', 'ProductIds', 'TotalPrice', 'TotalQuantity', 'Email', 'PhoneNumber', 'Address', 'State', 'District', 'Pincode', 'ProductTrackingStatus', 'OrderConfirm', 'BuyProductAddedTime')


class TrackOrderSerializers(serializers.ModelSerializer):

    class Meta:
        model = ProductBuyDetails
        fields = ('TrackingId', 'ProductIds', 'TotalPrice', 'TotalQuantity', 'Email', 'PhoneNumber', 'Address', 'State', 'District', 'Pincode', 'ProductTrackingStatus', 'OrderConfirm', 'BuyProductAddedTime')


class OrderStatusUpdateSerializers(serializers.ModelSerializer):

    class Meta:
        model = ProductBuyDetails
        fields = ('TrackingId', 'ProductIds', 'TotalPrice', 'TotalQuantity', 'Email', 'PhoneNumber', 'Address', 'State', 'District', 'Pincode', 'ProductTrackingStatus', 'OrderConfirm', 'Otp', 'BuyProductAddedTime', 'BuyProductModifiedTime')


