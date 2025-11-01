project('py-orthpol', 'c', 'fortran',
  version: '1.2.0',
  default_options: [
    'warning_level=1',
  ],
)

py = import('python').find_installation(pure: false)
py_dep = py.dependency()

incdir_numpy = run_command(py,
  ['-c', 'import numpy; print(numpy.get_include())'],
  check: true
).stdout().strip()

incdir_f2py = incdir_numpy / '..' / '..' / 'f2py' / 'src'

# Get all Fortran source files
fortran_sources = run_command('sh', '-c', 'ls src/*.f', check: true).stdout().strip().split('\n')

inc_dirs = include_directories(incdir_numpy, incdir_f2py)

py.extension_module(
  '_orthpol',
  fortran_sources,
  include_directories: inc_dirs,
  dependencies: py_dep,
  install: true,
  subdir: 'orthpol',
)

py.install_sources(
  ['orthpol/__init__.py'],
  subdir: 'orthpol',
)
