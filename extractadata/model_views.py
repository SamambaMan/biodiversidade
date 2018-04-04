# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class VActiveExpedTplant(models.Model):
    expedid = models.IntegerField(blank=True, null=True)
    tplantid = models.IntegerField(blank=True, null=True)
    family = models.CharField(max_length=80, blank=True, null=True)
    genus = models.CharField(max_length=80, blank=True, null=True)
    species = models.CharField(max_length=80, blank=True, null=True)
    common = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'v_active_exped_tplant'


class VAdminLog(models.Model):
    logid = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    userid = models.IntegerField(blank=True, null=True)
    event = models.CharField(max_length=255, blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
    ip = models.GenericIPAddressField(blank=True, null=True)
    comments = models.CharField(max_length=1024, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'v_admin_log'


class VAdminPrefs(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    fullname = models.CharField(max_length=255, blank=True, null=True)
    active = models.NullBooleanField()
    id = models.SmallIntegerField(primary_key=True)
    style_box = models.CharField(max_length=40, blank=True, null=True)
    style = models.CharField(max_length=40, blank=True, null=True)
    lang = models.CharField(max_length=2, blank=True, null=True)
    font = models.CharField(max_length=40, blank=True, null=True)
    fontsize = models.CharField(max_length=6, blank=True, null=True)
    mainwidth = models.SmallIntegerField(blank=True, null=True)
    icon_view = models.SmallIntegerField(blank=True, null=True)
    icon_logo = models.SmallIntegerField(blank=True, null=True)
    verb = models.SmallIntegerField(blank=True, null=True)
    debug = models.SmallIntegerField(blank=True, null=True)
    firsttab = models.SmallIntegerField(blank=True, null=True)
    showbanner = models.NullBooleanField()
    listview1 = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'v_admin_prefs'


class VAssay(models.Model):
    ttitle = models.CharField(max_length=255, blank=True, null=True)
    ttitle_short = models.CharField(max_length=255, blank=True, null=True)
    assayid = models.IntegerField(blank=True, null=True)
    targetid = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    folder = models.CharField(max_length=255, blank=True, null=True)
    detection_meth = models.IntegerField(blank=True, null=True)
    data_format = models.IntegerField(blank=True, null=True)
    substrate = models.CharField(max_length=255, blank=True, null=True)
    ref_compound = models.CharField(max_length=255, blank=True, null=True)
    mode_of_action = models.IntegerField(blank=True, null=True)
    sopfile = models.CharField(max_length=255, blank=True, null=True)
    developer = models.CharField(max_length=255, blank=True, null=True)
    validator = models.CharField(max_length=255, blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    init = models.CharField(max_length=20, blank=True, null=True)
    initdate = models.DateField(blank=True, null=True)
    edit = models.CharField(max_length=20, blank=True, null=True)
    editdate = models.DateField(blank=True, null=True)
    active = models.NullBooleanField()
    title_short = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'v_assay'


class VCcaResults(models.Model):
    cca_resultid = models.IntegerField(blank=True, null=True)
    sampleid = models.IntegerField(blank=True, null=True)
    chemclassid = models.SmallIntegerField(blank=True, null=True)
    classname = models.CharField(max_length=80, blank=True, null=True)
    ref_table = models.CharField(max_length=20, blank=True, null=True)
    ref_fkey = models.CharField(max_length=20, blank=True, null=True)
    ref_id = models.IntegerField(blank=True, null=True)
    bresult = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'v_cca_results'


class VCompound(models.Model):
    sampleid = models.IntegerField(primary_key=True)
    origin_sampleid = models.IntegerField(blank=True, null=True)
    opeid = models.IntegerField(blank=True, null=True)
    isolationdate = models.DateField(blank=True, null=True)
    depid = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    active = models.NullBooleanField()
    remove = models.NullBooleanField()
    purity_pct = models.SmallIntegerField(blank=True, null=True)
    purity_notes = models.TextField(blank=True, null=True)
    quantity = models.FloatField(blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)
    solvent = models.CharField(max_length=255, blank=True, null=True)
    mw = models.FloatField(blank=True, null=True)
    formula = models.CharField(max_length=255, blank=True, null=True)
    name_common = models.CharField(max_length=255, blank=True, null=True)
    name_iupac = models.CharField(max_length=255, blank=True, null=True)
    smiles = models.CharField(max_length=255, blank=True, null=True)
    init = models.CharField(max_length=20, blank=True, null=True)
    initdate = models.DateField(blank=True, null=True)
    edit = models.CharField(max_length=20, blank=True, null=True)
    editdate = models.DateField(blank=True, null=True)
    operator = models.CharField(max_length=80, blank=True, null=True)
    depositor = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'v_compound'


class VInactiveExpedTplant(models.Model):
    expedid = models.IntegerField(blank=True, null=True)
    tplantid = models.IntegerField(blank=True, null=True)
    family = models.CharField(max_length=80, blank=True, null=True)
    genus = models.CharField(max_length=80, blank=True, null=True)
    species = models.CharField(max_length=80, blank=True, null=True)
    common = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'v_inactive_exped_tplant'


class VPlateAssay(models.Model):
    plateid = models.IntegerField(blank=True, null=True)
    platetype = models.CharField(max_length=2, blank=True, null=True)
    platemap = models.CharField(max_length=255, blank=True, null=True)
    platemapid = models.IntegerField(blank=True, null=True)
    solvent = models.CharField(max_length=255, blank=True, null=True)
    origin = models.CharField(max_length=2, blank=True, null=True)
    active = models.SmallIntegerField(blank=True, null=True)
    runid = models.IntegerField(blank=True, null=True)
    runtitle = models.CharField(max_length=255, blank=True, null=True)
    ractive = models.NullBooleanField()
    rstatus = models.SmallIntegerField(blank=True, null=True)
    paorigin = models.CharField(max_length=2, blank=True, null=True)
    origin_plateid = models.IntegerField(blank=True, null=True)
    origin_volume = models.FloatField(blank=True, null=True)
    volume_init = models.FloatField(blank=True, null=True)
    init = models.CharField(max_length=20, blank=True, null=True)
    initdate = models.DateField(blank=True, null=True)
    edit = models.CharField(max_length=20, blank=True, null=True)
    editdate = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'v_plate_assay'


class VPlateDilution(models.Model):
    plateid = models.IntegerField(blank=True, null=True)
    platetype = models.CharField(max_length=2, blank=True, null=True)
    platemap = models.CharField(max_length=255, blank=True, null=True)
    platemapid = models.IntegerField(blank=True, null=True)
    solvent = models.CharField(max_length=255, blank=True, null=True)
    origin = models.CharField(max_length=2, blank=True, null=True)
    active = models.SmallIntegerField(blank=True, null=True)
    mo_plateid = models.IntegerField(blank=True, null=True)
    mo_volume = models.FloatField(blank=True, null=True)
    is_diluted = models.NullBooleanField()
    di_date = models.DateField(blank=True, null=True)
    expire_date = models.DateField(blank=True, null=True)
    volume_dilution = models.FloatField(blank=True, null=True)
    volume_current = models.FloatField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    init = models.CharField(max_length=20, blank=True, null=True)
    initdate = models.DateField(blank=True, null=True)
    edit = models.CharField(max_length=20, blank=True, null=True)
    editdate = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'v_plate_dilution'


class VPlateDiscovery(models.Model):
    plateid = models.IntegerField(blank=True, null=True)
    platetype = models.CharField(max_length=2, blank=True, null=True)
    platemap = models.CharField(max_length=255, blank=True, null=True)
    platemapid = models.IntegerField(blank=True, null=True)
    solvent = models.CharField(max_length=255, blank=True, null=True)
    origin = models.CharField(max_length=2, blank=True, null=True)
    active = models.SmallIntegerField(blank=True, null=True)
    tatitle = models.TextField(blank=True, null=True)
    assayid = models.IntegerField(blank=True, null=True)
    creation_date = models.DateField(blank=True, null=True)
    expire_date = models.DateField(blank=True, null=True)
    volume_current = models.FloatField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    init = models.CharField(max_length=20, blank=True, null=True)
    initdate = models.DateField(blank=True, null=True)
    edit = models.CharField(max_length=20, blank=True, null=True)
    editdate = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'v_plate_discovery'


class VPlateMother(models.Model):
    plateid = models.IntegerField(blank=True, null=True)
    platetype = models.CharField(max_length=2, blank=True, null=True)
    platemap = models.CharField(max_length=255, blank=True, null=True)
    platemapid = models.IntegerField(blank=True, null=True)
    solvent = models.CharField(max_length=255, blank=True, null=True)
    origin = models.CharField(max_length=2, blank=True, null=True)
    active = models.SmallIntegerField(blank=True, null=True)
    volume_init = models.FloatField(blank=True, null=True)
    volume_current = models.FloatField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    init = models.CharField(max_length=20, blank=True, null=True)
    initdate = models.DateField(blank=True, null=True)
    edit = models.CharField(max_length=20, blank=True, null=True)
    editdate = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'v_plate_mother'


class VPlateTannin(models.Model):
    plateid = models.IntegerField(blank=True, null=True)
    platetype = models.CharField(max_length=2, blank=True, null=True)
    platemap = models.CharField(max_length=255, blank=True, null=True)
    platemapid = models.IntegerField(blank=True, null=True)
    solvent = models.CharField(max_length=255, blank=True, null=True)
    origin = models.CharField(max_length=2, blank=True, null=True)
    active = models.SmallIntegerField(blank=True, null=True)
    analdate = models.DateField(blank=True, null=True)
    opeid = models.IntegerField(blank=True, null=True)
    last = models.CharField(max_length=80, blank=True, null=True)
    first = models.CharField(max_length=80, blank=True, null=True)
    imagefile = models.CharField(max_length=80, blank=True, null=True)
    scanfile = models.CharField(max_length=80, blank=True, null=True)
    dilution = models.FloatField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    init = models.CharField(max_length=20, blank=True, null=True)
    initdate = models.DateField(blank=True, null=True)
    edit = models.CharField(max_length=20, blank=True, null=True)
    editdate = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'v_plate_tannin'


class VRun(models.Model):
    ttitle = models.CharField(max_length=255, blank=True, null=True)
    ttitle_short = models.CharField(max_length=255, blank=True, null=True)
    atitle = models.CharField(max_length=255, blank=True, null=True)
    atitle_short = models.CharField(max_length=255, blank=True, null=True)
    runid = models.IntegerField(blank=True, null=True)
    assayid = models.IntegerField(blank=True, null=True)
    targetid = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    run_data_source = models.SmallIntegerField(blank=True, null=True)
    folder = models.CharField(max_length=255, blank=True, null=True)
    platemap = models.CharField(max_length=255, blank=True, null=True)
    platemapid = models.IntegerField(blank=True, null=True)
    plateorigin = models.CharField(max_length=2, blank=True, null=True)
    nreplicates = models.SmallIntegerField(blank=True, null=True)
    operator = models.IntegerField(blank=True, null=True)
    goal = models.TextField(blank=True, null=True)
    automation = models.CharField(max_length=255, blank=True, null=True)
    qcdata = models.CharField(max_length=255, blank=True, null=True)
    evaluation = models.SmallIntegerField(blank=True, null=True)
    evaluation_comments = models.TextField(blank=True, null=True)
    active = models.NullBooleanField()
    status = models.SmallIntegerField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    init = models.CharField(max_length=20, blank=True, null=True)
    initdate = models.DateField(blank=True, null=True)
    edit = models.CharField(max_length=20, blank=True, null=True)
    editdate = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'v_run'


class VRunProcess(models.Model):
    runprocessid = models.IntegerField(blank=True, null=True)
    runid = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    method = models.TextField(blank=True, null=True)
    nresults = models.SmallIntegerField(blank=True, null=True)
    normalized = models.NullBooleanField()
    normalized_value = models.FloatField(blank=True, null=True)
    join_replicates = models.NullBooleanField()
    init = models.CharField(max_length=20, blank=True, null=True)
    initdate = models.DateField(blank=True, null=True)
    plateprocdatasetid = models.IntegerField(blank=True, null=True)
    row = models.CharField(max_length=1, blank=True, null=True)
    col = models.SmallIntegerField(blank=True, null=True)
    result = models.FloatField(blank=True, null=True)
    error = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'v_run_process'


class VTarget(models.Model):
    targetid = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    folder = models.CharField(max_length=255, blank=True, null=True)
    disease = models.CharField(max_length=255, blank=True, null=True)
    assay_format = models.IntegerField(blank=True, null=True)
    principle = models.TextField(blank=True, null=True)
    literature = models.TextField(blank=True, null=True)
    client = models.CharField(max_length=255, blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    init = models.CharField(max_length=20, blank=True, null=True)
    initdate = models.DateField(blank=True, null=True)
    edit = models.CharField(max_length=20, blank=True, null=True)
    editdate = models.DateField(blank=True, null=True)
    active = models.NullBooleanField()
    title_short = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'v_target'


class VTargetAssay(models.Model):
    targetid = models.IntegerField(blank=True, null=True)
    ttitle = models.CharField(max_length=255, blank=True, null=True)
    ttitle_short = models.CharField(max_length=255, blank=True, null=True)
    tfolder = models.CharField(max_length=255, blank=True, null=True)
    assay_format = models.IntegerField(blank=True, null=True)
    tactive = models.NullBooleanField()
    tstatus = models.SmallIntegerField(blank=True, null=True)
    assayid = models.IntegerField(blank=True, null=True)
    atitle = models.CharField(max_length=255, blank=True, null=True)
    atitle_short = models.CharField(max_length=255, blank=True, null=True)
    afolder = models.CharField(max_length=255, blank=True, null=True)
    detection_meth = models.IntegerField(blank=True, null=True)
    sopfile = models.CharField(max_length=255, blank=True, null=True)
    data_format = models.IntegerField(blank=True, null=True)
    aactive = models.NullBooleanField()
    astatus = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'v_target_assay'


class VTargetAssayRun(models.Model):
    targetid = models.IntegerField(blank=True, null=True)
    ttitle = models.CharField(max_length=255, blank=True, null=True)
    ttitle_short = models.CharField(max_length=255, blank=True, null=True)
    tfolder = models.CharField(max_length=255, blank=True, null=True)
    assay_format = models.IntegerField(blank=True, null=True)
    tactive = models.NullBooleanField()
    tstatus = models.SmallIntegerField(blank=True, null=True)
    assayid = models.IntegerField(blank=True, null=True)
    atitle = models.CharField(max_length=255, blank=True, null=True)
    atitle_short = models.CharField(max_length=255, blank=True, null=True)
    afolder = models.CharField(max_length=255, blank=True, null=True)
    detection_meth = models.IntegerField(blank=True, null=True)
    data_format = models.IntegerField(blank=True, null=True)
    sopfile = models.CharField(max_length=255, blank=True, null=True)
    aactive = models.NullBooleanField()
    astatus = models.SmallIntegerField(blank=True, null=True)
    runid = models.IntegerField(blank=True, null=True)
    run_data_source = models.SmallIntegerField(blank=True, null=True)
    rtitle = models.CharField(max_length=255, blank=True, null=True)
    rfolder = models.CharField(max_length=255, blank=True, null=True)
    platemapid = models.IntegerField(blank=True, null=True)
    plateorigin = models.CharField(max_length=2, blank=True, null=True)
    nreplicates = models.SmallIntegerField(blank=True, null=True)
    automation = models.CharField(max_length=255, blank=True, null=True)
    qcdata = models.CharField(max_length=255, blank=True, null=True)
    evaluation = models.SmallIntegerField(blank=True, null=True)
    evaluation_comments = models.TextField(blank=True, null=True)
    ractive = models.NullBooleanField()
    rstatus = models.SmallIntegerField(blank=True, null=True)
    rcomments = models.TextField(blank=True, null=True)
    opeid = models.IntegerField(blank=True, null=True)
    rfirst_ope = models.CharField(max_length=80, blank=True, null=True)
    rlast_ope = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'v_target_assay_run'


class VTlcplate(models.Model):
    tlcplateid = models.IntegerField(blank=True, null=True)
    opeid = models.IntegerField(blank=True, null=True)
    first = models.CharField(max_length=80, blank=True, null=True)
    last = models.CharField(max_length=80, blank=True, null=True)
    nlanes = models.SmallIntegerField(blank=True, null=True)
    eluent_developer = models.SmallIntegerField(blank=True, null=True)
    imagefile = models.CharField(max_length=80, blank=True, null=True)
    analdate = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    active = models.SmallIntegerField(blank=True, null=True)
    init = models.CharField(max_length=20, blank=True, null=True)
    initdate = models.DateField(blank=True, null=True)
    edit = models.CharField(max_length=20, blank=True, null=True)
    editdate = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'v_tlcplate'
