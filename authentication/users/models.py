
# Create your models here.
from django.db import models

# Create your models here.

class Role(models.Model):
    todo_update = 'todo_update'
    todo_view = 'todo_view'
    # TEAM_MEMBER = 'TEAM MEMBER'
    name = models.CharField(max_length = 255, null = False)

    class Meta:
        db_table = 'roles'