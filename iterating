#!/usr/bin/env python3.7

users = [{'admin': True, 'active': True, 'name': 'Vlad'},
 {'admin': False, 'active': True, 'name': 'Ostin'},
 {'admin': False, 'active': False, 'name': 'Segj'}]

count = 0
for user in users:
    name = user['name']
    is_active = user['active']
    is_admin = user['admin']
    
    if is_admin and is_active:
            print (f'{count}. ' + name + ' ACTIVE-(ADMIN)')
    elif is_admin:
        print(f'{count}. ' + name + ' (ADMIN)')
    elif is_active:
        print (f'{count}. ' + name + ' ACTIVE')
    else:
        print(f'{count}. ' + name)
    count += 1
