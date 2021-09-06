from metaL import *

p = Project(
    title='Guest UNIX in Rust',
    about='''
* **guest OS** works over any mainstream Windows/Linux/...
* POSIX API emulation layer over host-OS generic API (WinAPI, Linux libc)
    * https://t.me/uneex_talks/4162
''') \
    | Rust()

p.sync()
