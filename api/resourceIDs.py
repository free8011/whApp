# coding: utf-8
# 2014-10-03 update ids

class SYSTEM_TYPE:
    SYS_WINDOWS = 1
    SYS_OSX = 2
    SYS_LINUX = 3


class WH_CASE_IDS:
    WH_COMPANY = 10009
    WH_PROJECT = 10010
    WH_SHOT    = 10011
    WH_ASSET   = 10012
    WH_SEQUENCE = 10013
    WH_SHOT_HIST = 10014
    WH_ASSET_HIST = 10015

    WH_MEMBER = 10016
    WH_TASK = 10017
    WH_PRJ_PATH = 10018

    WH_TASK_LIST = 10019

    WH_PUBLISH_ASSET = 10020
    WH_PUBLISH_SHOT = 10021
    WH_RECORD_ASSET = 10022

class JOB_TYPE_IDS:
    IDS_JOB_DESIGN  =  2101
    IDS_JOB_MODELING = 2102
    IDS_JOB_SHADING	= 2103
    IDS_JOB_RENDERING = 2104
    IDS_JOB_CODING	= 2105


class SW_TYPE_IDS:  
    IDS_SW_MAYA = 1010
    IDS_SW_MAX = 1011
    IDS_SW_XSI = 1012
    IDS_SW_NUKE = 1013


class MAYA_VERSION_IDS:
    IDS_MAYA_2012 =	1111
    IDS_MAYA_2013 =	1112
    IDS_MAYA_2014 = 1113
    IDS_MAYA_2015 = 1114


class XSI_VERSION_IDS:
    IDS_XSI_2012 = 2112
    IDS_XSI_2013 = 2113
    IDS_XSI_2014 = 2114
    IDS_XSI_2015 = 2115

class NUKE_VERSION_IDS:
    IDS_NUKE_6 = 3111
    IDS_NUKE_7 = 3112
    IDS_NUKE_8 = 3113
    IDS_NUKE_9 = 3114

class MAX_VERSION_IDS:
    IDS_MAX_2012 = 4112
    IDS_MAX_2013 = 4113
    IDS_MAX_2014 = 4114
    IDS_MAX_2015 = 4115

class WH_PROJECT_MODE:
    IDS_SHOT_MODE = 5001
    IDS_ASSET_MODE = 5002

class WH_PRJ:
    count = 0

class WH_PATH_MAP:
    FILESERVERHOME  = 'FILESERVERHOME' #ProjectHome
    COMPANY         = 'COMPANY' #Company
    PROJECTID       = 'PROJECTID' #Project
    ASSETID         = 'ASSETID' #AssetPrefix
    SEQUENCEID      = 'SEQUENCEID' #SeqName
    SHOTID          = 'SHOTID' #ShotName
    VERSIONNUMBER   = 'VERSIONNUMBER'
    PUBLISHER       = 'USERID' #UserID
    TASKTYPEID      = 'TASKTYPEID' #TaskType
    DATE            = 'DATE'
    PDATATYPE       = 'PDATATYPE'
    CATEGORY        = 'CATEGORY'
