from django.db import models

# Create your models here.


class Gk(models.Model):
    sofifa_id = models.AutoField(db_column='sofifa_id', primary_key=True)
    short_name = models.CharField(db_column='short_name', max_length=50)
    long_name = models.CharField(db_column='long_name', max_length=100)
    age = models.IntegerField(db_column='age')
    dob = models.DateField(db_column='dob')
    nationality = models.CharField(db_column='nationality', max_length=25)
    club = models.CharField(db_column='club', max_length=50)
    player_positions = models.CharField(db_column='player_positions', max_length=2)
    player_image = models. CharField(db_column='player_image', max_length=200)

    class Meta:
        managed = True
        db_table = 'gk'

    class Database:
        using = 'fifawebsite'


class Cam(models.Model):
    sofifa_id = models.AutoField(db_column='sofifa_id', primary_key=True)
    short_name = models.CharField(db_column='short_name', max_length=50)
    long_name = models.CharField(db_column='long_name', max_length=100)
    age = models.IntegerField(db_column='age')
    dob = models.DateField(db_column='dob')
    nationality = models.CharField(db_column='nationality', max_length=25)
    club = models.CharField(db_column='club', max_length=50)
    player_positions = models.CharField(db_column='player_positions', max_length=20)
    player_image = models. CharField(db_column='player_image', max_length=200)

    class Meta:
        managed = True
        db_table = 'cam'

    class Database:
        using = 'fifawebsite'


class Cb(models.Model):
    sofifa_id = models.AutoField(db_column='sofifa_id', primary_key=True)
    short_name = models.CharField(db_column='short_name', max_length=50)
    long_name = models.CharField(db_column='long_name', max_length=100)
    age = models.IntegerField(db_column='age')
    dob = models.DateField(db_column='dob')
    nationality = models.CharField(db_column='nationality', max_length=25)
    club = models.CharField(db_column='club', max_length=50)
    player_positions = models.CharField(db_column='player_positions', max_length=20)
    player_image = models. CharField(db_column='player_image', max_length=200)

    class Meta:
        managed = True
        db_table = 'cb'

    class Database:
        using = 'fifawebsite'


class Cdm(models.Model):
    sofifa_id = models.AutoField(db_column='sofifa_id', primary_key=True)
    short_name = models.CharField(db_column='short_name', max_length=50)
    long_name = models.CharField(db_column='long_name', max_length=100)
    age = models.IntegerField(db_column='age')
    dob = models.DateField(db_column='dob')
    nationality = models.CharField(db_column='nationality', max_length=25)
    club = models.CharField(db_column='club', max_length=50)
    player_positions = models.CharField(db_column='player_positions', max_length=20)
    player_image = models. CharField(db_column='player_image', max_length=200)

    class Meta:
        managed = True
        db_table = 'cdm'

    class Database:
        using = 'fifawebsite'


class Cf(models.Model):
    sofifa_id = models.AutoField(db_column='sofifa_id', primary_key=True)
    short_name = models.CharField(db_column='short_name', max_length=50)
    long_name = models.CharField(db_column='long_name', max_length=100)
    age = models.IntegerField(db_column='age')
    dob = models.DateField(db_column='dob')
    nationality = models.CharField(db_column='nationality', max_length=25)
    club = models.CharField(db_column='club', max_length=50)
    player_positions = models.CharField(db_column='player_positions', max_length=20)
    player_image = models. CharField(db_column='player_image', max_length=200)

    class Meta:
        managed = True
        db_table = 'cf'

    class Database:
        using = 'fifawebsite'


class Cm(models.Model):
    sofifa_id = models.AutoField(db_column='sofifa_id', primary_key=True)
    short_name = models.CharField(db_column='short_name', max_length=50)
    long_name = models.CharField(db_column='long_name', max_length=100)
    age = models.IntegerField(db_column='age')
    dob = models.DateField(db_column='dob')
    nationality = models.CharField(db_column='nationality', max_length=25)
    club = models.CharField(db_column='club', max_length=50)
    player_positions = models.CharField(db_column='player_positions', max_length=20)
    player_image = models. CharField(db_column='player_image', max_length=200)

    class Meta:
        managed = True
        db_table = 'cm'

    class Database:
        using = 'fifawebsite'


class Lb(models.Model):
    sofifa_id = models.AutoField(db_column='sofifa_id', primary_key=True)
    short_name = models.CharField(db_column='short_name', max_length=50)
    long_name = models.CharField(db_column='long_name', max_length=100)
    age = models.IntegerField(db_column='age')
    dob = models.DateField(db_column='dob')
    nationality = models.CharField(db_column='nationality', max_length=25)
    club = models.CharField(db_column='club', max_length=50)
    player_positions = models.CharField(db_column='player_positions', max_length=20)
    player_image = models. CharField(db_column='player_image', max_length=200)

    class Meta:
        managed = True
        db_table = 'lb'

    class Database:
        using = 'fifawebsite'


class Lm(models.Model):
    sofifa_id = models.AutoField(db_column='sofifa_id', primary_key=True)
    short_name = models.CharField(db_column='short_name', max_length=50)
    long_name = models.CharField(db_column='long_name', max_length=100)
    age = models.IntegerField(db_column='age')
    dob = models.DateField(db_column='dob')
    nationality = models.CharField(db_column='nationality', max_length=25)
    club = models.CharField(db_column='club', max_length=50)
    player_positions = models.CharField(db_column='player_positions', max_length=20)
    player_image = models. CharField(db_column='player_image', max_length=200)

    class Meta:
        managed = True
        db_table = 'lm'

    class Database:
        using = 'fifawebsite'


