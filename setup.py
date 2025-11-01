#!/usr/bin/env python
"""Setup script for py-orthpol with NumPy 2.x compatibility"""

import os
import glob
import sys
import subprocess
from pathlib import Path
from setuptools import setup
from setuptools.command.build_ext import build_ext as _build_ext
import numpy as np


class f2py_build_ext(_build_ext):
    """Custom build_ext command that uses f2py to compile Fortran"""

    def build_extension(self, ext):
        # Get source files
        sources = [str(Path(s).resolve()) for s in ext.sources]

        # Output directory
        build_dir = Path(self.build_lib) / 'orthpol'
        build_dir.mkdir(parents=True, exist_ok=True)

        # Module name
        module_name = ext.name.split('.')[-1]

        # Call f2py
        f2py_cmd = [
            sys.executable, '-m', 'numpy.f2py',
            '-c',
            '--build-dir', str(self.build_temp),
        ] + sources + [
            '-m', module_name,
        ]

        print(f"Running f2py: {' '.join(f2py_cmd)}")
        result = subprocess.run(f2py_cmd, cwd=str(Path.cwd()))

        if result.returncode != 0:
            raise RuntimeError("f2py compilation failed")

        # Move the compiled module to the right place
        import shutil
        for item in Path('.').glob(f'{module_name}.*.so'):
            shutil.move(str(item), str(build_dir / item.name))


# Get all Fortran source files
fortran_sources = glob.glob(os.path.join('src', '*.f'))

if __name__ == "__main__":
    from setuptools import Extension

    ext_module = Extension(
        name='orthpol._orthpol',
        sources=fortran_sources,
    )

    setup(
        ext_modules=[ext_module],
        cmdclass={'build_ext': f2py_build_ext},
    )
