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
            raise TypeError('form must be an instance of OpenForm Enum')
        if form.value == interface.OpenForm.OpenForm.ENGINE:
            raise TypeError('form dont must be ENGINE in this function')
        self.commandline += ' -inform ' + form.value;
        self.commandlineArray.append('-inform ' + form.value);
        return self;

    # ["DER", "PEM"]
    def outform(self, form):
        # Type checking
        if not isinstance(form, interface.OpenForm.OpenForm):
            raise TypeError('direction must be an instance of OpenForm Enum')
        if form.value == interface.OpenForm.OpenForm.ENGINE:
            raise TypeError('form dont must be ENGINE in this function')
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
        try:
            cli = self.commandline;
            self.commandline = self.opensslBin + ' ' + self.command;
            # const saxonProc = commandSync(cli, options).stdout;
            # return saxonProc;

        except Exception as e:
            print(e)

    def cli(self):
        try:
            cl = self.commandline
            self.commandline = self.opensslBin + ' ' + self.command;
            return cl
        except Exception as e:
            print(e)

    def cliArray(self):
        try:
            cl = self.commandlineArray
            self.commandlineArray = []
            return cl;
        except Exception as e:
            print(e)
