from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from .models import Customer
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_customer_profile(sender, instance, created, **kwargs):
    if created:
        # Create a new Customer profile for the newly created User
        customer = Customer.objects.create(user=instance, name=instance.username)
        # Add the new user to the 'customer' group
        customer_group, _ = Group.objects.get_or_create(name='customer')
        instance.groups.add(customer_group)
        print(f"Customer profile created for user: {instance.username} and added to 'customer' group.")
        
        
