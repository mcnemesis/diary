from django.db import models

KINDS_OF_WORK = (
        ('f', 'Formula'),
        ('r', 'Ritual'),
        ('l', 'Lesson'),
        ('e', 'Reminder'),
        ('s', 'Success'),
        ('l', 'Reflection'),
        ('a', 'Art'),
        ('d', 'Dream'),
        ('m', 'Miscellaneous'),
        )
FORMS_OF_ORIGINALITY = (
        ('o', 'Original'),
        ('d', 'Derived'),
        ('q', 'Quoted'),
        )

REMINDER_FREQUENCIES = (
        ('n', 'None'),
        ('o', 'Once'),
        ('d', 'Daily'),
        ('w', 'Weekly'),
        ('m', 'Monthly'),
        ('a', 'Annual'),
        #Because this is the realm of magicians...
        ('e', 'Decade'),
        ('c', 'Century'),
        ('m', 'Millenium'),
        )

class Event(models.Model):
    '''
    An object capturing the work of a magician in time
    '''
    created = models.DateTimeField ( auto_now_add = True )

    '''mandatory'''
    title = models.CharField( max_length = 137 )
    summary = models.TextField()
    date = models.DateField()
    kind = models.CharField( max_length = 1, choices = KINDS_OF_WORK )
    originality = models.CharField( max_length = 1, choices = FORMS_OF_ORIGINALITY )
    private = models.BooleanField( help_text = '''True: Is Private, False: Is Public''' )

    '''optional'''

    '''indexing'''
    references = models.TextField( help_text = '''Preferably: name|uri, name|uri,...''', blank = True, null = True  )
    tags = models.TextField( help_text = '''Preferably: tag, tag, tag,...''', blank = True, null = True )

    '''application'''
    purpose = models.CharField( max_length = 137 * 3 , blank = True, null = True )
    details = models.TextField( blank = True, null = True )

    '''involvement'''
    partners = models.TextField( help_text = '''Preferably: name|reference, name|reference,...''', blank = True, null = True  )

    '''placement'''
    time = models.TimeField( blank = True, null = True )
    place = models.CharField( max_length = 137, blank = True, null = True )

    '''GPS'''
    latitude = models.FloatField( blank = True, null = True )
    longitude = models.FloatField( blank = True, null = True )

    '''Reminder'''
    reminder_date = models.DateField( blank = True, null = True )
    reminder_time = models.TimeField( blank = True, null = True )
    reminder_frequency = models.CharField( max_length = 1, choices = REMINDER_FREQUENCIES, blank = True, null = True )

    '''art'''
    def primary_art_uploadto(instance,filename):
        return "art/%s/%s/%s" % ('primary',instance.id,filename)
    primary_art = models.ImageField( upload_to = primary_art_uploadto, blank = True, null = True )
    def secondary_art_uploadto(instance,filename):
        return "art/%s/%s/%s" % ('secondary',instance.id,filename)
    secondary_art = models.ImageField( upload_to = secondary_art_uploadto, blank = True, null = True )

    '''cross-referencing'''
    related = models.ManyToManyField( 'Event', related_name = 'referencing_entries', blank = True, null = True )

    @property
    def view_kind(self):
        return self.get_kind_display()
    @property
    def view_originality(self):
        return self.get_originality_display()
    @property
    def view_reminder_frequency(self):
        return self.get_reminder_frequency_display()
    @property
    def view_date(self):
        return self.date.strftime("%a %b %d, %Y")

    @staticmethod
    def public_stream():
        return Event.objects.filter( private = False )

    @staticmethod
    def stream():
        return Event.objects.all()

    def __unicode__(self):
        return '''%s[%s %s on %s] %s''' % (
                '*' if self.private else '',
                self.view_originality,
                self.view_kind,
                self.view_date,
                self.title
                )


