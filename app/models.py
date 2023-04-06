import os
import uuid
import logging

from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _


########################
# App -> Models Logger #
########################

# ------- Configuring Logging File -------- #

# Logger For Log File
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Log File Logging Format
formatter = logging.Formatter("%(asctime)s:%(levelname)s::%(message)s")

# Create Log Folder and File
log_folder_name = "app/logs"
log_file_name = "models.log"
os.makedirs(log_folder_name, exist_ok=True)
log_file_path = f"{log_folder_name}/{log_file_name}"

# Log File Handler
Log_File_Handler = logging.FileHandler(log_file_path)
Log_File_Handler.setLevel(logging.DEBUG)
Log_File_Handler.setFormatter(formatter)

# Stream Handlers
Stream_Handler = logging.StreamHandler()

# Adding The Handlers
logger.addHandler(Log_File_Handler)
logger.addHandler(Stream_Handler)

# Log On START 
logger.debug("")
logger.debug("="*100)
logger.info("app App -> Models.py :: Logging Active")
logger.debug("")


class PollingUnitsModel(models.Model):

    result_id = models.IntegerField(primary_key=True)
    polling_unit_uniqueid = models.IntegerField()
    party_abbreviation = models.CharField(max_length=10, blank=False, null=False, default="Not Set")
    party_score = models.IntegerField()
    entered_by_user = models.CharField(max_length=100, blank=True, null=True, default="Bincom")
    date_entered = models.DateTimeField(default=timezone.now)
    user_ip_address = models.GenericIPAddressField()

    # Model metadata
    class Meta:
        db_table = 'announced_pu_results'


class LGA_Model(models.Model):

    uniqueid = models.IntegerField()
    lga_id = models.IntegerField()
    lga_name = models.CharField(null=False,blank=False, max_length=50)
    state_id = models.IntegerField()
    lga_description = models.TextField(null=False,blank=False,default="Bincom")
    entered_by_user = models.CharField(max_length=100, blank=True, null=True, default="Bincom")
    date_entered = models.DateTimeField(default=timezone.now)
    user_ip_address = models.GenericIPAddressField()

    # Model metadata
    class Meta:
        db_table = "lga"


class PollingUnitsInfoModel(models.Model):

    uniqueid = models.IntegerField(primary_key=True)
    polling_unit_id = models.IntegerField()
    ward_id = models.IntegerField()
    lga_id = models.IntegerField()
    uniquewardid = models.IntegerField()
    polling_unit_number = models.CharField(null=True, blank=True,max_length=50)
    polling_unit_name = models.CharField(null=True, blank=True,max_length=50)
    polling_unit_description = models.CharField(null=True, blank=True,max_length=50)
    lat = models.FloatField()
    long = models.FloatField()
    entered_by_user = models.CharField(max_length=100, blank=True, null=True, default="Bincom")
    date_entered = models.DateTimeField(default=timezone.now)
    user_ip_address = models.GenericIPAddressField()

    # Model metadata
    class Meta:
        db_table = 'polling_unit'


class Party(models.Model):

    partyid = models.CharField(null=False, blank=False, max_length=50)
    partyname = models.CharField(null=False, blank=False, max_length=50)
    
    # Model metadata
    class Meta:
        db_table = 'party'


class Ward(models.Model):

    unique_id = models.IntegerField()
    ward_id = models.IntegerField()
    ward_name = models.CharField(blank=False, null=False, max_length=100)
    lga_id = models.IntegerField()
    ward_description = models.CharField(null=True, blank=True,max_length=50)
    entered_by_user = models.CharField(max_length=100, blank=True, null=True, default="Bincom")
    date_entered = models.DateTimeField(default=timezone.now)
    user_ip_address = models.GenericIPAddressField()

    class Meta:
        db_table = "ward"
