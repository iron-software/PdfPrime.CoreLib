import os
import subprocess
from pygemstones.system import runner as r
from pygemstones.io import file as f
from pygemstones.util import log as l

def build_qpdf_wasm():
    build_dir = os.path.join("build", "emscripten", "qpdf")
    f.recreate_dir(build_dir)
    os.chdir(build_dir)

    emcmake = os.path.join(os.getenv("EMSDK"), "upstream", "emscripten", "emcmake")

    command = [
        "python",
        emcmake,
        "cmake",
        "../../third_party/qpdf",
        "-DCMAKE_BUILD_TYPE=Release",
        "-DBUILD_SHARED_LIBS=OFF",
        "-DQPDF_BUILD_TESTS=OFF",
        "-DQPDF_BUILD_DOC=OFF",
        "-DQPDF_BUILD_STATIC=ON",
        "-DCMAKE_C_COMPILER=emcc",
        "-DCMAKE_CXX_COMPILER=em++",
    ]
    r.run(" ".join(command), shell=True)

    r.run("emmake make -j4", shell=True)

    os.chdir("../../../..")
    l.ok()
