class Key:
    def getKey(self, keyfile, password):

        try:
            # keyPem = pkcs8.inform('DER'). in (keyfile).outform('PEM').passin('pass:' + password).run();
            # privateKey = {
            #     privateKeyPem: keyPem,
            #     privatekey: keyPem.replace( / (-+[ ^ -]+-+) / g, '').replace( /\s + / g, '')
            # }
            return 1  # privateKey
        except Exception as e:
            return e

    def generaKeyPem(self, filePathKey, outputpath):
        return 1;

    def getKeyPem(self, keyfile, title):
        try:
            # pem = await fs.readFileSync(keyfile);
            # key = pem.toString('ascii');
            # if title:
            # key = key.replace( / (-+[ ^ -]+-+) / g, '');
            # key = key.replace( /\s + / g, '');
            return 1  # key;
        except Exception as e:
            return e
