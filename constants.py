"""
LDAP Settings
"""
LDAP_SERVER = '10.244.50.135'
LDAP_SERVER_URI = 'ldap://LDAP_SERVER'
BIND_DN = 'cn=ldapadm,dc=testldap,dc=local'
LDAP_PREFIX = 'dc='
LDAP_SUFFIX = ',dc=testldap,dc=local'
LDAP_BIND_USER = 'cn=ldapadm,dc=testldap,dc=local'
LDAP_BIND_PASSWORD = 'adg37tup'
LDAP_BASE_DN = 'dc=companies,dc=testldap,local'
QUERY_PREFIX = ''
QUERY_SUFFIX = ''

"""
Forms Class Settings
"""
dropdown = [('searchcompany', 'search company'), ('searchuser', 'search user'),
            ('adduser', 'add user'), ('addcompany', 'add company'),
            ('removeuser', 'remove user')]