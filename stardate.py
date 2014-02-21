#!/usr/bin/env python
#
# Author: Rahul Anand <et@eternal-thinker.com>
#         2014-02-21, stardate[-28]( <date> 6.00 pm 30 secs)            
#
# Description: 
#   Convert date formats to Stardates
#   Uses Stardate versions in Star Trek FAQ, as adopted by Google Calender 
#
# Python version: 2.7
#####################################################################################
#
# Based on the following work:
#
# stardate: convert between date formats
# by Andrew Main <zefram@fysh.org>
# 1997-12-26, stardate [-30]0458.96
#
# Stardate code is based on version 1 of the Stardates in Star Trek FAQ.
#####################################################################################

import time

class Stardate():

    # The length of one quadcent year, 12622780800 / 400 == 31556952 seconds. 
    QCYEAR = 31556952
    STDYEAR = 31536000

    # Definitions to help with leap years. */
    nrmdays = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
    lyrdays = [ 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]

    def jleapyear(self, y):
        return not y % 4

    def gleapyear(self, y):
        return (not y % 4) and (y % 100 or not y % 400)

    def jdays(self, y):
        return lyrdays if jleapyear(y) else nrmdays

    def gdays(self, y):
        return lyrdays if gleapyear(y) else nrmdays

    def xdays(self, gp, y):
        return lyrdays if (gleapyear(y) if gp else jleapyear(y)) else nrmdays

    #define jleapyear(y) ( !((y)%4L) )
    #define gleapyear(y) ( !((y)%4L) && ( ((y)%100L) || !((y)%400L) ) )
    #define jdays(y) (jleapyear(y) ? lyrdays : nrmdays)
    #define gdays(y) (gleapyear(y) ? lyrdays : nrmdays)
    #define xdays(gp, y) ( ((gp) ? gleapyear(y) : jleapyear(y))    ? lyrdays : nrmdays)

    # /* The date 0323-01-01 (0323*01*01) is 117609 days after the internal   *
    # * epoch, 0001=01=01 (0000-12-30).  This is a difference of             *
    # * 117609*86400 (0x1cb69*0x15180) == 10161417600 (0x25daaed80) seconds. */
    qcepoch = [ 0x2, 0x5daaed80 ]    

    # /* The length of four centuries, 146097 days of 86400 seconds, is *
    # * 12622780800 (0x2f0605980) seconds.                             */
    quadcent = [ 0x2, 0xf0605980 ]

    # /* The epoch for Unix time, 1970-01-01, is 719164 (0xaf93c) days after *
    # * our internal epoch, 0001=01=01 (0000-12-30).  This is a difference  *
    # * of 719164*86400 (0xaf93c*0x15180) == 62135769600 (0xe77949a00)      *
    # * seconds.                                                            */
    unixepoch = [ 0xe, 0x77949a00 ]

    # /* The epoch for stardates, 2162-01-04, is 789294 (0xc0b2e) days after *
    # * the internal epoch.  This is 789294*86400 (0xc0b2e*0x15180) ==      *
    # * 68195001600 (0xfe0bd2500) seconds.                                  */
    ufpepoch = [ 0xf, 0xe0bd2500 ]

    # /* The epoch for TNG-style stardates, 2323-01-01, is 848094 (0xcf0de) *
    # * days after the internal epoch.  This is 73275321600 (0x110f8cad00) *
    # * seconds.                                                           */
    tngepoch = [ 0x11, 0x0f8cad00 ]

    __init__(self):
        pass

    def toStardate(self, date=None):
        if not date:
            date = time.strftime("%d %m %Y %H %M %S")
        d, m, y, H, M, S = [ int(item) for item in date.split() ]
        

    def fromStardate(self, stardate):
        pass

if __name__ == "__main__":    
    print "Current stardate is: %s" % toStardate()