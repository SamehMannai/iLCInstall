##################################################
#
# ROOT module
#
# Author: Jan Engels, DESY
# Date: Jan, 2007
#
##################################################
                                                                                                                                                            
# custom imports
from baseilc import BaseILC
from util import *


class ROOT(BaseILC):
    """ Responsible for the ROOT configuration process. """
    
    def __init__(self, userInput):
        BaseILC.__init__(self, userInput, "ROOT", "root")

        self.installSupport = False
        self.hasCMakeBuildSupport = False

        self.reqfiles = [
                ["lib/libCore.so", "lib64/libCore.so", "lib/libCore.dylib"], 
                ["lib/libPhysics.so", "lib64/libPhysics.so", "lib/libPhysics.dylib"],
                ["bin/root-config"]
        ]

    def postCheckDeps(self):
        BaseILC.postCheckDeps(self)

        self.env["ROOTSYS"] = self.installPath
        self.envpath["PATH"].append( "$ROOTSYS/bin" )
        self.envpath["LD_LIBRARY_PATH"].append( "$ROOTSYS/lib" )
