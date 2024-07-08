from django.db import models

# Create your models here.
class Agenda(models.Model):
    # ဒိုက်ထိုး
    title = models.CharField(max_length=255)
    # ဒိုက်ထိုးရင် ဘာတွေကောင်းလဲ
    content = models.TextField(null=True, blank=True)
    # ပုံ
    image = models.ImageField(upload_to='imageupload')
    # အချိန်
    time = models.IntegerField(blank=True, null=True)
    # အကြိမ်ရေ
    count = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title
