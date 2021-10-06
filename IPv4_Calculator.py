#       Program:                IPv4_Calculator.py
#       Date:                   7/Mar/2020
#       Author:                 Oluwatosin Fletcher
#       Description:            This Program breaks down IPv4 address


octet = []
prefix = []
temp = ""
print("IPv4 Break Down Program")
print("#" * 73)

while True:
    ipaddress = input(
        "Please enter an IPv4 Address and prefix (#.#.#.#/MM): ")  # Promt the user to enter a valid IP Address

    for char in ipaddress:
        if char != "." and char != "/":  # Loop through the IP Address, Exclude the "." and "/" sign and save the number in the variable temp.
            temp += char

        else:
            octet.append(int(temp))  # Add the IP address from the variable temp into the variable octet.
            temp = ""

    else:
        prefix.append(int(temp))  # Add the prefix after the "/" sign into the variable prefix
        temp = ""

    if " " in ipaddress:  # If there is a space in the IP Address entered, prompt the user to enter the correct IP address format
        print("- The correct format is [0-255].[0-255].[0-255].[0-255]/[8-31] Mask")
        print("- Example: 192.168.2.1/24 (no spaces)\n")
        octet = []  # Reset the octet list to empty after each error prompt
        prefix = []  # Reset the prefix list to empty after each error prompt

        continue


    elif octet == octet[
                  :3]:  # If users does not input the complete IP address by including the prefix, this will prompt the user input the correct IP format.
        print("- The correct format is [0-255].[0-255].[0-255].[0-255]/[8-31] Mask")
        print("- Example: 192.168.2.1/24 (no spaces)\n")
        octet = []  # Reset the octet list to empty after each error prompt
        prefix = []  # Reset the prefix list to empty after each error prompt

    elif octet[0] < 0 or octet[
        0] > 255:  # if the first octect is less than 0 or greater than 255, this will prompt the user to input the correct IP format.
        print("- The correct format is [0-255].[0-255].[0-255].[0-255]/[8-31] Mask")
        print("- Example: 192.168.2.1/24 (no spaces)\n")
        octet = []  # Reset the octet list to empty after each error prompt
        prefix = []  # Reset the prefix list to empty after each error prompt

    elif octet[1] < 0 or octet[
        1] > 255:  # if the second octet is less than 0 or greater than 255, this will promt the user to input the correct IP format
        print("- The correct format is [0-255].[0-255].[0-255].[0-255]/[8-31] Mask")
        print("- Example: 192.168.2.1/24 (no spaces)\n")
        octet = []  # Reset the octet list to empty after each error prompt
        prefix = []  # Reset the prefix list to empty after each error prompt

    elif octet[2] < 0 or octet[
        2] > 255:  # if the third octet is less than 0 or greater than 255, this will promt the user to input the correct IP format
        print("- The correct format is [0-255].[0-255].[0-255].[0-255]/[8-31] Mask")
        print("- Example: 192.168.2.1/24 (no spaces)\n")
        octet = []  # Reset the octet list to empty after each error prompt
        prefix = []  # Reset the prefix list to empty after each error prompt

    elif octet[3] < 0 or octet[
        3] > 255:  # if the forth octet is less than 0 or greater than 255, this will promt the user to input the correct IP format
        print("- The correct format is [0-255].[0-255].[0-255].[0-255]/[8-31] Mask")
        print("- Example: 192.168.2.1/24 (no spaces)\n")
        octet = []  # Reset the octet list to empty after each error prompt
        prefix = []  # Reset the prefix list to empty after each error prompt

    elif prefix[0] < 8 or prefix[
        0] > 31:  # if the prefix entered is less than 8 or greater than 31, this will promt the user to input the correct IP format
        print("- The correct format is [0-255].[0-255].[0-255].[0-255]/[8-31] Mask")
        print("- Example: 192.168.2.1/24 (no spaces)\n")
        octet = []  # Reset the octet list to empty after each error prompt
        prefix = []  # Reset the prefix list to empty after each error prompt


    else:
        break

