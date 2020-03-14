from django.db import models


class Note(models.Model):
    username=models.CharField(max_length=20)
    note_text = models.CharField(max_length=120)
    update = models.DateTimeField(auto_now_add=True)
    last_up_date = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return ' '.join([

        self.username,
        self.note_text,
        self.update,
        self.last_update_date,

    ])