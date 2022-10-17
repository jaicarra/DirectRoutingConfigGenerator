

from platform import platform

search_text1 = "sbc.example.com"
search_text2 = "ISR4321"
search_text3 = "192.0.2.2"
search_text4 = "cube-priv-ip"
search_text5 = "nat-ext-ip"

hostname = input("Enter the  hostname of the Router:")
print("hostname  is: " + hostname)

domain = input("Enter the  domain of the Router:")
print("The domain  is: " + domain)

print("Please enter one of the platform options  listed here")
platform = ["ISR1100", "ISR4321", "ISR4331", "ISR4351", "ISR4431", "ISR4451-X", "ISR4461", "Catalyst 8000V",
            "Catalyst 8200", "Catalyst 8300", "ASR1001-X", "ASR1002-X", "ASR1004", "ASR1006/RP2", "ASR1006/RP3"]

print(platform)
routerPlatform1 = ""
while routerPlatform1 not in platform:
    routerPlatform1 = input("What is the platform of the Router ? ")
sqdn = hostname + "." + domain
print("The SQDN of the router is " + sqdn)

cube_routing = {"1": "CUBE should work with a public ip address",
                "2": "CUBE should work  with a nated ip address"}

print(cube_routing)
CUBE_deployment_Model = input("How signaling should travers ?  ")
if CUBE_deployment_Model == "1":
    publicIp = input(" What is the CUBE public ip address ")
    replace_text1 = str(sqdn)
    replace_text2 = str(routerPlatform1)
    replace_text3 = str(publicIp)
    # I would implement a swithc case for opening the file that contains the config example
# Config example where constructed based on signal traverse mode and media traversing mode.
    with open('publicIpNoMediaBypass.txt') as file_object:
        # Opening our text file in read only
        # mode using the open() function
        main_file = file_object.read()

    # Searching and replacing the text
    # using the replace() function
        main_file = main_file.replace(search_text1, replace_text1)
        main_file = main_file.replace(search_text2, replace_text2)
        main_file = main_file.replace(search_text3, replace_text3)

# Opening our text file in write only
# mode to write the replaced content
    with open(r'publicIpNoMediaBypass_New.txt', 'w') as file_object:

        # Writing the replaced data in our
        # text file
        file_object.write(main_file)

    # Printing Text replaced
        print("New file was created and this  contains your direct routing configuraiton ")
        f = open('publicIpNoMediaBypass_New.txt', "r")
        print(f.read())

elif CUBE_deployment_Model == "2":
    natedIP = input("What is the CUBE nated ip address ")
    privadeIP = input("What is the CUBE private ip address ")

    replace_text1 = str(sqdn)
    replace_text2 = str(routerPlatform1)
    replace_text4 = str(privadeIP)
    replace_text5 = str(natedIP)

    # Config example where constructed based on signal traverse mode and media traversing mode.
    with open('behindNatNoMediaBypass.txt') as file_object:
        # Opening our text file in read only
        # mode using the open() function
        main_file = file_object.read()

    # Searching and replacing the text
    # using the replace() function
        main_file = main_file.replace(search_text1, replace_text1)
        main_file = main_file.replace(search_text2, replace_text2)
        main_file = main_file.replace(search_text4, replace_text4)
        main_file = main_file.replace(search_text5, replace_text5)

# Opening our text file in write only
# mode to write the replaced content
    with open(r'behindNatNoMediaBypass_New.txt', 'w') as file_object:

        # Writing the replaced data in our
        # text file
        file_object.write(main_file)

    # Printing Text replaced
        print("New file was created and this  contains your direct routing configuraiton ")
        f = open('behindNatNoMediaBypass_New.txt', "r")
        print(f.read())
