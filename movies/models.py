from django.db import models
import uuid





class MoviesModel(models.Model):
    id              = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name            = models.CharField(max_length = 50, null=False, unique=True)
    duration        = models.CharField(max_length=20, null=True)
    parental_rating = models.CharField(max_length=20, null=False)
    sinopse         = models.CharField(max_length=255)
    imdb_rating     = models.CharField(max_length=10)
    release_date    = models.DateField(null = False)
    closing_date    =  models.DateField(null = False)
    created_at      = models.DateTimeField(auto_now_add = True, null = False)
    updated_at      = models.DateTimeField(auto_now = True, null = False)

    # !! esse app faz relação OneToMany com genres