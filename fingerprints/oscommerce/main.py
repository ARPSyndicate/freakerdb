import os
import sys

if __name__ == "__main__":
    os.system('echo "\nTARGET: {0}\n" | tee -a {1}'.format(sys.argv[1], sys.argv[2]))
    os.system("bash fingerprint.sh {0} | tee -a {1}".format(sys.argv[1], sys.argv[2]))