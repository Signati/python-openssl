from openssl.cliShare import CliShare
from utils.getOsComandBin import getOsComandBin
from interface.OpenForm import OpenForm


class x509(CliShare):

    def __init__(self):
        self.commandline = '';
        self.commandlineArray = [];
        self.command = 'x509';
        self.opensslBin = '';
        self.opensslBin = getOsComandBin();
        self.commandline = self.opensslBin + ' ' + self.command;

    def help(self):
        return self

    def digest(self):
        self.commandline += " -digest";
        self.commandlineArray.append("-digest");
        return self;

    def rand(self, file):
        self.commandline += " -rand " + file
        self.commandlineArray.append("-rand " + file);
        return self;

    def writerand(self, file):
        self.commandline += " -writerand " + file;
        self.commandlineArray.append("-writerand " + file);
        return self;

    def engine(self, id):
        self.commandline += " -engine " + id;
        self.commandlineArray.append("-engine " + id);
        return self;

    def preserve_dates(self):
        # todo validate if use options days
        self.commandline += " -preserve_dates";
        self.commandlineArray.append("-preserve_dates");
        return self;

    def text(self):
        self.commandline += " -text";
        self.commandlineArray.append("-text");
        return self;

    def ext(self, extensions):
        self.commandline += " -ext  " + extensions;
        self.commandlineArray.append("-ext  " + extensions);
        return self;

    def certopt(self, option):
        self.commandline += " -certopt " + option;
        self.commandlineArray.append("-certopt " + option);
        return self;

    def noout(self):
        self.commandline += " -noout";
        self.commandlineArray.append("-noout");
        return self;

    def pubkey(self):
        self.commandline += " -pubkey";
        self.commandlineArray.append("-pubkey");
        return self;

    def modulus(self):
        self.commandline += " -modulus";
        self.commandlineArray.append("-modulus");
        return self;

    def serial(self):
        self.commandline += " -serial";
        self.commandlineArray.append("-serial");
        return self;

    def subject_hash(self):
        self.commandline += " -subject_hash";
        self.commandlineArray.append("-subject_hash");
        return self;

    def issuer_hash(self):
        self.commandline += " -issuer_hash";
        self.commandlineArray.append("-issuer_hash");
        return self;

    def ocspid(self):
        self.commandline += " -ocspid";
        self.commandlineArray.append("-ocspid");
        return self;

    def hash(self):
        self.commandline += " -hash";
        self.commandlineArray.append("-hash");
        return self;

    def subject_hash_old(self):
        self.commandline += " -subject_hash_old";
        self.commandlineArray.append("-subject_hash_old");
        return self;

    def issuer_hash_old(self):
        self.commandline += " -issuer_hash_old";
        self.commandlineArray.append("-issuer_hash_old");
        return self;

    def subject(self):
        self.commandline += " -subject";
        self.commandlineArray.append("-subject");
        return self;

    def issuer(self):
        self.commandline += " -issuer";
        self.commandlineArray.append("-issuer");
        return self;

    def nameopt(self, option):
        self.commandline += " -nameopt " + option;
        self.commandlineArray.append("-nameopt " + option);
        return self;

    def email(self):
        self.commandline += " -email";
        self.commandlineArray.append("-email");
        return self;

    def ocsp_uri(self):
        self.commandline += " -ocsp_uri";
        self.commandlineArray.append("-ocsp_uri");
        return self;

    def startdate(self):
        self.commandline += " -startdate";
        self.commandlineArray.append("-startdate");
        return self;

    def enddate(self):
        self.commandline += " -enddate";
        self.commandlineArray.append("-enddate");
        return self;

    def dates(self):
        self.commandline += " -dates";
        self.commandlineArray.append("-dates");
        return self;

    def checkend(self, num):
        self.commandline += " -checkend " + num;
        self.commandlineArray.append("-checkend " + num);
        return self;

    def fingerprint(self):
        self.commandline += " -fingerprint";
        self.commandlineArray.append("-fingerprint");
        return self;

    def C(self):
        self.commandline += " -C";
        self.commandlineArray.append("-C");
        return self;

    def trustout(self):
        self.commandline += " -trustout";
        self.commandlineArray.append("-trustout");
        return self;

    def setalias(self, arg):
        self.commandline += " -setalias " + arg
        self.commandlineArray.append("-setalias " + arg);
        return self;

    def alias(self):
        self.commandline += " -alias";
        self.commandlineArray.append("-alias");
        return self;

    def clrtrust(self):
        self.commandline += " -clrtrust";
        self.commandlineArray.append("-clrtrust");
        return self;

    def clrreject(self):
        self.commandline += " -clrreject";
        self.commandlineArray.append("-clrreject");
        return self;

    def addtrust(self, arg):
        self.commandline += " -addtrust " + arg
        self.commandlineArray.append("-addtrust " + arg);
        return self;

    def addreject(self, arg):
        self.commandline += " -addreject " + arg;
        self.commandlineArray.append("-addreject " + arg);
        return self;

    def purpose(self):
        self.commandline += " -purpose";
        self.commandlineArray.append("-purpose");
        return self;

    def sigopt(self, arg):
        # todo
        return self;

    def clrext(self):
        self.commandline += " -clrext";
        self.commandlineArray.append("-clrext");
        return self;

    #: 'DER' | 'PEM' | 'ENGINE'
    def keyform(self, options):
        # Type checking
        if not isinstance(options, OpenForm):
            raise TypeError('direction must be an instance of OpenForm Enum')
        self.commandline += " -signkey " + options;
        self.commandlineArray.append("-signkey " + options);
        return self;

    def days(self, arg):
        self.commandline += " -days " + arg;
        self.commandlineArray.append("-days " + arg);
        return self;

    def x509toreq(self):
        self.commandline += " -x509toreq";
        self.commandlineArray.append("-x509toreq");
        return self;

    def req(self):
        self.commandline += " -req";
        self.commandlineArray.append("-req");
        return self;

    def set_serial(self, n):
        self.commandline += " -set_serial " + n;
        self.commandlineArray.append("-set_serial " + n);
        return self;

    def CA(self, filename):
        self.commandline += " -CA " + filename;
        self.commandlineArray.append("-CA " + filename);
        return self;

    def CAkey(self, filename):
        self.commandline += " -CAkey " + filename;
        self.commandlineArray.append("-CAkey " + filename);
        return self;

    def CAserial(self, filename):
        self.commandline += " -CAserial " + filename;
        self.commandlineArray.append("-CAserial " + filename);
        return self;

    def CAcreateserial(self):
        self.commandline += " -CAcreateserial";
        self.commandlineArray.append("-CAcreateserial");
        return self;

    def extfile(self, filename):
        self.commandline += " -extfile " + filename;
        self.commandlineArray.append("-extfile " + filename);
        return self;

    def extensions(self, section):
        self.commandline += " -extensions " + section;
        self.commandlineArray.append("-extensions " + section);
        return self;

    def force_pubkey(self, key):
        self.commandline += " -force_pubkey " + key;
        self.commandlineArray.append("-force_pubkey " + key);
        return self;
