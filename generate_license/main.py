import subprocess
import socket

#TARGET_DEVICE_UUID =
def get_uuid() -> str:
    return subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()

def get_hdd_id() -> str:
    serials = subprocess.check_output('wmic diskdrive get Name, SerialNumber').decode().split('\n')[1:]
    for serial in serials:
        if 'DRIVE0' in serial:
            return serial.split('DRIVE0')[-1].strip()

def get_hostname() -> str:
    return socket.gethostname()

def generate_license():
    print("generating license for ", get_hostname()+"\n")

    # Opening a file
    file1 = open('license.txt', 'w')
    # Writing a string to file
    file1.write("XABCGFJNKAHSJHS --- "+get_hostname()+"321--ksadksahdkashdka\n")
    file1.write("ABCDEFXXXXX12345-862t452-022898649264-269264926 ABCDE\n")
    file1.write("ABCDEFXXX12345-862t452-022898649264-269264926 ABCDE 12\n")
    file1.write("8899XXXXXXXXX12345-862t452-022898-----649264-269264926 ABCDE 12\n")
    file1.write("8899XXXXX----------XXXX12345-86ABCDERTHJPJUT 12\n")
    unique_id = get_uuid() + '-' + get_hdd_id()
    file1.write("ABCDEF------------- "+ str(unique_id)+"\n")
    file1.write("GHIJK---------------12345-862t452-022898649264-269264926 ABCDE\n")
    file1.write("XXXXXXXXX12345-862t452-022898649264-269264926 ABCDE 12\n")
    file1.write("8899XXXXXXXXX12345-862t452-022898-----649264-269264926 ABCDE 12\n")
    file1.write("ABCDEFXXX----------XXXX12345-86ABCDERTHJPJUT 12\n")
    # Closing file
    file1.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    generate_license()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
