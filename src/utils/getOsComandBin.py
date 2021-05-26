import os

def getOsComandBin():
    if os.name == "Windows":
        return 'openssl.exe';
    elif os.name == 'linux':
        return 'openssl';
    elif os.name == 'darwin':
        return 'openssl';
    return 'openssl';
#
#
# sys.modules[__name__] = getOsComandBin
