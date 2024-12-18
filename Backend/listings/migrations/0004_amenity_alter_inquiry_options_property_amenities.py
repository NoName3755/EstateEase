# Generated by Django 5.1.4 on 2024-12-13 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_alter_property_options_alter_property_is_active_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amenity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the amenity (e.g., Parking, Swimming Pool)', max_length=100, unique=True)),
                ('description', models.TextField(blank=True, help_text='Optional description of the amenity', null=True)),
                ('icon', models.ImageField(blank=True, help_text='Optional icon/image for the amenity', null=True, upload_to='amenity_icons/')),
            ],
        ),
        migrations.AlterModelOptions(
            name='inquiry',
            options={'verbose_name_plural': 'Inquiries'},
        ),
        migrations.AddField(
            model_name='property',
            name='amenities',
            field=models.ManyToManyField(blank=True, null=True, related_name='properties', to='listings.amenity'),
        ),
    ]