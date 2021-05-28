import utils.getOsComandBin
import utils.getOsComandBin
import interface.OpenForm


class CliShare:

    def __init__(self):
        self.opensslBin = utils.getOsComandBin.getOsComandBin();
        self.commandline = self.opensslBin;
        self.commandlineArray = [];
        self.command = '';

    # ["DER", "PEM"]
    def inform(self, form):
        # Type checking
        if not isinstance(form, interface.OpenForm.OpenForm):
            raise TypeError('direction must be an instance of Direction Enum')
        self.commandline += ' -inform ' + form.value;
        self.commandlineArray.append('-inform ' + form.value);
        return self;

    # ["DER", "PEM"]
    def outform(self, form):
        # Type checking
        if not isinstance(form, interface.OpenForm.OpenForm):
            raise TypeError('direction must be an instance of Direction Enum')
        self.commandline += ' -outform ' + form.value;
        self.commandlineArray.append('-outform ' + form.value);
        return self;

    def In(self, filename):
        self.commandline += ' -in ' + filename;
        self.commandlineArray.append(' -in ' + filename);
        return self;

    # todo https://www.openssl.org/docs/man1.1.1/man1/openssl.html

    def passin(self, arg):
        self.commandline += ' -passin ' + arg;
        self.commandlineArray.append(' -passin ' + arg);
        return self;

    def passout(self, arg):
        self.commandline += ' -passout ' + arg;
        self.commandlineArray.append(' -passout ' + arg);
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
