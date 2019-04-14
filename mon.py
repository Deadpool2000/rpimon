import os
try:
    print("""
    ##############################################################################

               Monitor mode for Raspberry Pi 3 B/B+,Zero W On Raspbian OS

    ##############################################################################\n
    """)
    print("Warning! Please take a backup of your system before installation.\nYour system may corrupted while installation! So be careful!")
    # Upadating
    print("Installing Dependencies.......................\n")
    os.system("sudo apt-get update")
    os.system("sudo apt-get install aircrack-ng tar wget -y")

    # Installing Re4son kernel in Raspbian
    # Downloading tar
    PATH=os.path.isfile("/usr/local/src/re4son-kernel_current.tar.xz")
    print("\nDownloading tar....................\n")
    if PATH==True:
        print("File already exist! Skipping download..................\n")
    else:
        os.system("sudo wget -O /usr/local/src/re4son-kernel_current.tar.xz https://re4son-kernel.com/download/re4son-kernel-current/")

    # Extracting
    print("\nExtracting................................\n")
    os.system("tar -xJf /usr/local/src/re4son-kernel_current.tar.xz -C /usr/local/src")
    print("\nExtraction suucessfull!\n")
    print("""
    ######################################################################################

                     Now take a cup of tea/coffee until complete installation :)

    ######################################################################################\n""")

    # Installation
    os.system("cd /usr/local/src/re4son-kernel_4.14* && chmod +x install.sh && ./install.sh")
    os.system("sudo rm /usr/local/src/re4son-kernel_current.tar.xz")
    print("""
    #######################################################################################

                   Succeed! Now start monitor mode by typing 'sudo mon0 up'
              
    ########################################################################################

                                     Script By:Deadpool007
                              
    ########################################################################################                    
    """)
except KeyboardInterrupt:
    print("Interrupted! Have a nice day :)")
