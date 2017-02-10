from conans import ConanFile, CMake

class BoostSmlConan(ConanFile):
    name = "boost-sml"
    version = "git-master"
    author = "Erik Zenker (erikzenker@posteo.de)"
    license = "Boost"
    url ="https://github.com/erikzenker/conan-sml"
    description = "Your scalable C++14 header State Machine Library with no dependencies"
    build_policy = "missing"
    settings = "os", "compiler", "build_type", "arch"

    def source(self):
        self.run("git clone https://github.com/boost-experimental/sml.git")

    def build(self):
        cmake = CMake(self.settings)
        self.run('cd %s/sml && make' % (self.conanfile_directory))

    def package(self):
        self.copy("*", dst="include", src="sml/include")
