# Generated by Django 4.2.4 on 2023-09-09 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_tag_project_vote_ratio_project_vote_total_review_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='created',
            field=models.DateTimeField(auto_created=True, blank=True, null=True),
        ),
    ]
