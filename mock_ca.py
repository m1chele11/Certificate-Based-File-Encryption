#mock to "sign" a public key by appending a CA sig


def sign_cert(public_key_path):
    with open(public_key_path, "r") as pub_file:
        public_key = pub_file.read()

    signed_cert = f"MOCK CA SIGNATURE\n{public_key}\n END MOCK CA SIGNATURE"
    with open("signed_certificate.pem", "w") as cert_file:
        cert_file.write(signed_cert)

sign_cert("public_key.pem")