import datetime
import random
import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description='Generates random NRN.')
    parser.add_argument('--check', dest='nrn', help='Check if an NRN is valid.')
    return parser.parse_args()


def check_nrn(nrn: str):
    year = int(nrn[0:2])
    month = int(nrn[2:4])
    day = int(nrn[4:6])

    valid = True

    if month <= 0 or month > 12:
        valid = False

    if day <= 0 or day > 31:
        valid = False

    if valid:
        base18xx__19xx = int(nrn[0:9])
        base20xx = int(f'2{nrn[0:9]}')
        checksum = int(nrn[9:11])
        actual_year = 0

        if checksum == 97 - (base18xx__19xx % 97):
            actual_year = 1900 + year
        elif checksum == 97 - (base20xx % 97):
            actual_year = 2000 + year
        else:
            valid = False

        if valid:
            try:
                eighteenth_birthday = datetime.datetime(actual_year + 18, month, day)
                valid = datetime.datetime.now() >= eighteenth_birthday
            except:
                valid = False

    return valid


def generate_valid_nrn():
    valid_found = False
    while not valid_found:
        potential_correct_nrn = str(random.randint(40101032178, 99101032178))
        valid_found = check_nrn(potential_correct_nrn)
        if valid_found:
            return potential_correct_nrn


if __name__ == '__main__':
    arguments = parse_arguments()

    if arguments.nrn is not None:
        if check_nrn(arguments.nrn):
            print(f'{arguments.nrn} is valid.')
        else:
            print(f'{arguments.nrn} is not valid.')
    else:
        valid_nrn = generate_valid_nrn()
        print(valid_nrn)
