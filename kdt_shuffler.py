#!/usr/bin/python
import sys
import random

if len(sys.argv) < 2:
    print('Usage: python password_locker.py [account] - copy account password')
    sys.exit()

members_list_fname      = sys.argv[1]
num_of_members_per_rota = int(sys.argv[2])

in_fhandle  = open(members_list_fname, 'r')
all_members = in_fhandle.read().splitlines()
in_fhandle.close()

random.shuffle(all_members)

out_fhandle = open('shuffled_surname_list.txt', 'w')

for surname in all_members:
    # cap_surname = surname.capitalize()
    cap_surname = surname
    out_fhandle.write(cap_surname + ' ')
    if all_members.index(surname) % num_of_members_per_rota == (num_of_members_per_rota-1):
        out_fhandle.write('\n')

out_fhandle.close()
