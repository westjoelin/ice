# **********************************************************************
#
# Copyright (c) 2003-2016 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************

$(project)_libraries	= TestCommon
$(project)_noinstall	:= 1

#
# Put the shared TestCommon library in the lib directory for convenience on platforms
# which don't support something like @loader_path.
#
TestCommon[shared]_targetdir	:= lib
TestCommon_dependencies 	:= Ice
TestCommon_sliceflags   	:= --dll-export TEST_API
TestCommon_cppflags		:= -DTEST_API_EXPORTS -I$(includedir) -I$(project) -Itest/include

projects += $(project)
