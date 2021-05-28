from openssl.x509 import x509


class Cer:
    def __init__(self):
        self.x509 = x509()

    def generaCerPem(filePathCer, outputpath):
        return 1;

    def getCer(self, cerpath):
        return 1

    # cer: self.getCertificate(cerpath).certificate,
    # nocer: self.getNoCer(cerpath)

    def getCertificate(self, cerFile):
        try:
            pem = self.x509.inform('DER').In(cerFile).outform('PEM').run();
            #      cerPem = {
            #     cerPem: pem,
            #     certificate: pem.replace( / (-+[ ^ -]+-+) / g, '').replace( /\s + / g, '')
            #     }
            # return cerPem
        except Exception as e:
            return e

    def getNoCer(self, cerFile):

        try:
        # const pem = x509.inform('DER').in (cerFile).outform('PEM').run();
        # // @ ts-ignore
        # const serialNumber = pki.certificateFromPem(pem).serialNumber.match( /.{1, 2} / g).map((v) = > {
        # return String.fromCharCode(parseInt(v, 16));
        # }).join('');
        # return serialNumber;
        except Exception as e:
            return e

    def agetCerPem(cerpempath):
        return 1

    def getCerFile(cerfile):
        return 1

    def text(cerFile):
        try:
        # return x509.inform('DER'). in (cerFile).noout().text().run()
        # x509 - inform
        # der - in ${cer} - noout - text
        # `).stdout
        except Exception as e:
            return e

    def pubkey(self, cerFile):
        try:
        # cli = x509.inform('DER').In(cerFile).noout().pubkey().run()
        # pubkey = {
        #     pubkey: cli,
        #     pubkeyData: '',
        # }
        # pubkey.pubkeyData = cli.replace( / (-+[ ^ -]+-+) / g, '').replace( /\s + / g, '');
        # return pubkey;
        except Exception as e:
            return e

    def modulu(self, cerFile):
        try:
        # cli = x509.inform('DER').in (cerFile).noout().modulus().run()
        #  modul = {
        #   modulus: cli.replace('Modulus=', '').replace( / ^\s + / g, '').replace( /\s +$ / g, '')
        #  }
        # return modul
        except Exception as e:
            return e

    def serial(self, cerFile):
        try:
        # const cli = x509.inform('DER').in (cerFile).noout().serial().run()
        # const seria = {
        # serial: cli.replace('serial=', '').replace( / ^\s + / g, '').replace( /\s +$ / g, '')
        # }
        # return seria;
        except Exception as e:
            return e

    def subjectHash(self, cerFile):
        try:
            return x509.inform('DER').In(cerFile).noout().subject_hash().run()
        except Exception as e:
            return e

    def issuerHash(self, cerFile):
        try:
            return x509.inform('DER').In(cerFile).noout().issuer_hash().run()
        except Exception as e:
            return e

    def ocspid(self, cerFile):
        try:
            return x509.inform('DER').In(cerFile).noout().ocspid().run()
        except Exception as e:
            return e

    def hash(self, cerFile):
        try:
            return x509.inform('DER'). in (cerFile).noout().hash().run()
        except Exception as e:
            return e

    def subjectHashOld(self, cerFile):
        try:
            return x509.inform('DER'). in (cerFile).noout().subject_hash_old().run()
        except Exception as e:
            return e

    def issuerHashOld(self, cerFile):
        try:
            return x509.inform('DER').In(cerFile).noout().issuer_hash_old().run()
        except Exception as e:
            return e

    def subject(self, cerFile):
        try:
        # text = x509.inform('DER').in (cerFile).noout().subject().run()
        # text = text.replace('subject=', '');
        # stringArray = text.split(',');
        # obj = {};
        # for(const txt of stringArray)
        #     extrac = txt.split('=');
        #     if extrac.length == 2:
        #         key = extrac[0].replace( / ^\s + / g, '').replace( /\s +$ / g, '');
        #         val = extrac[1].replace( / ^\s + / g, '').replace( /\s +$ / g, '');
        #         obj[key] = val;
        # return obj;
        except Exception as e:
            return e

    def date(self, file, format='DD/MM/YYYY HH:mm:ss.SSS'):
        try:
        # DateCer = x509.inform('DER').in (file).noout().startdate().enddate().run();
        #  data = DateCer.split('\n');
        #  startDate = data[0].replace('notBefore=', '').replace('  ', '');
        #  endDate = data[1].replace('notAfter=', '').replace('  ', '');
        #  pattOne = new RegExp('([A-z]{3}) ([0-9]{1,2}) ([0-2][0-9]:[0-5][0-9]:[0-5][0-9]) ([0-9]{4})');
        #  st = startDate.match(pattOne);
        #  stfecha = st ? st[2] + '/' + st[1] + '/' + st[4]: ''; //+' ' + findregex[3]
        #  ststaff = st ? st[3]: '';
        #  startDate = moment(newDate(stfecha + ' ' + ststaff)).format(format)
        #      ed = endDate.match(pattOne);
        #     edfecha = ed ? ed[2] + '/' + ed[1] + '/' + ed[4]: ''; // +' ' + findregex[3]
        #     edstaff = ed ? ed[3]: '';
        #     endDate = moment(new Date(edfecha + ' ' + edstaff)).format(format)
        #     return  {
        #                startDate,
        #             endDate
        #     };
        except Exception as e:
            return e

    def getSerialCert(self):
        return 1;

    def getFechaVigencia(self):

        return 1;

    def getCerPem(self, cerpempath, title):

        try:
            cerpem = readFileSync(cerpempath);
            if title:
                cerpem = cerpem.replace( / (-+[ ^ -]+-+) / g, '');
                cerpem = cerpem.replace( /  \s + / g, '');
                return cerpem;
                except Exception as e:
                return e

    def issuer(self, cerFile):
        try:
            text = x509.inform('DER').In(cerFile).noout().issuer().run({encoding: 'utf8'})
            text = text.replace('issuer=', '');
            stringArray = text.split(',');
            obj = {};
        for (const txt of stringArray):
            extrac = txt.split('=');
            if (extrac.length === 2)
                key = extrac[0].replace( / ^\s + / g, '').replace( /\s +$ / g, '');
                val = extrac[1].replace( / ^\s + / g, '').replace( /\s +$ / g, '');
                obj[key] = val;
        return obj;
        except Exception as e:
        return e

    def email(self, cerFile):
        try:
            return x509.inform('DER'). in (cerFile).noout().email().run();
        except Exception as e:
            return e

    def ocspUri(self, cerFile):
        try:
            return x509.inform('DER').In(cerFile).noout().ocsp_uri().run();
        except Exception as e:
            return e

    def Dates(cerFile: string):
        try:
            return x509.inform('DER').In(cerFile).noout().dates().run();
        except Exception as e:
            return e

    def checkend(self, cerFile, seconds):
        try:
            # // Certificate will expire El certificado caducará
            # // Certificate will not expire El certificado no caducará
            check = x509.inform('DER').In(cerFile).noout().checkend(seconds).run();
            return check
        except Exception as e:
            return e

    def fingerPrint(self, cerFile):
        try:
            check = x509.inform('DER').In(cerFile).noout().fingerprint().run();
            return check
        except Exception as e:
            return e

    def C(self, cerFile):
        try:
            # // Certificate will not expire El certificado no caducará
            # // Certificate will expire El certificado caducará
            check = x509.inform('DER').In(cerFile).noout().C().run();
            return check
        except Exception as e:
            return e

    def validarCertificado(self):
        return 1

    def generaPFX(self):
        return 1;

    def pareja(self):
        return 1;

    def certificadoBase64(self, nombreCer):
        return 1;
