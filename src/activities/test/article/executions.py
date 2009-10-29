# -*- coding: utf-8 -*-
#
# Copyright 2009: Johannes Raggam, BlueDynamics Alliance
#                 http://bluedynamics.com
# GNU Lesser General Public License Version 2 or later

__author__ = """Johannes Raggam <johannes@raggam.co.at>"""
__docformat__ = 'plaintext'

from activities.runtime.interfaces import IExecution
from zope.interface import implements
from zope.component import getGlobalSiteManager
import sys
from copy import copy

class Article(object):
    title = None
    body = None

class CreateTemplate(object):
    implements(IExecution)
    name = "create-template"

    def __call__(self, action_info, tgv_dict, data):
        data['template'] = Article()
        # here, data will be passed through, keeping all original items
        return data

class WriteArticle(object):
    implements(IExecution)
    name = "write-article"

    def __call__(self, action_info, tgv_dict, data):
        article = copy(data['template'])
        article.title = sys.stdin.readline()[:-1] # whole line without "\n"
        article.body = sys.stdin.readline()[:-1] # whole line without "\n"
        # here, a new object is returned which will be used as token's data
        # the token object will put it in it's data dictionary with a uuid as
        # key
        return article

class MergeArticle(object):
    implements(IExecution)
    name = "merge-article"

    def __call__(self, action_info, tgv_dict, data):
        merged_article = []
        for item in data.itervalues():
            merged_article.append(item)
        # here, a dict is returned and the key will be preserved because the
        # token object just creates auto-keys when no dict is passed in.
        return {'merged_article': merged_article}


gsm = getGlobalSiteManager()
gsm.registerUtility(component=CreateTemplate(), name=CreateTemplate.name)
gsm.registerUtility(component=WriteArticle(), name=WriteArticle.name)
gsm.registerUtility(component=MergeArticle(), name=MergeArticle.name)


#