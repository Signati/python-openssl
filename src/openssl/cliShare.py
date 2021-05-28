import utils.getOsComandBin
import utils.getOsComandBin
import interface.derpem

class CliShare:

    def __init__(self):
        self.opensslBin = utils.getOsComandBin.getOsComandBin();
        self.commandline = self.opensslBin;
        self.commandlineArray = [];
        self.command = '';

    # ["DER", "PEM"]
    def inform(self, direction):
        # Type checking
        if not isinstance(direction, interface.derpem.Direction):
            raise TypeError('direction must be an instance of Direction Enum')


        self.commandline += ' -inform ' + direction.value;
        self.commandlineArray.append('-inform ' + direction.value);
        return self;

    def outform(self, options: ["DER", "PEM"]):
        self.commandline += ' -outform  ${options}';
        self.commandlineArray.append('-outform ${options}');
        return self;

    def In(self, filename):
        self.commandline += ' -in  ${filename}';
        self.commandlineArray.append('-in ${filename}');
        return self;

    # todo https://www.openssl.org/docs/man1.1.1/man1/openssl.html

    def passin(self, arg):
        self.commandline += ' -passin ${arg}';
        self.commandlineArray.append('-passin ${arg}');
        return self;

    def passout(self, arg):
        self.commandline += ' -passout ${arg}';
        self.commandlineArray.append('-passout ${arg}');
        return self;

    def out(self, filename):
        self.commandline += ' -out ' + filename;
        self.commandlineArray.append(' -out ' + filename);
        return self;

    def run(self, options):
        return ''

    # try {
    # const cli = self.commandline
    # self.commandline = self.opensslBin + ' '+ self.command;
    # const saxonProc = commandSync(cli, options).stdout;
    # return saxonProc;
    # } catch(e)
    # {
    # throw
    # new
    # Error(e.message);

    def cli(self):
        return ''

    # try {
    # const cp = self.commandline
    # self.commandline = self.opensslBin + ' '+ self.command;
    # return cp
    # } catch(e)
    # {
    # throw
    # new
    # Error(e.message);

    def cliArray(self):
        return ''

# try {
# const cp =[...self.commandlineArray]
# self.commandlineArray =[]
# return cp;
# } catch(e)
# {
# throw
# new
# Error(e.message);
# li = CliShare()
# print(li.opensslBin)
