from openssl.cliShare import CliShare
from interface.derpem import Direction

li = CliShare()
li.inform(Direction.DOWN)
li.out("a")
print(li.commandlineArray)
