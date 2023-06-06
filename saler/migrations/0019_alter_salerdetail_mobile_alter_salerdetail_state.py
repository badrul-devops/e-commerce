# Generated by Django 4.2.1 on 2023-06-05 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saler', '0018_productreview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salerdetail',
            name='mobile',
            field=models.CharField(max_length=11, null=True),
        ),
        migrations.AlterField(
            model_name='salerdetail',
            name='state',
            field=models.CharField(choices=[('Bagerhat', 'Bagerhat'), ('Bandarban', 'Bandarban'), ('Barguna', 'Barguna'), ('Barisal', 'Barisal'), ('Bhola', 'Bhola'), ('Bogra', 'Bogra'), ('Brahmanbaria', 'Brahmanbaria'), ('Chandpur', 'Chandpur'), ('Chapainawabganj', 'Chapainawabganj'), ('Chittagong', 'Chittagong'), ('Chuadanga', 'Chuadanga'), ('Comilla', 'Comilla'), ("Cox's Bazar", "Cox's Bazar"), ('Dhaka', 'Dhaka'), ('Dinajpur', 'Dinajpur'), ('Faridpur', 'Faridpur'), ('Feni', 'Feni'), ('Gaibandha', 'Gaibandha'), ('Gazipur', 'Gazipur'), ('Gopalganj', 'Gopalganj'), ('Habiganj', 'Habiganj'), ('Jamalpur', 'Jamalpur'), ('Jessore', 'Jessore'), ('Jhalokati', 'Jhalokati'), ('Jhenaidah', 'Jhenaidah'), ('Joypurhat', 'Joypurhat'), ('Khagrachari', 'Khagrachari'), ('Khulna', 'Khulna'), ('Kishoreganj', 'Kishoreganj'), ('Kurigram', 'Kurigram'), ('Kushtia', 'Kushtia'), ('Lakshmipur', 'Lakshmipur'), ('Lalmonirhat', 'Lalmonirhat'), ('Madaripur', 'Madaripur'), ('Magura', 'Magura'), ('Manikganj', 'Manikganj'), ('Meherpur', 'Meherpur'), ('Moulvibazar', 'Moulvibazar'), ('Munshiganj', 'Munshiganj'), ('Mymensingh', 'Mymensingh'), ('Naogaon', 'Naogaon'), ('Narail', 'Narail'), ('Narayanganj', 'Narayanganj'), ('Narsingdi', 'Narsingdi'), ('Natore', 'Natore'), ('Nawabganj', 'Nawabganj'), ('Netrokona', 'Netrokona'), ('Nilphamari', 'Nilphamari'), ('Noakhali', 'Noakhali'), ('Pabna', 'Pabna'), ('Panchagarh', 'Panchagarh'), ('Patuakhali', 'Patuakhali'), ('Pirojpur', 'Pirojpur'), ('Rajbari', 'Rajbari'), ('Rajshahi', 'Rajshahi'), ('Rangamati', 'Rangamati'), ('Rangpur', 'Rangpur'), ('Satkhira', 'Satkhira'), ('Shariatpur', 'Shariatpur'), ('Sherpur', 'Sherpur'), ('Sirajganj', 'Sirajganj')], max_length=50, null=True),
        ),
    ]
