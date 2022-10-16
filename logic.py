

from platform import platform

hostname = input("Enter the  hostname of the Router:")
print("hostname  is: " + hostname)

domain = input("Enter the  domain of the Router:")
print("The domain  is: " + domain)

sqdn = hostname + "." + domain
print("The SQDN of the router is " + sqdn)
publicIp = input("What is the CUBE Public IP address ?  ")
print("The CUBE public IP addres is : " + publicIp)

print("Please enter one the platform listed here")
platform = ["ISR1100", "ISR4321", "ISR4331", "ISR4351", "ISR4431", "ISR4451-X", "ISR4461", "Catalyst 8000V",
            "Catalyst 8200", "Catalyst 8300", "ASR1001-X", "ASR1002-X", "ASR1004", "ASR1006/RP2", "ASR1006/RP3"]

print(platform)

routerPlatform1 = input("What is the platform of the Router ? ")

print("The platform of the router is: " + routerPlatform1)

search_text1 = "sbc.example.com"
search_text2 = "ISR4321"
search_text3 = "192.0.2.2"
replace_text1 = str(sqdn)
replace_text2 = str(routerPlatform1)
replace_text3 = str(publicIp)

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
print("This is are the values of your new direct routing deployment")
f = open('publicIpNoMediaBypass_New.txt', "r")
print(f.read())
