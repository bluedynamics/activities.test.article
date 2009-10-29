# -*- coding: utf-8 -*-
#
# Copyright 2009: Johannes Raggam, BlueDynamics Alliance
#                 http://bluedynamics.com
# GNU Lesser General Public License Version 2 or later

__author__ = """Johannes Raggam <johannes@raggam.co.at>"""
__docformat__ = 'plaintext'

import activities.metamodel as mm

profile = mm.Profile('activities.test.article')
#profile['create-template'] = mm.Stereotype()
#profile['write-article'] = mm.Stereotype()
#profile['merge-article'] = mm.Stereotype()

# PROFILE AS METAMODEL
model = mm.Package('collaborative-article')
model[profile.__name__] = profile
model['main'] = mm.Activity()
act = model['main']

act['start'] = mm.InitialNode()

act['a'] = mm.OpaqueAction()
act['a']['create-template'] = mm.Stereotype(profile=profile)

act['b'] = mm.ForkNode()

act['c'] = mm.OpaqueAction()
act['c']['write-article'] = mm.Stereotype(profile=profile)

act['d'] = mm.OpaqueAction()
act['d']['write-article'] = mm.Stereotype(profile=profile)

act['e'] = mm.OpaqueAction()
act['e']['merge-article'] = mm.Stereotype(profile=profile)

act['end'] = mm.ActivityFinalNode()

act['1'] = mm.ActivityEdge(source=act['start'], target=act['a'])
act['2'] = mm.ActivityEdge(source=act['a'], target=act['b'])
act['3'] = mm.ActivityEdge(source=act['b'], target=act['c'])
act['4'] = mm.ActivityEdge(source=act['b'], target=act['d'])
act['5'] = mm.ActivityEdge(source=act['c'], target=act['e'])
act['6'] = mm.ActivityEdge(source=act['d'], target=act['e'])
act['7'] = mm.ActivityEdge(source=act['e'], target=act['end'])

mm.validate(model)


# CREATING PROFILE IN-PLACE
"""
model = Package('collaborative-article')
model['activities.test.article'] = Profile()
model['main'] = Activity(context="A dummy context")
act = model['main']

act['start'] = InitialNode()

act['a'] = OpaqueAction()
act['a']['create-template'] = Stereotype()
act['a']['create-template']['template_path'] = \
     TaggedValue(value='data/template.txt')

act['b'] = ForkNode()

act['c'] = OpaqueAction()
act['c']['write-article'] = Stereotype()

act['d'] = OpaqueAction()
act['d']['write-article'] = Stereotype()

act['e'] = OpaqueAction()
act['e']['merge-article'] = Stereotype()

act['end'] = ActivityFinalNode()

act['1'] = ControlFlow(source=act['start'], target=act['a'])
# TODO: ObjectFlow's may not have actions at either end (they want Pins).
# do someting.
act['2'] = ControlFlow(source=act['a'], target=act['b'])
act['3'] = ControlFlow(source=act['b'], target=act['c'])
act['4'] = ControlFlow(source=act['b'], target=act['d'])
act['5'] = ControlFlow(source=act['c'], target=act['e'])
act['6'] = ControlFlow(source=act['d'], target=act['e'])
act['7'] = ControlFlow(source=act['e'], target=act['end'])

act.validate()
"""