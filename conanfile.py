#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.69.0@bincrafters/stable")

class BoostLogicConan(base.BoostBaseConan):
    name = "boost_logic"
    version = "1.69.0"
    url = "https://github.com/bincrafters/conan-boost_logic"
    lib_short_names = ["logic"]
    header_only_libs = ["logic"]
    b2_requires = [
        "boost_config",
        "boost_core"
    ]