one = "1"
zero = "0"
network_bits = one * prefix[0]  # Network bits in string
length_host_bits = 32 - prefix[0]  # Total number of host bits (length)
host_bits = zero * length_host_bits  # Host bits in string
subnet_mask = network_bits + host_bits  # Concatenate the strings of network bits + the host bits

first_octet = subnet_mask[
              :8]  # Assign the first string of eight bits to the variable first_octet by using the slice syntax
second_octet = subnet_mask[
               8:16]  # Assign the second string of eight bits to the variable second_octet by using the slice syntax
third_octet = subnet_mask[
              16:24]  # Assign the third string of eight bits to the variable third_octet by using the slice syntax
forth_octet = subnet_mask[
              24:]  # Assign the forth string of eight bits to the variable forth_octet by using the slice syntax

print("\nFor the provided IP Address and Prefix.")
print("The IP Address you entered was ", octet[0], ".", octet[1], ".", octet[2], ".", octet[3], "\n", sep="")

first_octet = int(first_octet, 2)  # Convert the binary bits of each octet to a base 2 decimal
second_octet = int(second_octet, 2)
third_octet = int(third_octet, 2)
forth_octet = int(forth_octet, 2)

first_anding = octet[0] & first_octet  # Calculate the network address.
second_anding = octet[1] & second_octet  # Using the bitwise ANDing method, We take the IP address and use it to
third_anding = octet[2] & third_octet  # perform the bitwise conjuction operation against the subnetmask.
forth_anding = octet[3] & forth_octet

print("This IP belongs to the network ", first_anding, ".", second_anding, ".", third_anding, ".", forth_anding, sep="")
print("- The Subnet mask would be ", first_octet, ".", second_octet, ".", third_octet, ".", forth_octet, "\n", sep="")

num_of_host = 2 ** len(host_bits) - 2  # Calculates the number of host allowed on the network.
first_useable_octet4 = int(forth_anding + 1)  # Calculates last octet in the first useable address.

print("The number of hosts allowed on this network is", num_of_host)
print("- The First Address would be ", first_anding, ".", second_anding, ".", third_anding, ".", first_useable_octet4,
      sep="")

wildcard = ""  # Create an empty variable and name it wildcard

for i in subnet_mask:  # Loop through the subnet_mask and flip all the 1's bits to 0's and the 0's bits to 1's
    if i == "1":
        wildcard += "0"  # When i in subnet_mask is 1, replace it with a string of zero's and add it to the variable wildcard.

    else:
        wildcard += "1"  # When i in subnet_mask is 0, replace it with a string of one's and add it to the variable wildcard.

oct1_wildcard = wildcard[:8]  # We divide the wildcard into four octets by using the slice syntax
oct2_wildcard = wildcard[8:16]
oct3_wildcard = wildcard[16:24]
oct4_wildcard = wildcard[24:]

oct1_wildcard = int(oct1_wildcard, 2)  # Convert the binary bits of each octets to a base 2 decimal.
oct2_wildcard = int(oct2_wildcard, 2)
oct3_wildcard = int(oct3_wildcard, 2)
oct4_wildcard = int(oct4_wildcard, 2)

first_anding = first_anding ^ oct1_wildcard  # We Calculate each octet of the broadcast address using the
second_anding = second_anding ^ oct2_wildcard  # bitwise exclusive or (Xor) operator. We take the value of each
third_anding = third_anding ^ oct3_wildcard  # octet in the network address and use it to perform the bitwise Xor operation against the
forth_anding = forth_anding ^ oct4_wildcard  # the value of each octet in the wildcard address.

last_useable_oct4 = forth_anding - 1  # The forth octet of the last usable address can be calculated by subtracting 1 from the forth octet of the broadcast address.

print("- The Last Address would be ", first_anding, ".", second_anding, ".", third_anding, ".", last_useable_oct4,
      sep="")
print("- The Network Broadcast Address would be ", first_anding, ".", second_anding, ".", third_anding, ".", forth_anding, sep="")

print("#" * 73)
print("This application is courtesy of: Oluwatosin Fletcher")
print("#" * 73)
close = input("Press Enter to exit the application\n")