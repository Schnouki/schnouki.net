Title: lighttpd and SSL client certificates
Date: 2014-08-12 12:07
Category: Software
Tags: lighttpd, SSL, security

I recently configured my [lighttpd][] server to enable authentication based on SSL client certificates on a private
subdomain. Here's a quick how-to.


1.  Configure OpenSSL:

        :::console
        $ cp /etc/ssl/openssl.cnf ./
        $ $EDITOR openssl.cnf  # Edit "dir"
        $ mkdir certs
        $ echo "00" > serial
        $ echo "00" > crlnumber
        $ touch index.txt

2.  Create the CA:

        :::console
        $ openssl genrsa -out ca.key 2048  # Generate a RSA-2048 private key
        $ openssl req -new -x509 -days 3650 -key ca.key -out ca.crt  # Generate a certificate from the private key

3.  Create a SSL client certificate:

        :::console
        $ openssl genrsa -out client.key 2048  # Generate a RSA-2048 private key
        $ openssl req -config openssl.cnf -new -key client.key -out client.csr  # Generate a certificate from the private key
        $ openssl ca -batch -config openssl.cnf -days 3650 -in client.csr -out client.crt -keyfile ca.key -cert ca.crt -policy policy_anything  # Sign the certificate using the CA
        $ openssl pkcs12 -export -in client.crt -inkey client.key -certfile ca.crt -out client.p12  # Convert the certificate to PKCS#12 for browser support

4.  Import the certificates in a browser. For example in Firefox:

    1. Go to Settings, "Advanced", "Certificates" tab, and click "Show certificates"
    2. In "Authorities", click "Import" and select `ca.crt`
    3. In "Your certificates", click "Import" and select `client.p12`

5.  Configure lighttpd.

    1. If you haven't configured SSL in lighttpd yet, [do it][ssl-details].
    2. Add your newly generated `ca.crt` to the PEM file you're using as `ssl.ca-file` in lighttpd. I'm using StartSSL,
        so my `ca-file` contains the StartSSL root CA and its Class 1 certificate, so I use the following to generate my
        `ca-file`:

            :::console
            $ cat /etc/ssl/startssl/ca.pem /etc/ssl/startssl/sub.class1.server.ca.pem ./ca.crt > /etc/lighttpd/ca.pem
            $ cat /etc/lighttpd/lighttpd.conf | grep ssl.ca-file
                ssl.ca-file = "/etc/lighttpd/ca.pem"

    3. Enable client certificate verification in lighttpd:

            :::lighttpd
            $HTTP["host"] == "my-ssl-domain" {
                ssl.ca-file = "/etc/lighttpd/ca.pem"
                ssl.verifyclient.activate = "enable"
                ssl.verifyclient.enforce = "enable"
                ssl.verifyclient.username = "SSL_CLIENT_S_DN_CN"
            }

        - `ssl.verifyclient.activate` activates the client certificate verification
        - `ssl.verifyclient.enforce` allows to *enforce* valid client certificates: if enabled, the SSL connections will
           fail if no client certificate is provided. If disabled, client certificates will be optional.
        - `ssl.verifyclient.username` defines which field of the client certificate will be stored in the request
           environment (which can then be used by scripts run by the server): `SSL_CLIENT_S_DN_CN` for the Common Name,
           `SSL_CLIENT_S_DN_emailAddress` for the email address, etc.
        - more options are described [in the official docs][ssl-conf].

6.  Restart lighttpd and visit your site: you should be asked which certificate you want to use to connect.


*[CA]: Certificate Authority

[lighttpd]: http://www.lighttpd.net/
[ssl-conf]: http://redmine.lighttpd.net/projects/lighttpd/wiki/Docs_SSL#Configuration
[ssl-details]: http://redmine.lighttpd.net/projects/1/wiki/docs_ssl#Details
