# Generated by Django 4.2.7 on 2023-11-26 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Descuentos', '0002_suscripcion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Descuento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('tipo', models.CharField(max_length=50)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('productos', models.ManyToManyField(blank=True, related_name='descuentos', to='Descuentos.producto')),
            ],
        ),
    ]
