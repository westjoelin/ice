# **********************************************************************
#
# Copyright (c) 2003-2010 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

import Ice, Test

def test(b):
    if not b:
        raise RuntimeError('test assertion failed')

def allTests():

    print "testing default values...",

    v = Test.Struct1()
    test(not v.boolFalse)
    test(v.boolTrue)
    test(v.b == 254)
    test(v.s == 16000)
    test(v.i == 3)
    test(v.l == 4)
    test(v.f == 5.1)
    test(v.d == 6.2)
    test(v.str == "foo bar")
    test(v.c == Test.Color.red)
    test(v.noDefault == '')

    v = Test.Struct2()
    test(v.boolTrue == Test.ConstBool)
    test(v.b == Test.ConstByte)
    test(v.s == Test.ConstShort)
    test(v.i == Test.ConstInt)
    test(v.l == Test.ConstLong)
    test(v.f == Test.ConstFloat)
    test(v.d == Test.ConstDouble)
    test(v.str == Test.ConstString)
    test(v.c == Test.ConstColor)

    v = Test.Base()
    test(not v.boolFalse)
    test(v.boolTrue)
    test(v.b == 1)
    test(v.s == 2)
    test(v.i == 3)
    test(v.l == 4)
    test(v.f == 5.1)
    test(v.d == 6.2)
    test(v.str == "foo bar")
    test(v.noDefault == '')

    v = Test.Derived()
    test(not v.boolFalse)
    test(v.boolTrue)
    test(v.b == 1)
    test(v.s == 2)
    test(v.i == 3)
    test(v.l == 4)
    test(v.f == 5.1)
    test(v.d == 6.2)
    test(v.str == "foo bar")
    test(v.c == Test.Color.green)
    test(v.noDefault == '')

    v = Test.BaseEx()
    test(not v.boolFalse)
    test(v.boolTrue)
    test(v.b == 1)
    test(v.s == 2)
    test(v.i == 3)
    test(v.l == 4)
    test(v.f == 5.1)
    test(v.d == 6.2)
    test(v.str == "foo bar")
    test(v.noDefault == '')

    v = Test.DerivedEx()
    test(not v.boolFalse)
    test(v.boolTrue)
    test(v.b == 1)
    test(v.s == 2)
    test(v.i == 3)
    test(v.l == 4)
    test(v.f == 5.1)
    test(v.d == 6.2)
    test(v.str == "foo bar")
    test(v.noDefault == '')
    test(v.c == Test.Color.green)

    print "ok"