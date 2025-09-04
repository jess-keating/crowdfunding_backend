from django.db import models
from django.contrib.auth import get_user_model


class Fundraiser(models.Model):
    """
    Model representing a fundraising campaign
    
    Fields:
        title: Name of the fundraising campaign
        description: Detailed description of the campaign
        goal: Target amount to raise (integer)
        image: URL to campaign image
        is_open: Boolean flag indicating if campaign is active
        date_created: Timestamp of creation (auto-set)
        owner: Foreign key to User model (campaign creator)
    
    Relationships:
        - One-to-Many with Pledge model (via related_name='pledges')
        - Many-to-One with User model (via owner field)
    """
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        get_user_model(),
        related_name='owned_fundraisers',
        on_delete=models.CASCADE
    )


class Pledge(models.Model):
    """
    Model representing a pledge to a fundraising campaign
    
    Fields:
        amount: Pledge amount (integer)
        comment: Optional comment from supporter
        anonymous: Boolean flag for anonymous pledges
        fundraiser: Foreign key to associated campaign
        supporter: Foreign key to User model (pledge creator)
    
    Relationships:
        - Many-to-One with Fundraiser model (via fundraiser field)
        - Many-to-One with User model (via supporter field)
    """
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    fundraiser = models.ForeignKey(
        'Fundraiser',
        related_name='pledges',
        on_delete=models.CASCADE
    )
    supporter = models.ForeignKey(
        get_user_model(),
        related_name='pledges',
        on_delete=models.CASCADE
    )

