# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from .model_views import * 

# 
# class AdminLog(models.Model):
#     logid = models.AutoField(primary_key=True)
#     eventid = models.ForeignKey('AdminLogevents', models.DO_NOTHING, db_column='eventid')
#     time = models.DateTimeField()
#     ip = models.GenericIPAddressField(blank=True, null=True)
#     userid = models.IntegerField()
#     comments = models.CharField(max_length=1024, blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'admin_log'
# 
# 
# class AdminLogevents(models.Model):
#     eventid = models.IntegerField(primary_key=True)
#     event = models.CharField(max_length=255, blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'admin_logevents'
# 
# 
# class AdminPrefs(models.Model):
#     id = models.ForeignKey('AdminUsers', models.DO_NOTHING, db_column='id')
#     style_box = models.CharField(max_length=40)
#     style = models.CharField(max_length=40)
#     lang = models.CharField(max_length=2)
#     font = models.CharField(max_length=40)
#     fontsize = models.CharField(max_length=6)
#     mainwidth = models.SmallIntegerField()
#     icon_view = models.SmallIntegerField()
#     icon_logo = models.SmallIntegerField()
#     verb = models.SmallIntegerField()
#     debug = models.SmallIntegerField()
#     firsttab = models.SmallIntegerField()
#     showbanner = models.BooleanField()
#     listview1 = models.CharField(max_length=255)
#     listview2 = models.CharField(max_length=255)
# 
#     class Meta:
#         managed = False
#         db_table = 'admin_prefs'
# 
# 
# class AdminPrivs(models.Model):
#     id = models.ForeignKey('AdminUsers', models.DO_NOTHING, db_column='id')
#     trust_level = models.SmallIntegerField()
#     view_tabs = models.TextField(blank=True, null=True)  # This field type is a guess.
#     select_tables = models.TextField(blank=True, null=True)  # This field type is a guess.
#     insert_tables = models.TextField(blank=True, null=True)  # This field type is a guess.
#     update_tables = models.TextField(blank=True, null=True)  # This field type is a guess.
#     update_admin_tables = models.TextField(blank=True, null=True)  # This field type is a guess.
# 
#     class Meta:
#         managed = False
#         db_table = 'admin_privs'
# 
# 
# class AdminUsers(models.Model):
#     id = models.SmallIntegerField(primary_key=True)
#     name = models.CharField(unique=True, max_length=255)
#     password = models.CharField(max_length=20)
#     email = models.CharField(max_length=255, blank=True, null=True)
#     fullname = models.CharField(max_length=255, blank=True, null=True)
#     usertype = models.SmallIntegerField()
#     mygroup = models.SmallIntegerField()
#     active = models.BooleanField()
#     remoteip = models.CharField(max_length=15, blank=True, null=True)
#     sessioncode = models.CharField(max_length=20, blank=True, null=True)
#     lastconnect = models.DateTimeField(blank=True, null=True)
#     lastip = models.CharField(max_length=15, blank=True, null=True)
#     firstconnect = models.DateTimeField(blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'admin_users'
# 
# 
# class Aplant(models.Model):
#     aplantid = models.AutoField(primary_key=True)
#     formnum = models.SmallIntegerField(blank=True, null=True)
#     coldate = models.DateField(blank=True, null=True)
#     deprecated_latdeg = models.SmallIntegerField(blank=True, null=True)
#     deprecated_latmin = models.FloatField(blank=True, null=True)
#     deprecated_londeg = models.SmallIntegerField(blank=True, null=True)
#     deprecated_lonmin = models.FloatField(blank=True, null=True)
#     depth = models.FloatField(blank=True, null=True)
#     mapinfo = models.CharField(max_length=255, blank=True, null=True)
#     family = models.CharField(max_length=80, blank=True, null=True)
#     genus = models.CharField(max_length=80, blank=True, null=True)
#     species = models.CharField(max_length=80, blank=True, null=True)
#     common = models.CharField(max_length=80, blank=True, null=True)
#     author = models.CharField(max_length=80, blank=True, null=True)
#     light = models.SmallIntegerField(blank=True, null=True)
#     abund = models.SmallIntegerField(blank=True, null=True)
#     photonum = models.TextField(blank=True, null=True)  # This field type is a guess.
#     numindiv = models.SmallIntegerField(blank=True, null=True)
#     ethnologic = models.TextField(blank=True, null=True)
#     notes = models.TextField(blank=True, null=True)
#     identid = models.ForeignKey('People', models.DO_NOTHING, db_column='identid', blank=True, null=True)
#     herbname = models.CharField(max_length=80, blank=True, null=True)
#     herbdate = models.DateField(blank=True, null=True)
#     herbnum = models.CharField(max_length=80, blank=True, null=True)
#     active = models.BooleanField()
#     remove = models.BooleanField()
#     init = models.CharField(max_length=20)
#     initdate = models.DateField()
#     edit = models.CharField(max_length=20)
#     editdate = models.DateField()
#     lat = models.FloatField(blank=True, null=True)
#     lon = models.FloatField(blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'aplant'
# 
# 
# class Aplantorgan(models.Model):
#     sampleid = models.ForeignKey('Sample', models.DO_NOTHING, db_column='sampleid')
#     expedid = models.ForeignKey('Exped', models.DO_NOTHING, db_column='expedid')
#     aplantid = models.ForeignKey(Aplant, models.DO_NOTHING, db_column='aplantid')
#     organ = models.CharField(max_length=20)
#     color = models.CharField(max_length=20, blank=True, null=True)
#     smell = models.CharField(max_length=20, blank=True, null=True)
#     weight = models.FloatField(blank=True, null=True)
#     notes = models.TextField(blank=True, null=True)
#     active = models.BooleanField()
#     remove = models.BooleanField()
#     init = models.CharField(max_length=20)
#     initdate = models.DateField()
#     edit = models.CharField(max_length=20)
#     editdate = models.DateField()
# 
#     class Meta:
#         managed = False
#         db_table = 'aplantorgan'
# 
# 
# class AppGroups(models.Model):
#     appgroupid = models.SmallIntegerField(primary_key=True)
#     title = models.CharField(max_length=255, blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'app_groups'
# 
# 
# class Apps(models.Model):
#     appid = models.SmallIntegerField(primary_key=True)
#     app = models.CharField(unique=True, max_length=255)
#     title = models.CharField(max_length=255, blank=True, null=True)
#     subtitle = models.CharField(max_length=255, blank=True, null=True)
#     icon_plain = models.CharField(max_length=255, blank=True, null=True)
#     icon_fancy = models.CharField(max_length=255, blank=True, null=True)
#     icon_bevel = models.CharField(max_length=255, blank=True, null=True)
#     appgroupid = models.ForeignKey(AppGroups, models.DO_NOTHING, db_column='appgroupid')
#     appsubgroup = models.CharField(max_length=255, blank=True, null=True)
#     appfile = models.CharField(max_length=255, blank=True, null=True)
#     acllevels = models.TextField(blank=True, null=True)  # This field type is a guess.
#     status = models.CharField(max_length=255, blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'apps'
# 
# 
# class Assay(models.Model):
#     assayid = models.AutoField(primary_key=True)
#     targetid = models.ForeignKey('Target', models.DO_NOTHING, db_column='targetid')
#     title = models.CharField(max_length=255)
#     folder = models.CharField(max_length=255, blank=True, null=True)
#     detection_meth = models.IntegerField(blank=True, null=True)
#     data_format = models.IntegerField()
#     substrate = models.CharField(max_length=255, blank=True, null=True)
#     ref_compound = models.CharField(max_length=255, blank=True, null=True)
#     mode_of_action = models.IntegerField(blank=True, null=True)
#     sopfile = models.CharField(max_length=255)
#     developer = models.CharField(max_length=255, blank=True, null=True)
#     validator = models.CharField(max_length=255, blank=True, null=True)
#     status = models.SmallIntegerField()
#     comments = models.TextField(blank=True, null=True)
#     init = models.CharField(max_length=20)
#     initdate = models.DateField()
#     edit = models.CharField(max_length=20)
#     editdate = models.DateField()
#     active = models.BooleanField()
#     title_short = models.CharField(max_length=255)
# 
#     class Meta:
#         managed = False
#         db_table = 'assay'
# 
# 
# class BarcodeIds(models.Model):
#     username = models.CharField(max_length=1024)
#     position = models.IntegerField()
#     message = models.TextField(blank=True, null=True)
#     barcodeid = models.IntegerField(blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'barcode_ids'
#         unique_together = (('username', 'position'),)
# 
# 
# class BarcodePageSetup(models.Model):
#     id = models.IntegerField(unique=True)
#     title = models.CharField(unique=True, max_length=1024)
#     style = models.CharField(max_length=80)
#     page_size_x_mm = models.FloatField()
#     page_size_y_mm = models.FloatField()
#     page_size_title = models.CharField(max_length=80)
#     page_tmargin = models.FloatField()
#     page_bmargin = models.FloatField()
#     page_lmargin = models.FloatField()
#     page_rmargin = models.FloatField()
#     columns = models.IntegerField()
#     rows = models.IntegerField()
#     label_tmargin = models.FloatField()
#     label_lmargin = models.FloatField()
#     barcode_encoding = models.CharField(max_length=80)
#     image = models.CharField(max_length=80, blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'barcode_page_setup'
# 
# 
# class BarcodePageSetupUser(models.Model):
#     username = models.CharField(unique=True, max_length=1024)
#     page_setup = models.ForeignKey(BarcodePageSetup, models.DO_NOTHING)
# 
#     class Meta:
#         managed = False
#         db_table = 'barcode_page_setup_user'
# 
# 
# class CcaResults(models.Model):
#     cca_resultid = models.AutoField(primary_key=True)
#     sampleid = models.ForeignKey('Sample', models.DO_NOTHING, db_column='sampleid', blank=True, null=True)
#     chemclassid = models.ForeignKey('ChemicalClasses', models.DO_NOTHING, db_column='chemclassid', blank=True, null=True)
#     ref_table = models.CharField(max_length=20, blank=True, null=True)
#     ref_fkey = models.CharField(max_length=20, blank=True, null=True)
#     ref_id = models.IntegerField(blank=True, null=True)
#     bresult = models.NullBooleanField()
# 
#     class Meta:
#         managed = False
#         db_table = 'cca_results'
# 
# 
# class ChemicalClasses(models.Model):
#     chemclassid = models.SmallIntegerField(primary_key=True)
#     classname = models.CharField(max_length=80, blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'chemical_classes'
# 
# 
# class Compound(models.Model):
#     sampleid = models.ForeignKey('Sample', models.DO_NOTHING, db_column='sampleid')
#     origin_sampleid = models.ForeignKey('Sample', models.DO_NOTHING, db_column='origin_sampleid', blank=True, null=True)
#     opeid = models.ForeignKey('People', models.DO_NOTHING, db_column='opeid', blank=True, null=True)
#     isolationdate = models.DateField()
#     depid = models.ForeignKey('People', models.DO_NOTHING, db_column='depid')
#     notes = models.TextField()
#     active = models.BooleanField()
#     remove = models.BooleanField()
#     purity_pct = models.SmallIntegerField()
#     purity_notes = models.TextField()
#     quantity = models.FloatField()
#     volume = models.FloatField(blank=True, null=True)
#     solvent = models.CharField(max_length=255, blank=True, null=True)
#     mw = models.FloatField()
#     formula = models.CharField(max_length=255, blank=True, null=True)
#     name_common = models.CharField(max_length=255, blank=True, null=True)
#     name_iupac = models.CharField(max_length=255, blank=True, null=True)
#     smiles = models.CharField(max_length=255, blank=True, null=True)
#     init = models.CharField(max_length=20)
#     initdate = models.DateField()
#     edit = models.CharField(max_length=20)
#     editdate = models.DateField()
# 
#     class Meta:
#         managed = False
#         db_table = 'compound'
# 
# 
# class DataTannin(models.Model):
#     plateid = models.ForeignKey('PlateTannin', models.DO_NOTHING, db_column='plateid')
#     row = models.CharField(max_length=1, blank=True, null=True)
#     col = models.SmallIntegerField(blank=True, null=True)
#     red = models.SmallIntegerField(blank=True, null=True)
#     green = models.SmallIntegerField(blank=True, null=True)
#     blue = models.SmallIntegerField(blank=True, null=True)
#     score = models.FloatField(blank=True, null=True)
#     active = models.NullBooleanField()
# 
#     class Meta:
#         managed = False
#         db_table = 'data_tannin'
#         unique_together = (('plateid', 'row', 'col'),)
# 
# 
# class Dna(models.Model):
#     reftable = models.CharField(max_length=20, blank=True, null=True)
#     refid = models.IntegerField(blank=True, null=True)
#     analdate = models.DateField(blank=True, null=True)
#     analid = models.SmallIntegerField(blank=True, null=True)
#     analmethod = models.CharField(max_length=255, blank=True, null=True)
#     filename = models.CharField(max_length=255, blank=True, null=True)
#     nbands = models.SmallIntegerField(blank=True, null=True)
#     coords = models.CharField(max_length=255, blank=True, null=True)
#     init = models.CharField(max_length=20)
#     initdate = models.DateField()
#     edit = models.CharField(max_length=20)
#     editdate = models.DateField()
# 
#     class Meta:
#         managed = False
#         db_table = 'dna'
# 
# 
# class Exped(models.Model):
#     expedid = models.AutoField(primary_key=True)
#     startdate = models.DateField(blank=True, null=True)
#     enddate = models.DateField(blank=True, null=True)
#     country = models.CharField(max_length=20, blank=True, null=True)
#     state = models.CharField(max_length=80, blank=True, null=True)
#     muni = models.CharField(max_length=80, blank=True, null=True)
#     district = models.CharField(max_length=80, blank=True, null=True)
#     sitename = models.CharField(max_length=80, blank=True, null=True)
#     colid = models.ForeignKey('People', models.DO_NOTHING, db_column='colid', blank=True, null=True)
#     depid = models.ForeignKey('People', models.DO_NOTHING, db_column='depid', blank=True, null=True)
#     licid = models.IntegerField(blank=True, null=True)
#     lic_number = models.CharField(max_length=80, blank=True, null=True)
#     lic_issuedate = models.DateField(blank=True, null=True)
#     lic_expdate = models.DateField(blank=True, null=True)
#     trans_permitno = models.CharField(max_length=80, blank=True, null=True)
#     trans_issuedby = models.CharField(max_length=80, blank=True, null=True)
#     trans_issuedate = models.DateField(blank=True, null=True)
#     equip_gps = models.CharField(max_length=80, blank=True, null=True)
#     equip_camera = models.CharField(max_length=80, blank=True, null=True)
#     notes = models.TextField(blank=True, null=True)
#     active = models.BooleanField()
#     remove = models.BooleanField()
#     process_status = models.SmallIntegerField()
#     init = models.CharField(max_length=20)
#     initdate = models.DateField()
#     edit = models.CharField(max_length=20)
#     editdate = models.DateField()
#     lat = models.FloatField(blank=True, null=True)
#     latsd = models.FloatField(blank=True, null=True)
#     lonsd = models.FloatField(blank=True, null=True)
#     lon = models.FloatField(blank=True, null=True)
#     nspecies = models.FloatField(blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'exped'
# 
# 
# class Family(models.Model):
#     abbr = models.CharField(max_length=4)
#     name = models.CharField(max_length=255)
# 
#     class Meta:
#         managed = False
#         db_table = 'family'
# 
# 
# class FitPlatePos(models.Model):
#     runid = models.ForeignKey('Run', models.DO_NOTHING, db_column='runid')
#     row = models.CharField(max_length=1)
#     col = models.SmallIntegerField()
#     conc = models.FloatField(blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'fit_plate_pos'
#         unique_together = (('runid', 'row', 'col'),)
# 
# 
# class FitSetup(models.Model):
#     runid = models.ForeignKey('Run', models.DO_NOTHING, db_column='runid')
#     contents = models.ForeignKey('PlateMapContents', models.DO_NOTHING, db_column='contents')
#     association = models.SmallIntegerField(blank=True, null=True)
#     eqid = models.SmallIntegerField(blank=True, null=True)
#     starting = models.CharField(max_length=255, blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'fit_setup'
#         unique_together = (('runid', 'contents', 'association'),)
# 
# 
# class Fraction(models.Model):
#     sampleid = models.ForeignKey('Sample', models.DO_NOTHING, db_column='sampleid', unique=True)
#     fractionationid = models.ForeignKey('Fractionation', models.DO_NOTHING, db_column='fractionationid', blank=True, null=True)
#     opeid = models.ForeignKey('People', models.DO_NOTHING, db_column='opeid', blank=True, null=True)
#     rt_start = models.FloatField(blank=True, null=True)
#     rt_end = models.FloatField(blank=True, null=True)
#     frac_number = models.SmallIntegerField(blank=True, null=True)
#     notes = models.TextField(blank=True, null=True)
#     active = models.BooleanField()
#     status = models.SmallIntegerField()
#     init = models.CharField(max_length=20)
#     initdate = models.DateField()
#     edit = models.CharField(max_length=20)
#     editdate = models.DateField()
# 
#     class Meta:
#         managed = False
#         db_table = 'fraction'
# 
# 
# class FractionPre(models.Model):
#     opeid = models.ForeignKey('People', models.DO_NOTHING, db_column='opeid')
#     frac_protocol = models.SmallIntegerField()
#     sampleid = models.IntegerField()
# 
#     class Meta:
#         managed = False
#         db_table = 'fraction_pre'
# 
# 
# class Fractionation(models.Model):
#     fractionationid = models.AutoField(primary_key=True)
#     date = models.DateField(blank=True, null=True)
#     opeid = models.ForeignKey('People', models.DO_NOTHING, db_column='opeid', blank=True, null=True)
#     frac_protocol = models.SmallIntegerField()
#     protocoldesc = models.TextField(blank=True, null=True)
#     pfssampleid = models.ForeignKey('Sample', models.DO_NOTHING, db_column='pfssampleid', blank=True, null=True)
#     pfsdesc = models.TextField(blank=True, null=True)
#     data_file = models.CharField(max_length=255, blank=True, null=True)
#     data_image = models.CharField(max_length=255, blank=True, null=True)
#     notes = models.TextField(blank=True, null=True)
#     active = models.BooleanField()
#     status = models.SmallIntegerField()
#     remove = models.NullBooleanField()
#     init = models.CharField(max_length=20)
#     initdate = models.DateField()
#     edit = models.CharField(max_length=20)
#     editdate = models.DateField()
# 
#     class Meta:
#         managed = False
#         db_table = 'fractionation'
# 
# 
# class HitSelection(models.Model):
#     runprocessid = models.ForeignKey('RunProcess', models.DO_NOTHING, db_column='runprocessid')
#     sampleid = models.ForeignKey('Sample', models.DO_NOTHING, db_column='sampleid')
#     deprecated_sample_type = models.ForeignKey('SampleTypes', models.DO_NOTHING, db_column='deprecated_sample_type', blank=True, null=True)
#     src_pfssampleid = models.ForeignKey('Sample', models.DO_NOTHING, db_column='src_pfssampleid', blank=True, null=True)
#     src_tplantid = models.ForeignKey('Tplant', models.DO_NOTHING, db_column='src_tplantid', blank=True, null=True)
#     src_aplantid = models.ForeignKey(Aplant, models.DO_NOTHING, db_column='src_aplantid', blank=True, null=True)
#     wave = models.SmallIntegerField()
#     time = models.IntegerField()
#     moplateid = models.ForeignKey('PlateMother', models.DO_NOTHING, db_column='moplateid', blank=True, null=True)
#     origin_plateid = models.ForeignKey('Plate', models.DO_NOTHING, db_column='origin_plateid')
#     row = models.CharField(max_length=1)
#     col = models.SmallIntegerField()
#     plateprocdatasetid = models.ForeignKey('PlateProcdataset', models.DO_NOTHING, db_column='plateprocdatasetid')
#     result = models.FloatField()
#     error = models.FloatField()
#     origin = models.CharField(max_length=2)
#     z = models.FloatField(blank=True, null=True)
#     sample_type = models.CharField(max_length=20)
#     sample_subtype = models.CharField(max_length=20)
#     pp_plateid = models.ForeignKey('Plate', models.DO_NOTHING, db_column='pp_plateid')
# 
#     class Meta:
#         managed = False
#         db_table = 'hit_selection'
#         unique_together = (('runprocessid', 'origin_plateid', 'plateprocdatasetid', 'row', 'col'),)
# 
# 
# class Insect(models.Model):
#     sampleid = models.ForeignKey('Sample', models.DO_NOTHING, db_column='sampleid')
#     notes = models.TextField(blank=True, null=True)
#     active = models.NullBooleanField()
#     remove = models.NullBooleanField()
#     init = models.CharField(max_length=20)
#     initdate = models.DateField()
#     edit = models.CharField(max_length=20)
#     editdate = models.DateField()
# 
#     class Meta:
#         managed = False
#         db_table = 'insect'
# 
# 
# class JoinPlateProcdataset(models.Model):
#     plateprocdatasetid = models.ForeignKey('PlateProcdataset', models.DO_NOTHING, db_column='plateprocdatasetid')
#     platedatasetid = models.ForeignKey('PlateDataset', models.DO_NOTHING, db_column='platedatasetid')
# 
#     class Meta:
#         managed = False
#         db_table = 'join_plate_procdataset'
#         unique_together = (('plateprocdatasetid', 'platedatasetid'),)
# 
# 
# class Lcms(models.Model):
#     lcmsid = models.AutoField(primary_key=True)
#     sampleid = models.ForeignKey('Sample', models.DO_NOTHING, db_column='sampleid', blank=True, null=True)
#     analdate = models.DateField()
#     opeid = models.ForeignKey('People', models.DO_NOTHING, db_column='opeid')
#     sampleconc = models.FloatField(blank=True, null=True)
#     temp = models.FloatField(blank=True, null=True)
#     flow = models.FloatField(blank=True, null=True)
#     volume = models.FloatField(blank=True, null=True)
#     lcmscolumn = models.IntegerField(blank=True, null=True)
#     lcmsmethod = models.IntegerField(blank=True, null=True)
#     methodnotes = models.TextField(blank=True, null=True)
#     project = models.IntegerField()
#     channelid = models.IntegerField()
#     quality = models.IntegerField(blank=True, null=True)
#     wavelength1 = models.FloatField(blank=True, null=True)
#     wavelength2 = models.FloatField(blank=True, null=True)
#     retention = models.TextField(blank=True, null=True)  # This field type is a guess.
#     notes = models.TextField(blank=True, null=True)
#     active = models.BooleanField()
#     remove = models.BooleanField()
#     init = models.CharField(max_length=20)
#     initdate = models.DateField()
#     edit = models.CharField(max_length=20)
#     editdate = models.DateField()
# 
#     class Meta:
#         managed = False
#         db_table = 'lcms'
# 
# 
# class Microorganism(models.Model):
#     sampleid = models.ForeignKey('Sample', models.DO_NOTHING, db_column='sampleid')
#     notes = models.TextField(blank=True, null=True)
#     active = models.NullBooleanField()
#     remove = models.NullBooleanField()
#     init = models.CharField(max_length=20)
#     initdate = models.DateField()
#     edit = models.CharField(max_length=20)
#     editdate = models.DateField()
# 
#     class Meta:
#         managed = False
#         db_table = 'microorganism'
# 
# 
# class Nmr(models.Model):
#     reftable = models.CharField(max_length=20, blank=True, null=True)
#     refid = models.IntegerField(blank=True, null=True)
#     analdate = models.DateField(blank=True, null=True)
#     opeid = models.SmallIntegerField(blank=True, null=True)
#     analmethod = models.CharField(max_length=255, blank=True, null=True)
#     filename = models.CharField(max_length=255, blank=True, null=True)
#     h1_shifts = models.CharField(max_length=255, blank=True, null=True)
#     c13_shifts = models.CharField(max_length=255, blank=True, null=True)
#     init = models.CharField(max_length=20)
#     initdate = models.DateField()
#     edit = models.CharField(max_length=20)
#     editdate = models.DateField()
# 
#     class Meta:
#         managed = False
#         db_table = 'nmr'
# 
# 
# class People(models.Model):
#     peopleid = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=10, blank=True, null=True)
#     first = models.CharField(max_length=80, blank=True, null=True)
#     last = models.CharField(max_length=80)
#     other = models.CharField(max_length=80, blank=True, null=True)
#     category = models.TextField(blank=True, null=True)  # This field type is a guess.
#     aff = models.CharField(max_length=80, blank=True, null=True)
#     train = models.CharField(max_length=80, blank=True, null=True)
#     add1 = models.CharField(max_length=80, blank=True, null=True)
#     add2 = models.CharField(max_length=80, blank=True, null=True)
#     add3 = models.CharField(max_length=80, blank=True, null=True)
#     city = models.CharField(max_length=80, blank=True, null=True)
#     state = models.CharField(max_length=80, blank=True, null=True)
#     country = models.CharField(max_length=80, blank=True, null=True)
#     zip = models.CharField(max_length=80, blank=True, null=True)
#     contact1 = models.CharField(max_length=255, blank=True, null=True)
#     contact2 = models.CharField(max_length=255, blank=True, null=True)
#     contact3 = models.CharField(max_length=255, blank=True, null=True)
#     contact4 = models.CharField(max_length=255, blank=True, null=True)
#     contact5 = models.CharField(max_length=255, blank=True, null=True)
#     contact6 = models.CharField(max_length=255, blank=True, null=True)
#     contact7 = models.CharField(max_length=255, blank=True, null=True)
#     notes = models.TextField(blank=True, null=True)
#     active = models.BooleanField()
#     remove = models.BooleanField()
#     init = models.CharField(max_length=20)
#     initdate = models.DateField()
#     edit = models.CharField(max_length=20)
#     editdate = models.DateField()
#     nationality = models.CharField(max_length=80, blank=True, null=True)
#     marriage = models.CharField(max_length=80, blank=True, null=True)
#     cartemisor = models.CharField(max_length=80, blank=True, null=True)
#     cartid = models.CharField(max_length=80, blank=True, null=True)
#     cpf = models.CharField(max_length=80, blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'people'
# 
# 
# class Plate(models.Model):
#     plateid = models.AutoField(primary_key=True)
#     platetype = models.CharField(max_length=2)
#     platemapid = models.ForeignKey('PlateMap', models.DO_NOTHING, db_column='platemapid')
#     solvent = models.CharField(max_length=255)
#     origin = models.CharField(max_length=2, blank=True, null=True)
#     active = models.SmallIntegerField()
#     init = models.CharField(max_length=20)
#     initdate = models.DateField()
#     edit = models.CharField(max_length=20)
#     editdate = models.DateField()
# 
#     class Meta:
#         managed = False
#         db_table = 'plate'
# 
# 
# class PlateAssay(models.Model):
#     plateid = models.ForeignKey(Plate, models.DO_NOTHING, db_column='plateid', unique=True)
#     runid = models.ForeignKey('Run', models.DO_NOTHING, db_column='runid')
#     origin_plateid = models.ForeignKey(Plate, models.DO_NOTHING, db_column='origin_plateid', blank=True, null=True)
#     origin_volume = models.FloatField(blank=True, null=True)
#     volume_init = models.FloatField(blank=True, null=True)
#     deprecated_repid = models.IntegerField(blank=True, null=True)
#     origin = models.CharField(max_length=2, blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'plate_assay'
# 
# 
# class PlateDataset(models.Model):
#     platedatasetid = models.AutoField(primary_key=True)
#     runid = models.ForeignKey('Run', models.DO_NOTHING, db_column='runid')
#     plateid = models.IntegerField()
#     wave = models.SmallIntegerField(blank=True, null=True)
#     time = models.IntegerField(blank=True, null=True)
#     filename = models.CharField(max_length=80, blank=True, null=True)
#     pp_plateid = models.ForeignKey(Plate, models.DO_NOTHING, db_column='pp_plateid')
#     pp_platetype = models.CharField(max_length=2)
# 
#     class Meta:
#         managed = False
#         db_table = 'plate_dataset'
#         unique_together = (('runid', 'plateid', 'wave', 'time'),)
# 
# 
# class PlateDatasetResult(models.Model):
#     platedatasetid = models.ForeignKey(PlateDataset, models.DO_NOTHING, db_column='platedatasetid')
#     row = models.CharField(max_length=1, blank=True, null=True)
#     col = models.SmallIntegerField(blank=True, null=True)
#     result = models.FloatField(blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'plate_dataset_result'
#         unique_together = (('platedatasetid', 'row', 'col'),)
# 
# 
# class PlateDilution(models.Model):
#     plateid = models.ForeignKey(Plate, models.DO_NOTHING, db_column='plateid', unique=True)
#     mo_plateid = models.ForeignKey('PlateMother', models.DO_NOTHING, db_column='mo_plateid', blank=True, null=True)
#     mo_volume = models.FloatField()
#     is_diluted = models.BooleanField()
#     di_date = models.DateField(blank=True, null=True)
#     expire_date = models.DateField(blank=True, null=True)
#     volume_dilution = models.FloatField(blank=True, null=True)
#     volume_current = models.FloatField(blank=True, null=True)
#     comments = models.TextField(blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'plate_dilution'
# 
# 
# class PlateDiscovery(models.Model):
#     plateid = models.ForeignKey(Plate, models.DO_NOTHING, db_column='plateid', unique=True)
#     creation_date = models.DateField()
#     expire_date = models.DateField()
#     volume_current = models.FloatField()
#     comments = models.TextField(blank=True, null=True)
#     assayid = models.ForeignKey(Assay, models.DO_NOTHING, db_column='assayid', blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'plate_discovery'
# 
# 
# class PlateMap(models.Model):
#     mapid = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=255)
#     active = models.SmallIntegerField()
#     description = models.TextField(blank=True, null=True)
#     firstrow = models.CharField(max_length=1)
#     lastrow = models.CharField(max_length=1)
#     firstcol = models.SmallIntegerField()
#     lastcol = models.SmallIntegerField()
#     init = models.CharField(max_length=20)
#     initdate = models.DateField()
#     edit = models.CharField(max_length=20)
#     editdate = models.DateField()
# 
#     class Meta:
#         managed = False
#         db_table = 'plate_map'
# 
# 
# class PlateMapContents(models.Model):
#     short = models.CharField(primary_key=True, max_length=4)
#     long = models.CharField(max_length=255)
# 
#     class Meta:
#         managed = False
#         db_table = 'plate_map_contents'
# 
# 
# class PlateMapPos(models.Model):
#     mapid = models.ForeignKey(PlateMap, models.DO_NOTHING, db_column='mapid')
#     contents = models.ForeignKey(PlateMapContents, models.DO_NOTHING, db_column='contents')
#     association = models.SmallIntegerField(blank=True, null=True)
#     row = models.CharField(max_length=1)
#     col = models.SmallIntegerField()
# 
#     class Meta:
#         managed = False
#         db_table = 'plate_map_pos'
#         unique_together = (('mapid', 'row', 'col'),)
# 
# 
# class PlateMother(models.Model):
#     plateid = models.ForeignKey(Plate, models.DO_NOTHING, db_column='plateid', unique=True)
#     volume_init = models.FloatField(blank=True, null=True)
#     volume_current = models.FloatField(blank=True, null=True)
#     comments = models.TextField(blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'plate_mother'
# 
# 
# class PlatePos(models.Model):
#     plateid = models.ForeignKey(Plate, models.DO_NOTHING, db_column='plateid')
#     sampleid = models.ForeignKey('Sample', models.DO_NOTHING, db_column='sampleid', blank=True, null=True)
#     description = models.CharField(max_length=255, blank=True, null=True)
#     row = models.CharField(max_length=1, blank=True, null=True)
#     col = models.SmallIntegerField(blank=True, null=True)
#     conc = models.FloatField(blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'plate_pos'
#         unique_together = (('plateid', 'row', 'col'),)
# 
# 
# class PlateProcdataset(models.Model):
#     plateprocdatasetid = models.AutoField(primary_key=True)
#     runprocessid = models.ForeignKey('RunProcess', models.DO_NOTHING, db_column='runprocessid')
#     ndatasets = models.SmallIntegerField(blank=True, null=True)
#     cp1_avg = models.FloatField(blank=True, null=True)
#     cp1_sd = models.FloatField(blank=True, null=True)
#     cn1_avg = models.FloatField(blank=True, null=True)
#     cn1_sd = models.FloatField(blank=True, null=True)
#     s_avg = models.FloatField(blank=True, null=True)
#     s_sd = models.FloatField(blank=True, null=True)
#     zstar = models.FloatField(blank=True, null=True)
#     zprime = models.FloatField(blank=True, null=True)
#     rc1_eqid = models.SmallIntegerField(blank=True, null=True)
#     rc1_chi_sq = models.FloatField(blank=True, null=True)
#     rc1_nfitparams = models.SmallIntegerField(blank=True, null=True)
#     rc1_fitparams_avg = models.CharField(max_length=1024, blank=True, null=True)
#     rc1_fitparams_sd = models.CharField(max_length=1024, blank=True, null=True)
#     pp_plateid = models.ForeignKey(Plate, models.DO_NOTHING, db_column='pp_plateid')
# 
#     class Meta:
#         managed = False
#         db_table = 'plate_procdataset'
# 
# 
# class PlateProcdatasetResult(models.Model):
#     plateprocdatasetid = models.ForeignKey(PlateProcdataset, models.DO_NOTHING, db_column='plateprocdatasetid')
#     row = models.CharField(max_length=1)
#     col = models.SmallIntegerField()
#     result = models.FloatField(blank=True, null=True)
#     error = models.FloatField(blank=True, null=True)
#     conc = models.FloatField(blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'plate_procdataset_result'
#         unique_together = (('plateprocdatasetid', 'row', 'col'),)
# 
# 
# class PlateProcdatasetResultStat(models.Model):
#     plateprocdatasetid = models.ForeignKey(PlateProcdataset, models.DO_NOTHING, db_column='plateprocdatasetid')
#     deprecated_contents = models.CharField(max_length=2, blank=True, null=True)
#     assoc = models.SmallIntegerField(blank=True, null=True)
#     deprecated_statistic = models.CharField(max_length=10, blank=True, null=True)
#     result = models.FloatField(blank=True, null=True)
#     statistic = models.CharField(max_length=10, blank=True, null=True)
#     contents = models.CharField(max_length=4)
# 
#     class Meta:
#         managed = False
#         db_table = 'plate_procdataset_result_stat'
#         unique_together = (('deprecated_statistic', 'plateprocdatasetid', 'deprecated_contents', 'assoc'),)
# 
# 
# class PlateTannin(models.Model):
#     plateid = models.ForeignKey(Plate, models.DO_NOTHING, db_column='plateid', unique=True)
#     analdate = models.DateField(blank=True, null=True)
#     opeid = models.ForeignKey(People, models.DO_NOTHING, db_column='opeid', blank=True, null=True)
#     imagefile = models.CharField(unique=True, max_length=80, blank=True, null=True)
#     scanfile = models.CharField(unique=True, max_length=80, blank=True, null=True)
#     dilution = models.FloatField(blank=True, null=True)
#     notes = models.TextField(blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'plate_tannin'
# 
# 
# class Project(models.Model):
#     projectid = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=255)
#     notes = models.TextField(blank=True, null=True)
#     active = models.BooleanField()
#     remove = models.BooleanField()
#     init = models.CharField(max_length=20)
#     initdate = models.DateField()
#     edit = models.CharField(max_length=20)
#     editdate = models.DateField()
#     last_recalc = models.DateTimeField()
# 
#     class Meta:
#         managed = False
#         db_table = 'project'
# 
# 
# class ProjectAssociate(models.Model):
#     screenid = models.ForeignKey('ProjectScreen', models.DO_NOTHING, db_column='screenid')
#     runprocessid = models.ForeignKey('RunProcess', models.DO_NOTHING, db_column='runprocessid')
# 
#     class Meta:
#         managed = False
#         db_table = 'project_associate'
# 
# 
# class ProjectChooseHits2(models.Model):
#     projectid = models.ForeignKey(Project, models.DO_NOTHING, db_column='projectid')
#     screenid = models.ForeignKey('ProjectScreen', models.DO_NOTHING, db_column='screenid')
#     choosehitsno = models.SmallIntegerField()
#     sampleid = models.ForeignKey('Sample', models.DO_NOTHING, db_column='sampleid')
#     src_sampleid = models.ForeignKey('Sample', models.DO_NOTHING, db_column='src_sampleid')
#     pp_plateid = models.ForeignKey(Plate, models.DO_NOTHING, db_column='pp_plateid')
#     row = models.CharField(max_length=1)
#     col = models.SmallIntegerField()
#     platetype = models.CharField(max_length=2)
# 
#     class Meta:
#         managed = False
#         db_table = 'project_choose_hits2'
# 
# 
# class ProjectChooseHits2Src(models.Model):
#     projectid = models.ForeignKey(Project, models.DO_NOTHING, db_column='projectid')
#     screenid = models.ForeignKey('ProjectScreen', models.DO_NOTHING, db_column='screenid')
#     choosehitsno = models.SmallIntegerField()
#     sampleid = models.ForeignKey('Sample', models.DO_NOTHING, db_column='sampleid')
#     comments = models.TextField(blank=True, null=True)
#     status = models.SmallIntegerField()
# 
#     class Meta:
#         managed = False
#         db_table = 'project_choose_hits2_src'
# 
# 
# class ProjectFlow(models.Model):
#     flowid = models.AutoField(primary_key=True)
#     projectid = models.ForeignKey(Project, models.DO_NOTHING, db_column='projectid')
#     stepno = models.IntegerField()
#     action = models.CharField(max_length=255)
#     actionon = models.IntegerField(blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'project_flow'
# 
# 
# class ProjectPlateList(models.Model):
#     projectid = models.ForeignKey(Project, models.DO_NOTHING, db_column='projectid')
#     screenid = models.ForeignKey('ProjectScreen', models.DO_NOTHING, db_column='screenid')
#     flowid = models.ForeignKey(ProjectFlow, models.DO_NOTHING, db_column='flowid')
#     stepno = models.SmallIntegerField()
#     plateid = models.ForeignKey(Plate, models.DO_NOTHING, db_column='plateid')
# 
#     class Meta:
#         managed = False
#         db_table = 'project_plate_list'
# 
# 
# class ProjectPs(models.Model):
#     project_ps_id = models.AutoField(primary_key=True)
#     projectid = models.IntegerField()
#     assayid = models.ForeignKey(Assay, models.DO_NOTHING, db_column='assayid')
# 
#     class Meta:
#         managed = False
#         db_table = 'project_ps'
#         unique_together = (('projectid', 'assayid'),)
# 
# 
# class ProjectSampleList(models.Model):
#     projectid = models.ForeignKey(Project, models.DO_NOTHING, db_column='projectid')
#     screenid = models.ForeignKey('ProjectScreen', models.DO_NOTHING, db_column='screenid')
#     flowid = models.ForeignKey(ProjectFlow, models.DO_NOTHING, db_column='flowid')
#     stepno = models.SmallIntegerField()
#     sampleid = models.ForeignKey('Sample', models.DO_NOTHING, db_column='sampleid')
#     sample_type = models.CharField(max_length=80)
#     sample_subtype = models.CharField(max_length=80)
#     src_sampleid = models.ForeignKey('Sample', models.DO_NOTHING, db_column='src_sampleid')
#     src_tplantid = models.ForeignKey('Tplant', models.DO_NOTHING, db_column='src_tplantid', blank=True, null=True)
#     src_aplantid = models.ForeignKey(Aplant, models.DO_NOTHING, db_column='src_aplantid', blank=True, null=True)
#     result = models.FloatField(blank=True, null=True)
#     error = models.FloatField(blank=True, null=True)
#     result_type = models.CharField(max_length=80)
#     plateprocdatasetid = models.ForeignKey(PlateProcdataset, models.DO_NOTHING, db_column='plateprocdatasetid', blank=True, null=True)
#     row = models.CharField(max_length=1)
#     col = models.SmallIntegerField()
#     pp_plateid = models.ForeignKey(Plate, models.DO_NOTHING, db_column='pp_plateid')
#     platetype = models.CharField(max_length=2)
#     conc = models.FloatField(blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'project_sample_list'
# 
# 
# class ProjectSampleRestriction(models.Model):
#     projectid = models.ForeignKey(Project, models.DO_NOTHING, db_column='projectid')
#     screenid = models.ForeignKey('ProjectScreen', models.DO_NOTHING, db_column='screenid')
#     stepno = models.SmallIntegerField()
#     sample_type = models.CharField(max_length=20)
#     sample_subtype = models.CharField(max_length=20, blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'project_sample_restriction'
#         unique_together = (('projectid', 'screenid', 'stepno'),)
# 
# 
# class ProjectScreen(models.Model):
#     screenid = models.AutoField(primary_key=True)
#     projectid = models.ForeignKey(Project, models.DO_NOTHING, db_column='projectid')
#     ps_screenid = models.ForeignKey('self', models.DO_NOTHING, db_column='ps_screenid', blank=True, null=True)
#     type = models.CharField(max_length=1)
#     assayid = models.ForeignKey(Assay, models.DO_NOTHING, db_column='assayid')
# #     deprecated_selection = models.SmallIntegerField(blank=True, null=True)
#     deprecated_orderby = models.CharField(max_length=1, blank=True, null=True)
#     deprecated_plate_criterion = models.CharField(max_length=255, blank=True, null=True)
#     complete_pct = models.FloatField()
# 
#     class Meta:
#         managed = False
#         db_table = 'project_screen'
# 
# 
# class ProjectSs(models.Model):
#     project_ps = models.ForeignKey(ProjectPs, models.DO_NOTHING)
#     assayid = models.ForeignKey(Assay, models.DO_NOTHING, db_column='assayid')
# 
#     class Meta:
#         managed = False
#         db_table = 'project_ss'
#         unique_together = (('project_ps', 'assayid'),)
# 
# 
# class Protocol(models.Model):
#     protocolid = models.AutoField(primary_key=True)
#     text = models.TextField(blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'protocol'
# 
# 
# class ResultType(models.Model):
#     result_typeid = models.AutoField(primary_key=True)
#     text = models.TextField(blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'result_type'
# 
# 
# class Run(models.Model):
#     runid = models.AutoField(primary_key=True)
#     assayid = models.ForeignKey(Assay, models.DO_NOTHING, db_column='assayid')
#     title = models.CharField(max_length=255)
#     folder = models.CharField(max_length=255, blank=True, null=True)
#     goal = models.TextField(blank=True, null=True)
#     automation = models.CharField(max_length=255, blank=True, null=True)
#     qcdata = models.CharField(max_length=255, blank=True, null=True)
#     operator = models.ForeignKey(People, models.DO_NOTHING, db_column='operator', blank=True, null=True)
#     evaluation = models.SmallIntegerField()
#     evaluation_comments = models.TextField(blank=True, null=True)
#     status = models.SmallIntegerField()
#     comments = models.TextField(blank=True, null=True)
#     init = models.CharField(max_length=20)
#     initdate = models.DateField()
#     edit = models.CharField(max_length=20)
#     editdate = models.DateField()
#     nreplicates = models.SmallIntegerField()
#     active = models.BooleanField()
#     platemapid = models.IntegerField()
#     run_data_source = models.SmallIntegerField(blank=True, null=True)
#     plateorigin = models.CharField(max_length=2, blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'run'
#         unique_together = (('assayid', 'title'),)
# 
# 
# class RunProcess(models.Model):
#     runprocessid = models.AutoField(primary_key=True)
#     runid = models.ForeignKey(Run, models.DO_NOTHING, db_column='runid')
#     title = models.CharField(max_length=255, blank=True, null=True)
#     notes = models.TextField(blank=True, null=True)
#     method = models.TextField(blank=True, null=True)
#     nresults = models.SmallIntegerField(blank=True, null=True)
#     normalized = models.BooleanField()
#     normalized_value = models.FloatField(blank=True, null=True)
#     join_replicates = models.BooleanField()
#     fitstarting = models.CharField(max_length=1024, blank=True, null=True)
#     filter = models.CharField(max_length=1024, blank=True, null=True)
#     init = models.CharField(max_length=20)
#     initdate = models.DateField()
# 
#     class Meta:
#         managed = False
#         db_table = 'run_process'
#         unique_together = (('title', 'runid'),)
# 
# 
# class Sample(models.Model):
#     sampleid = models.AutoField(primary_key=True)
#     deprecated_type = models.ForeignKey('SampleTypes', models.DO_NOTHING, db_column='deprecated_type', blank=True, null=True)
#     active = models.NullBooleanField()
#     type = models.CharField(max_length=20)
#     subtype = models.CharField(max_length=20)
# 
#     class Meta:
#         managed = False
#         db_table = 'sample'
# 
# 
# class SampleProcessing(models.Model):
#     sampleid = models.ForeignKey(Sample, models.DO_NOTHING, db_column='sampleid')
#     status = models.SmallIntegerField()
#     initial = models.FloatField(blank=True, null=True)
#     oven = models.FloatField(blank=True, null=True)
#     notes = models.TextField(blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'sample_processing'
# 
# 
# class SampleTracker(models.Model):
#     sampleid = models.ForeignKey(Sample, models.DO_NOTHING, db_column='sampleid')
#     freezer = models.SmallIntegerField()
#     bookcase = models.SmallIntegerField()
#     shelf = models.SmallIntegerField()
#     row = models.SmallIntegerField()
#     col = models.CharField(max_length=2)
#     location = models.CharField(unique=True, max_length=20, blank=True, null=True)
#     capcolor = models.SmallIntegerField()
#     init_volume = models.FloatField(blank=True, null=True)
#     curr_volume = models.FloatField(blank=True, null=True)
#     init_dry_mass = models.FloatField(blank=True, null=True)
#     conc = models.FloatField(blank=True, null=True)
#     od1 = models.FloatField(blank=True, null=True)
#     wave1 = models.FloatField(blank=True, null=True)
#     od2 = models.FloatField(blank=True, null=True)
#     wave2 = models.FloatField(blank=True, null=True)
#     appearance = models.TextField(blank=True, null=True)
#     notes = models.TextField(blank=True, null=True)
#     history = models.TextField(blank=True, null=True)
#     init = models.CharField(max_length=20)
#     initdate = models.DateField()
#     edit = models.CharField(max_length=20)
#     editdate = models.DateField()
#     deprecated_col_sortable = models.CharField(max_length=2, blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'sample_tracker'
# 
# 
# class SampleTypes(models.Model):
#     typeid = models.SmallIntegerField(primary_key=True)
#     tablename = models.CharField(max_length=255)
# 
#     class Meta:
#         managed = False
#         db_table = 'sample_types'
# 
# 
# class SummaryPlatesBySampletype(models.Model):
#     platetype = models.CharField(max_length=2)
#     sample_type = models.CharField(max_length=20)
#     sample_subtype = models.CharField(max_length=20)
#     plateid = models.ForeignKey(Plate, models.DO_NOTHING, db_column='plateid')
#     nsamples = models.SmallIntegerField()
# 
#     class Meta:
#         managed = False
#         db_table = 'summary_plates_by_sampletype'
# 
# 
# class SummaryTable(models.Model):
#     datestart = models.DateField()
#     dateperiod = models.CharField(max_length=255)
#     quantity = models.IntegerField()
#     tablename = models.CharField(max_length=255)
# 
#     class Meta:
#         managed = False
#         db_table = 'summary_table'
# 
# 
# class Target(models.Model):
#     targetid = models.AutoField(primary_key=True)
#     title = models.CharField(unique=True, max_length=255)
#     folder = models.CharField(unique=True, max_length=255)
#     disease = models.CharField(max_length=255, blank=True, null=True)
#     assay_format = models.IntegerField(blank=True, null=True)
#     principle = models.TextField(blank=True, null=True)
#     literature = models.TextField(blank=True, null=True)
#     client = models.CharField(max_length=255, blank=True, null=True)
#     status = models.SmallIntegerField()
#     comments = models.TextField(blank=True, null=True)
#     init = models.CharField(max_length=20)
#     initdate = models.DateField()
#     edit = models.CharField(max_length=20)
#     editdate = models.DateField()
#     active = models.BooleanField()
#     title_short = models.CharField(max_length=255)
# 
#     class Meta:
#         managed = False
#         db_table = 'target'
# 
# 
# class TlcChemicalClasses(models.Model):
#     eluent_developer = models.SmallIntegerField(unique=True)
#     result_types = models.TextField(blank=True, null=True)  # This field type is a guess.
#     chemclassids = models.TextField(blank=True, null=True)  # This field type is a guess.
# 
#     class Meta:
#         managed = False
#         db_table = 'tlc_chemical_classes'
# 
# 
# class Tlcdata(models.Model):
#     tlcplateid = models.ForeignKey('Tlcplate', models.DO_NOTHING, db_column='tlcplateid', blank=True, null=True)
#     sampleid = models.ForeignKey(Sample, models.DO_NOTHING, db_column='sampleid', blank=True, null=True)
#     quantity = models.FloatField(blank=True, null=True)
#     lane = models.SmallIntegerField(blank=True, null=True)
#     col = models.SmallIntegerField(blank=True, null=True)
#     chemclassid = models.SmallIntegerField(blank=True, null=True)
#     result = models.NullBooleanField()
#     tlc_compoundtype = models.SmallIntegerField(blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'tlcdata'
# 
# 
# class Tlcplate(models.Model):
#     tlcplateid = models.AutoField(primary_key=True)
#     nlanes = models.SmallIntegerField(blank=True, null=True)
#     analdate = models.DateField(blank=True, null=True)
#     opeid = models.ForeignKey(People, models.DO_NOTHING, db_column='opeid', blank=True, null=True)
#     imagefile = models.CharField(max_length=80, blank=True, null=True)
#     eluent_developer = models.SmallIntegerField(blank=True, null=True)
#     notes = models.TextField(blank=True, null=True)
#     active = models.SmallIntegerField(blank=True, null=True)
#     init = models.CharField(max_length=20)
#     initdate = models.DateField()
#     edit = models.CharField(max_length=20)
#     editdate = models.DateField()
# 
#     class Meta:
#         managed = False
#         db_table = 'tlcplate'
# 
# 
# class Tplant(models.Model):
#     tplantid = models.AutoField(primary_key=True)
#     formnum = models.SmallIntegerField(blank=True, null=True)
#     coldate = models.DateField(blank=True, null=True)
#     deprecated_latdeg = models.SmallIntegerField(blank=True, null=True)
#     deprecated_latmin = models.FloatField(blank=True, null=True)
#     deprecated_londeg = models.SmallIntegerField(blank=True, null=True)
#     deprecated_lonmin = models.FloatField(blank=True, null=True)
#     altitude = models.FloatField(blank=True, null=True)
#     mapinfo = models.CharField(max_length=255, blank=True, null=True)
#     soil = models.TextField(blank=True, null=True)  # This field type is a guess.
#     vegetation = models.SmallIntegerField(blank=True, null=True)
#     family = models.CharField(max_length=80, blank=True, null=True)
#     genus = models.CharField(max_length=80, blank=True, null=True)
#     species = models.CharField(max_length=80, blank=True, null=True)
#     common = models.CharField(max_length=80, blank=True, null=True)
#     author = models.CharField(max_length=80, blank=True, null=True)
#     light = models.SmallIntegerField(blank=True, null=True)
#     abund = models.SmallIntegerField(blank=True, null=True)
#     height = models.FloatField(blank=True, null=True)
#     diameter = models.FloatField(blank=True, null=True)
#     habit = models.SmallIntegerField(blank=True, null=True)
#     photonum = models.TextField(blank=True, null=True)  # This field type is a guess.
#     numindiv = models.SmallIntegerField(blank=True, null=True)
#     ethnologic = models.TextField(blank=True, null=True)
#     notes = models.TextField(blank=True, null=True)
#     identid = models.ForeignKey(People, models.DO_NOTHING, db_column='identid', blank=True, null=True)
#     herbname = models.CharField(max_length=80, blank=True, null=True)
#     herbdate = models.DateField(blank=True, null=True)
#     herbnum = models.CharField(max_length=80, blank=True, null=True)
#     active = models.BooleanField()
#     remove = models.BooleanField()
#     init = models.CharField(max_length=20)
#     initdate = models.DateField()
#     edit = models.CharField(max_length=20)
#     editdate = models.DateField()
#     lat = models.FloatField(blank=True, null=True)
#     lon = models.FloatField(blank=True, null=True)
# 
#     class Meta:
#         managed = False
#         db_table = 'tplant'
# 
# 
# class Tplantorgan(models.Model):
#     sampleid = models.ForeignKey(Sample, models.DO_NOTHING, db_column='sampleid')
#     expedid = models.ForeignKey(Exped, models.DO_NOTHING, db_column='expedid')
#     tplantid = models.ForeignKey(Tplant, models.DO_NOTHING, db_column='tplantid')
#     organ = models.CharField(max_length=20)
#     color = models.CharField(max_length=20, blank=True, null=True)
#     smell = models.CharField(max_length=20, blank=True, null=True)
#     weight = models.FloatField(blank=True, null=True)
#     notes = models.TextField(blank=True, null=True)
#     active = models.BooleanField()
#     remove = models.BooleanField()
#     init = models.CharField(max_length=20)
#     initdate = models.DateField()
#     edit = models.CharField(max_length=20)
#     editdate = models.DateField()
# 
#     class Meta:
#         managed = False
#         db_table = 'tplantorgan'
