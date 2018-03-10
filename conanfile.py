from conans import ConanFile, tools
import os
import shutil
import errno

def copy(src, dest):
    try:
        shutil.copytree(src, dest)
    except OSError as e:
        # If the error was caused because the source wasn't a directory
        if e.errno == errno.ENOTDIR:
            shutil.copy(src, dest)
        else:
            print('Directory not copied. Error: %s' % e)


class CoreconfigConan(ConanFile):
    name = "Core.Utils"
    version = "1.0"
    license = "Mit"
    url = "https://github.com/SlyrisOrg/conan-core-v2-utils.git"
    description = "Core::Utils Modules"
    no_copy_source = True


    # No settings/options are necessary, this is header only

    def requirements(self):
        self.requires.add("Core.PP/1.0@SlyrisOrg/stable", private=False)
        self.requires.add("Core.Config/1.0@SlyrisOrg/stable", private=False)


    def source(self):
        """retrieval of the source code here. Remember you can also put the code in the folder and
        use exports instead of retrieving it with this source() method
        """
        self.run("git clone https://github.com/SlyrisOrg/core-v2")
        copy(os.getcwd() + "/core-v2/core/utils/core/utils", "core/utils")
        shutil.rmtree(os.getcwd() + "/core-v2", ignore_errors=True)

    def package(self):
        self.copy("*.hpp", "include")
