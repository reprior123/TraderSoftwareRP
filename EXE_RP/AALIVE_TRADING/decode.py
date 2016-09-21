########################
def decoder(codein):
    output =''
    x = 'i'
    t = 'p'
    r = 'e'
    p = 'r'
    n = '3'
    w = '4'
    q = '1'
    d = '0'
    b = 'l'
    c = 'i'
    a = 'C'
    for nn in range(11) :
        output += locals()[codein[nn]]
    return output


#############
username = 'reprior123@gmail.com'
mypasswordnew = (str(decoder('abxttrpwdbn'))).strip()
mypassword = 'Clipper4013'
print '|',str(mypasswordnew),'|'
