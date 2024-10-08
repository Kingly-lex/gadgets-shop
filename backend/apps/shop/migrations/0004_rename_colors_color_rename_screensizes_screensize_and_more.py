# Generated by Django 5.0.1 on 2024-01-21 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_remove_product_colors_remove_product_screen_sizes_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Colors',
            new_name='Color',
        ),
        migrations.RenameModel(
            old_name='ScreenSizes',
            new_name='ScreenSize',
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Brand'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Phones', 'Phones'), ('Laptops', 'Laptops'), ('Desktops', 'Desktops'), ('Video_games', 'Video_games'), ('Tvs & Monitors', 'Tvs & Monitors'), ('Accessories', 'Accessories'), ('Others', 'Others')], default='Others', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='product',
            name='discount_percentage',
            field=models.SmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='specifications',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
