from conans import ConanFile, CMake
import os

class GlewConan(ConanFile):
    name = "glew"
    version = "2.1.0"
    license = "BDS"
    url = ""
    description = "Glew"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    exports_sources = os.path.join('glew-2.1.0', '*')

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder=os.path.join('glew-2.1.0', 'build', 'cmake'))
        cmake.build()

    def package(self):
        self.copy("*.h", dst="include", src=os.path.join('glew-2.1.0', "include"))
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)

    def package_info(self):
        if self.settings.build_type == 'Debug':
            self.cpp_info.libs = ["glew32d"]
        else:
            self.cpp_info.libs = ["glew32"]
