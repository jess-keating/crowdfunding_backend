from rest_framework import serializers
from django.apps import apps


class FundraiserSerializer(serializers.ModelSerializer):
    """
    Base serializer for Fundraiser model
    Handles basic serialization of fundraiser data
    
    Fields:
        All model fields
        owner: Read-only field linking to user ID
    """
    owner = serializers.ReadOnlyField(source="owner.id")

    class Meta:
        model = apps.get_model("fundraisers.Fundraiser")
        fields = "__all__"


class PledgeSerializer(serializers.ModelSerializer):
    """
    Base serializer for Pledge model
    Handles basic serialization of pledge data
    
    Fields:
        All model fields
        supporter: Read-only field linking to user ID
    """
    supporter = serializers.ReadOnlyField(source="supporter.id")

    class Meta:
        model = apps.get_model("fundraisers.Pledge")
        fields = ["__all__", "is_active"]


class FundraiserDetailSerializer(FundraiserSerializer):
    """
    Detailed serializer for Fundraiser model
    Extends FundraiserSerializer with additional pledge data
    
    Additional Fields:
        pledges: Nested serializer showing all pledges for fundraiser
    """
    pledges = PledgeSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        """
        Updates Fundraiser instance with validated data
        
        Args:
            instance: Existing Fundraiser object
            validated_data: Dict of new field values
            
        Returns:
            Updated Fundraiser instance
            
        Updates:
            - title
            - description
            - goal
            - image
            - is_open
            - date_created
            - owner
        """
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.goal = validated_data.get("goal", instance.goal)
        instance.image = validated_data.get("image", instance.image)
        instance.is_open = validated_data.get("is_open", instance.is_open)
        instance.is_active = validated_data.get("is_active", instance.is_active)
        instance.date_created = validated_data.get("date_created", instance.date_created)
        instance.owner = validated_data.get("owner", instance.owner)
        instance.save()
        return instance


class PledgeDetailSerializer(PledgeSerializer):
    """
    Detailed serializer for Pledge model
    Extends PledgeSerializer with additional pledge details
    
    Additional Fields:
        pledges: Nested serializer for related pledges (if any)
    """
    pledges = PledgeSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        """
        Updates Pledge instance with validated data
        
        Args:
            instance: Existing Pledge object
            validated_data: Dict of new field values
            
        Returns:
            Updated Pledge instance
            
        Updates:
            - amount
            - comment
            - anonymous
            Note: fundraiser and supporter updates are commented out for security
        """
        instance.amount = validated_data.get("amount", instance.amount)
        instance.comment = validated_data.get("comment", instance.comment)
        instance.anonymous = validated_data.get("anonymous", instance.anonymous)
        instance.save()
        return instance
