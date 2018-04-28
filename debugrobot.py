#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import inspect
from robot.run import RobotFramework

path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.append(path)
PYTHONPATH = os.path.realpath('%s/../' % path)
sys.path.append(PYTHONPATH)

__author__ = 'huaiyuan.gu@gmail.com'

"""
debug robot test case
"""

if __name__ == '__main__':

    import os
    import sys
    import inspect

    base_path = os.path.realpath(os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))))
    test_path = report_path = base_path
    sys.path.append(base_path)
    sys.path.append(test_path)

    root = base_path
    rb = os.path.join(test_path, 'smoketest.robot')

    xmlfile = os.path.join(report_path, 'output.xml')
    logfile = os.path.join(report_path, 'log.html')
    rptfile = os.path.join(report_path, 'report.html')

    bot = RobotFramework()
    bot.main([rb], output=xmlfile, log=None, report=None, include=['debug'])

    from robot.rebot import Rebot
    bot = Rebot()
    try:
        bot.main([xmlfile], log=logfile, report=rptfile, include=['debug'])
    except Exception as e:
        print ('=' * 10 + ' Robot report exception %s' % '=' * 10)
        print (e)