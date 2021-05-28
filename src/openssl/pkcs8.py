from openssl.cliShare import CliShare
from utils.getOsComandBin import getOsComandBin


class pkcs8(CliShare):

    def __init__(self):
        self.commandline = '';
        self.commandlineArray = [];
        self.command = 'pkcs8';
        self.opensslBin = '';
        self.opensslBin = getOsComandBin();
        self.commandline = self.opensslBin + ' ' + self.command;

    def topk8(self):
        self.commandline += " -topk8";
        self.commandlineArray.append("-topk8");
        return self;

    def traditional(self):
        self.commandline += " -traditional";
        self.commandlineArray.append("-traditional");
        return self;

    def iter(self, count):
        self.commandline += " -iter ${count}";
        self.commandlineArray.append("-iter ${count}");
        return self;

    def nocrypt(self):
        self.commandline += " -nocrypt";
        self.commandlineArray.append("-nocrypt");
        return self;

    def rand(self, file):
        self.commandline += " -rand ${file}";
        self.commandlineArray.append("-rand ${file}");
        return self;
