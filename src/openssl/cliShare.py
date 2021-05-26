import utils.getOsComandBin


class CliShare:

    def __init__(self):
        self.opensslBin = utils.getOsComandBin.getOsComandBin();
        self.commandline = self.opensslBin;
        self.commandlineArray = [];
        self.command = '';

    def inform(self, options: ["DER", "PEM"]):
        self.commandline += ' -inform ' + options;
        self.commandlineArray.append('-inform ' + options);
        return self;

    def outform(self, options: ["DER", "PEM"]):
        self.commandline += ' -outform  ${options}';
        self.commandlineArray.append('-outform ${options}');
        return self;

    def In(self, filename):
        self.commandline += ' -in  ${filename}';
        self.commandlineArray.push('-in ${filename}');
        return self;

    # todo https://www.openssl.org/docs/man1.1.1/man1/openssl.html

    def passin(self, arg):
        self.commandline += ' -passin ${arg}';
        self.commandlineArray.push('-passin ${arg}');
        return self;

    def passout(self, arg):
        self.commandline += ' -passout ${arg}';
        self.commandlineArray.push('-passout ${arg}');
        return self;

    def out(self, filename):
        self.commandline += ' -out ${filename}';
        self.commandlineArray.push('-out ${filename}');
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
class Sclishare:
    pass
