from openssl.cliShare import CliShare
from interface.OpenForm import OpenForm

li = CliShare()
li.inform(OpenForm.DER)
li.out("a")
print(li.commandlineArray)
