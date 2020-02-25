# Generated by Django 3.0.3 on 2020-02-25 14:36

from django.db import migrations


def copy_src_to_dst(Source, Destination):
    for src in Source.objects.all():
        dst = Destination(
            title=src.title,
            start=src.start,
            description=src.description,
            slots=src.slots,
        )

        dst.save()
        dst.speakers.set(src.speakers.all())
        src.delete()


def forward_course_abc_to_mti(apps, schema_editor):
    copy_src_to_dst(
        apps.get_model('core', 'CourseOld'),
        apps.get_model('core', 'Course')
    )


def backward_course_abc_to_mti(apps, schema_editor):
    copy_src_to_dst(
        apps.get_model('core', 'Course'),
        apps.get_model('core', 'CourseOld')
    )


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_course'),
    ]

    operations = [
        migrations.RunPython(forward_course_abc_to_mti,
                             backward_course_abc_to_mti)
    ]
