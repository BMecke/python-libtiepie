import os
import sys
import platform

try:
    from ...__config__ import LIBTIEPIE as DLL_PATH
except ImportError:
    this_dir = os.path.dirname(os.path.abspath(__file__))

    DLL_PATH = None
    if any(i == platform.machine() for i in ('x86_64', 'x86-64', 'amd64', 'x64', 'x86', 'x86-32', 'i586', 'i686')):
        is_32bit = (sys.maxsize <= 2 ** 32)
        arch = 'x86' if is_32bit else 'x86_64'
        arch_dir = os.path.join(this_dir, arch)
        DLL_PATH = os.path.join(arch_dir, 'libtiepie.so.0')

    elif any(i == platform.machine() for i in ('arm-bcm2708hardfp', 'armv6l')):
        arch_dir = os.path.join(this_dir, 'raspberry_pi')
        DLL_PATH = os.path.join(arch_dir, 'libtiepie.so.0')

    elif platform.machine() == 'armhf':
        arch_dir = os.path.join(this_dir, 'ARMv7')
        DLL_PATH = os.path.join(arch_dir, 'libtiepie.so.0')

    elif any(i == platform.machine() for i in ('arm64', 'aarch64')):
        arch_dir = os.path.join(this_dir, 'ARMv8')
        DLL_PATH = os.path.join(arch_dir, 'libtiepie.so.0')

    elif platform.machine() == 'armel':
        arch_dir = os.path.join(this_dir, 'armel')
        DLL_PATH = os.path.join(arch_dir, 'libtiepie.so.0')

    else:
        DLL_PATH = 'libtiepie.so.0'