class Lw(models.Model):
    sofifa_id = models.AutoField(db_column='sofifa_id', primary_key=True)
    short_name = models.CharField(db_column='short_name', max_length=50)
    long_name = models.CharField(db_column='long_name', max_length=100)
    age = models.IntegerField(db_column='age')
    dob = models.DateField(db_column='dob')
    nationality = models.CharField(db_column='nationality', max_length=25)
    club = models.CharField(db_column='club', max_length=50)
    player_positions = models.CharField(db_column='player_positions', max_length=20)
    player_image = models. CharField(db_column='player_image', max_length=200)

    class Meta:
        managed = True
        db_table = 'lw'

    class Database:
        using = 'fifawebsite'


class Lwb(models.Model):
    sofifa_id = models.AutoField(db_column='sofifa_id', primary_key=True)
    short_name = models.CharField(db_column='short_name', max_length=50)
    long_name = models.CharField(db_column='long_name', max_length=100)
    age = models.IntegerField(db_column='age')
    dob = models.DateField(db_column='dob')
    nationality = models.CharField(db_column='nationality', max_length=25)
    club = models.CharField(db_column='club', max_length=50)
    player_positions = models.CharField(db_column='player_positions', max_length=20)
    player_image = models. CharField(db_column='player_image', max_length=200)

    class Meta:
        managed = True
        db_table = 'lwb'

    class Database:
        using = 'fifawebsite'


class Rb(models.Model):
    sofifa_id = models.AutoField(db_column='sofifa_id', primary_key=True)
    short_name = models.CharField(db_column='short_name', max_length=50)
    long_name = models.CharField(db_column='long_name', max_length=100)
    age = models.IntegerField(db_column='age')
    dob = models.DateField(db_column='dob')
    nationality = models.CharField(db_column='nationality', max_length=25)
    club = models.CharField(db_column='club', max_length=50)
    player_positions = models.CharField(db_column='player_positions', max_length=20)
    player_image = models. CharField(db_column='player_image', max_length=200)

    class Meta:
        managed = True
        db_table = 'rb'

    class Database:
        using = 'fifawebsite'


class Rm(models.Model):
    sofifa_id = models.AutoField(db_column='sofifa_id', primary_key=True)
    short_name = models.CharField(db_column='short_name', max_length=50)
    long_name = models.CharField(db_column='long_name', max_length=100)
    age = models.IntegerField(db_column='age')
    dob = models.DateField(db_column='dob')
    nationality = models.CharField(db_column='nationality', max_length=25)
    club = models.CharField(db_column='club', max_length=50)
    player_positions = models.CharField(db_column='player_positions', max_length=20)
    player_image = models. CharField(db_column='player_image', max_length=200)

    class Meta:
        managed = True
        db_table = 'rm'

    class Database:
        using = 'fifawebsite'


class Rw(models.Model):
    sofifa_id = models.AutoField(db_column='sofifa_id', primary_key=True)
    short_name = models.CharField(db_column='short_name', max_length=50)
    long_name = models.CharField(db_column='long_name', max_length=100)
    age = models.IntegerField(db_column='age')
    dob = models.DateField(db_column='dob')
    nationality = models.CharField(db_column='nationality', max_length=25)
    club = models.CharField(db_column='club', max_length=50)
    player_positions = models.CharField(db_column='player_positions', max_length=20)
    player_image = models. CharField(db_column='player_image', max_length=200)

    class Meta:
        managed = True
        db_table = 'rw'

    class Database:
        using = 'fifawebsite'


class Rwb(models.Model):
    sofifa_id = models.AutoField(db_column='sofifa_id', primary_key=True)
    short_name = models.CharField(db_column='short_name', max_length=50)
    long_name = models.CharField(db_column='long_name', max_length=100)
    age = models.IntegerField(db_column='age')
    dob = models.DateField(db_column='dob')
    nationality = models.CharField(db_column='nationality', max_length=25)
    club = models.CharField(db_column='club', max_length=50)
    player_positions = models.CharField(db_column='player_positions', max_length=20)
    player_image = models. CharField(db_column='player_image', max_length=200)

    class Meta:
        managed = True
        db_table = 'rwb'

    class Database:
        using = 'fifawebsite'


class St(models.Model):
    sofifa_id = models.AutoField(db_column='sofifa_id', primary_key=True)
    short_name = models.CharField(db_column='short_name', max_length=50)
    long_name = models.CharField(db_column='long_name', max_length=100)
    age = models.IntegerField(db_column='age')
    dob = models.DateField(db_column='dob')
    nationality = models.CharField(db_column='nationality', max_length=25)
    club = models.CharField(db_column='club', max_length=50)
    player_positions = models.CharField(db_column='player_positions', max_length=20)
    player_image = models. CharField(db_column='player_image', max_length=200)

    class Meta:
        managed = True
        db_table = 'st'

    class Database:
        using = 'fifawebsite'


class UserRatings(models.Model):
    user_id = models.IntegerField(db_column='user_id')
    sofifa_id = models.IntegerField(db_column='sofifa_id')
    position = models.CharField(db_column='player_position', max_length=3)
    rating = models.IntegerField(db_column='user_rating')

    class Meta:
        managed = True
        db_table = 'ratings'

    class Database:
        using = 'fifawebsite'


class UserFavorites(models.Model):
    user_id = models.IntegerField(db_column='user_id')
    sofifa_id = models.IntegerField(db_column='sofifa_id')
    position = models.CharField(db_column='player_position', max_length=3)
    favorite = models.IntegerField(db_column='favorite')

    class Meta:
        managed = True
        db_table = 'favorites'

    class Database:
        using = 'fifawebsite'
