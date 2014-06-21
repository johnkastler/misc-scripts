#!/usr/bin/env python

"""
pulls some basic data for an opsworks user as imported from IAM
"""

from boto import connect_opsworks
from keyring import get_password

accounts = {'aws-dev': 'XXXXXXXXXXXXXXXXXXXX',
            'aws-qa': 'XXXXXXXXXXXXXXXXXXXX',
            'aws-staging': 'XXXXXXXXXXXXXXXXXXXX',
            'aws-demo': 'XXXXXXXXXXXXXXXXXXXX',
            'aws-prod': 'XXXXXXXXXXXXXXXXXXXX'}

def OpsWorksConn(account, id):
    key = get_password(account, id)
    conn = connect_opsworks(id, key)
    return(conn)

for account in accounts:
    id = accounts[account]
    conn = OpsWorksConn(account, id)
    profiles = conn.describe_user_profiles().get('UserProfiles')
    for profile in profiles:
        name = profile.get('SshUsername')    
        selfman = profile.get('AllowSelfManagement')
        sshkey = profile.get('SshPublicKey')
        
        print("{0}, {3}, Self-Manage: {1}, SSH Key: {2}".format(name, selfman, sshkey, account))
