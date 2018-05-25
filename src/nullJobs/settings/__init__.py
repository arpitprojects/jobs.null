from .base import *

from .production import *

try:
    from .local import *
except:
    pass

#Here local is overwrtiting all
