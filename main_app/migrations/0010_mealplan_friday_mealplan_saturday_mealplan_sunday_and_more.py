# Generated by Django 4.1.7 on 2023-04-04 19:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_alter_recipe_day_of_week_mealplan'),
    ]

    operations = [
        migrations.AddField(
            model_name='mealplan',
            name='friday',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='friday', to='main_app.recipe'),
        ),
        migrations.AddField(
            model_name='mealplan',
            name='saturday',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='saturday', to='main_app.recipe'),
        ),
        migrations.AddField(
            model_name='mealplan',
            name='sunday',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='sunday', to='main_app.recipe'),
        ),
        migrations.AddField(
            model_name='mealplan',
            name='thursday',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='thursday', to='main_app.recipe'),
        ),
        migrations.AddField(
            model_name='mealplan',
            name='tuesday',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='tuesday', to='main_app.recipe'),
        ),
        migrations.AddField(
            model_name='mealplan',
            name='wednesday',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='wednesday', to='main_app.recipe'),
        ),
        migrations.AlterField(
            model_name='mealplan',
            name='monday',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='monday', to='main_app.recipe'),
        ),
    ]
