from django.db import models

from django.contrib.auth.models import User, Group
from django.utils.timezone import now

class Location(models.Model):
    """
    Class for Locations that have Members
    """
    lc_name = models.CharField(max_length=250, verbose_name=u'Locationname')
    lc_geo = models.CharField(max_length=100, verbose_name=u'Geoinformation', blank=True, null=True)
    lc_adr = models.CharField(max_length=250, verbose_name=u'Address', blank=True, null=True)
    lc_plz = models.CharField(max_length=40, verbose_name=u'PLZ', blank=True, null=True)
    lc_city = models.CharField(max_length=250, verbose_name=u'City', blank=True, null=True)
    lc_www = models.CharField(max_length=500, verbose_name=u'Website', blank=True, null=True)
    lc_mail = models.CharField(max_length=250, verbose_name=u'E-Mail', blank=True, null=True)
    lc_info = models.TextField(verbose_name=u'Info', blank=True, null=True)

    class Meta:
        verbose_name = u'Location'
        verbose_name_plural = u'Locations'

    def __unicode__(self):
        return self.lc_name


class Membership(models.Model):
    """
    Class for User-Membership in Locations
    """
    me_user = models.ForeignKey(User, related_name=u'Username')
    me_location = models.ForeignKey(Location, related_name=u'Location')
    me_trust1 = models.ForeignKey(User, related_name=u'Trust1', blank=True, null=True)
    me_trust2 = models.ForeignKey(User, related_name=u'Trust2', blank=True, null=True)
    me_add = models.DateTimeField(auto_now_add=True, editable=False, verbose_name=u'Added')
    me_lastedit = models.DateTimeField(auto_now=True, editable=False, verbose_name=u'LastEdit')

    class Meta:
        verbose_name = u'Membership'
        verbose_name_plural = u'Membership'

    def __unicode__(self):
        info = str(self.me_user) + " / " + str(self.me_location)
        return info


class Items(models.Model):
    """
    Class for Items that could be shared in Locations by Members
    """
    it_name = models.CharField(max_length=250, verbose_name=u'Name')
    it_info = models.TextField(verbose_name=u'Info', blank=True, null=True)
    it_add = models.DateTimeField(auto_now_add=True, editable=False, verbose_name=u'Added')
    it_lastedit = models.DateTimeField(auto_now=True, editable=False, verbose_name=u'Last Edit')
    it_back_to_owner = models.BooleanField(default=False, verbose_name=u'Back to Owner')
    it_personal_handover = models.BooleanField(default=False, verbose_name=u'personal handover')
    it_storageinfo = models.TextField(verbose_name=u'Storage Information', blank=True, null=True)
    it_owner = models.ForeignKey(User, related_name=u'Owner')

    class Meta:
        verbose_name = u'Item'
        verbose_name_plural = u'Items'

    def __unicode__(self):
        return self.it_name

class ShareEvents(models.Model):
    """
    Class for The Item Sharestate and Who is next
    """
    se_item = models.ForeignKey(Items, related_name=u'Item')
    se_possessor = models.ForeignKey(User, related_name=u'Possessor', blank=True, null=True)
    se_add = models.DateTimeField(auto_now_add=True, editable=False, verbose_name=u'Added')
    se_lastedit = models.DateTimeField(auto_now=True, editable=False, verbose_name=u'Last Edit')
    se_has_possessor = models.BooleanField(verbose_name=u'has Possessor', default=False)
    se_possessor_date = models.DateTimeField(verbose_name=u'Possessor Date', blank=True, null=True)
    se_info = models.TextField(verbose_name=u'Info', blank=True, null=True)

    class Meta:
        verbose_name = u'Share Event'
        verbose_name_plural = u'Share Events'

    def __unicode__(self):
        info = str(self.se_item) + " / " + str(self.se_possessor) + " / " + str(self.se_possessor_date)
        return info
