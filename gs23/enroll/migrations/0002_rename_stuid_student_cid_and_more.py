# Generated by Django 4.1 on 2022-09-10 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='stuid',
            new_name='cid',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='stuemail',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='stuname',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='stupass',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='tinfo',
            new_name='teacher_info',
        ),
        migrations.RenameField(
            model_name='teacherinfo',
            old_name='tid',
            new_name='cid',
        ),
        migrations.RenameField(
            model_name='teacherinfo',
            old_name='temail',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='teacherinfo',
            old_name='tname',
            new_name='name',
        ),
    ]
