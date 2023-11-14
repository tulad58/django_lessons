# Generated by Django 4.2.4 on 2023-09-20 05:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_alter_scope_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scope',
            name='tags',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.tag'),
        ),
    ]
