from openssl.cliShare import CliShare
from openssl.pkcs8 import pkcs8
from openssl.x509 import x509
from interface.OpenForm import OpenForm

pk = pkcs8()
x5 = x509()
pk.inform(OpenForm.DER)
pk.out("a")
x5.inform(OpenForm.DER)
x5.out("a")
print("x5 " + x5.cli())
print("x5 ", x5.commandlineArray)
print("pk " + pk.cli())
print("pk ", pk.commandlineArray)
