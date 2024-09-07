
import hmac
import hashlib
def verify_hmac(my_socket, data):
    print('Message is being authenticated using HMAC...')
    received_hmac = my_socket.recv(4096)
    session_key = b'abcde' #REMOVE!!! this key is just for testing
    client_generated_hmac = hmac.digest(key=session_key, msg=data, digest=hashlib.sha256)
    if hmac.compare_digest(received_hmac, client_generated_hmac):
        print('Integrity check passed')
    else: # if integrity check fails, ask if they want to continue download
        valid_input = False
        while valid_input != True:
            continueprogram = input('Integrity check failed. Would you like to terminate connection? (Y/N)\n>> ').lower()
            if continueprogram == 'n':
                print('Resuming...')
                valid_input = True
                return
            elif continueprogram == 'y':
                print('Terminating...')
                valid_input = True
                exit()
            else:
                print('Invalid input. Please enter "Y" or "N".')