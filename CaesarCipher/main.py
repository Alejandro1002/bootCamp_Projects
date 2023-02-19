# import
from ASCII_ART import CaesarCipherLogo
from caesarCipher import CaesarCipher
from replit import clear

# recursive
def CaesarCipherProgram():
    # print
    print(f' {CaesarCipherLogo} \n')

    # flag for while loop
    shouldContinue = True

    while shouldContinue:

        try:
            # inputs
            cipher = input(' TYPE EITHER [ ENCODE ] OR [ DECODE ]: ').upper()
            text = input('\n TYPE THE TEXT YOU WANT TO CIPHER: ').upper()
            times = int(input('\n ENTER THE NUMBER OF SHIFTING TIMES: '))
            # shredding down the number of times shifting available
            times %= 26

        except Exception as error:
            print(f'\n SOMETHING HAS GONE WRONG: {error} \n')

        else:
            # create object
            caesarCipher = CaesarCipher(cipher=cipher, txt=text, times=times)

            if cipher == 'ENCODE':
                caesarCipher.encodingText()
                print(f' THE ENCODED TEXT IS: [ {caesarCipher.generated_text} ] \n')

            else:
                caesarCipher.decodingText()
                print(f' THE DECODED TEXT IS: [ {caesarCipher.generated_text} ] \n')

            continueCiphering = input(' WOULD YOU LIKE TO CIPHER TEXT AGAIN?. TYPE [ Y ] TO '
                                      'CIPHER AGAIN. TYPE [ X ] TO CLOSE THE PROGRAM: ').upper()

            if continueCiphering == 'Y':
                # clear the screen
                clear()
                # recursive funct
                CaesarCipherProgram()

            else:
                shouldContinue = False
                # clear
                clear()
                print(' THANK YOU FOR USING CAESAR CIPHER PROGRAM. GOOD BYE .... \n')

# call the function
CaesarCipherProgram()
