from django.db import models

KINDS_OF_WORK = (
        ('m', 'Meditation'),
        ('f', 'Formula'),
        ('r', 'Ritual'),
        ('d', 'Dream'),
        ('z', 'Realization'),
        ('l', 'Lesson'),
        ('n', 'Reflection'),
        ('e', 'Reminder'),
        ('a', 'Art'),
        ('i', 'Miscellaneous'),
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

    @property
    def has_references(self):
        return self.references is not None and len(self.references.strip()) > 0
    @property
    def has_partners(self):
        return self.partners is not None and len(self.partners.strip()) > 0
    @property
    def has_details(self):
        return self.details is not None and len(self.details.strip()) > 0
    @property
    def has_tags(self):
        return self.tags is not None and len(self.tags.strip()) > 0
    @property
    def has_purpose(self):
        return self.purpose is not None and len(self.purpose.strip()) > 0
    @property
    def has_art(self):
        try:
            return True if self.primary_art or self.secondary_art else False
        except:
            return False
    @property
    def has_related(self):
        return self.related is not None and self.related.all().count() > 0

    @property
    def has_primary_art(self):
        try:
            return True if self.primary_art else False
        except:
            return False

    @property
    def has_secondary_art(self):
        try:
            return True if self.secondary_art else False
        except:
            return False

    @property
    def tag_list(self):
        return map(lambda t:t.strip(), self.tags.split(',')) if self.has_tags else []

    @property
    def related_events(self):
        return self.related.all()

    @property
    def related_events_public(self):
        return self.related_events.filter( private = False )

    @property
    def has_related_events_public(self):
        if not self.has_related:
            return False
        else:
            return True if self.related_events_public.count() > 0 else False

    @property
    def reference_dicts(self):
        if self.has_references:
            try:
                return map(lambda r: {'name':r[0].strip(),'ref':r[1] }, map(lambda r: r.split('|') if '|' in r else [r,''], self.references.split(',')))
            except:
                return []
        else:
            return []
    @property
    def partners_dicts(self):
        if self.has_partners:
            try:
                return map(lambda r: {'name':r[0].strip(),'ref':r[1] }, map(lambda r: r.split('|') if '|' in r else [r,''], self.partners.split(',')))
            except:
                return []
        else:
            return []

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

class Log(models.Model):
    '''Just so we can automatically log activities happening in the magical diary app itself, and probably mine some statistics from them'''
    created = models.DateTimeField ( auto_now_add = True )
    log = models.TextField()
    kind = models.CharField( max_length = 137 )

    def view_log(self):
        return '''
        <div class="well well-large">
            <p>%s</p>
        </div>''' % self.log.replace("\n","\n<br/>\n")

    view_log.allow_tags = True
    view_log.short_description = 'Log'


