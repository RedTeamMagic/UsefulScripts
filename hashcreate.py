import argparse
import hashlib,binascii
    
parser = argparse.ArgumentParser(description='Converts a clear text password into an NT LM hash.') 
parser.add_argument('password',help=' Cleartext password used to generate the NTLM hash' ) 
args = parser.parse_args() 
        
hash = hashlib.new('md4', args.password.encode('utf-16le')).digest() 
print binascii.hexlify(hash)
