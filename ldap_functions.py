import ldap
import ldap.modlist as modlist
import constants

LDAP_SERVER = '10.244.50.135'
LDAP_SERVER_URI = 'ldap://10.244.50.135:389/'
BIND_DN = 'cn=ldapadm,dc=testldap,dc=local'
LDAP_PREFIX = 'dc='
LDAP_SUFFIX = ',dc=testldap,dc=local'
LDAP_BIND_PASSWORD = 'adg37tup'
LDAP_COMPANY_BASE_SEARCH = 'dc=companies,dc=testldap,dc=local'
LDAP_USER_BASE_SEARCH = 'dc=People,dc=testldap,dc=local'


def search_company(company):
    try:
        ldap_init = ldap.initialize(LDAP_SERVER_URI)
        ldap_init.bind(BIND_DN, LDAP_BIND_PASSWORD)

        criteria = "(o=" + company + ")"
        """
        attibute will needs changing to 'cn'to get the name on live
        """
        attributes = ['o']
        result = ldap_init.search_s(LDAP_COMPANY_BASE_SEARCH,
                                    ldap.SCOPE_SUBTREE, criteria, attributes)

        return result

    finally:
        ldap_init.unbind()


def search_user_name(user):
    try:
        ldap_init = ldap.initialize(LDAP_SERVER_URI)
        ldap_init.bind(BIND_DN, LDAP_BIND_PASSWORD)
        """
        seach dn will need changing when goes live
        """
        criteria = "(uid=" + user + ")"
        attributes = ['uid']
        result = ldap_init.search_s(LDAP_USER_BASE_SEARCH, ldap.SCOPE_SUBTREE,
                                    criteria, attributes)

        if not result:
            return False
        else:
            return True

    finally:
        ldap_init.unbind()


def add_company(company):
    try:
        full_dn = "o=" + company + "," + LDAP_COMPANY_BASE_SEARCH
        company_as_byte = str.encode(company)
        ldap_init = ldap.initialize(LDAP_SERVER_URI)
        ldap_init.bind(BIND_DN, LDAP_BIND_PASSWORD)

        attrs = {}
        attrs['objectClass'] = [b"extensibleObject", b"organization", b"top"]
        attrs['o'] = [company_as_byte]
        """
        attrs['dn'] = [b"company"]
        """
        attrs['cn'] = [company_as_byte]
        attrs['description'] = b"This is a test description"

        ldif = ldap.modlist.addModlist(attrs)
        ldap_init.add_s(full_dn, ldif)

        """
        search for the newly created  user to make sure it now exists
        """
        result = search_company(company)

        if not result:
            return False
        else:
            return True

    finally:
        ldap_init.unbind()


def add_user(username, password, company, firstname, lastname):

    if search_company(company) is not True:
        return "Company Does not exist!"

    elif search_user_name(username) is True:
        return "User already exists!"

    else:
        try:
            ldap_init = ldap.initialize(LDAP_SERVER_URI)
            ldap_init.bind(BIND_DN, LDAP_BIND_PASSWORD)
            company_full_dn = "o=" + company + "," + LDAP_COMPANY_BASE_SEARCH
            """
            full_dn = str.encode("uid=" + username + "," +
                LDAP_USER_BASE_SEARCH)
            """
            full_dn = "uid=" + username + "," + LDAP_USER_BASE_SEARCH
            username = str.encode(username)
            fullname = str.encode(firstname + " " + lastname)
            firstname = str.encode(firstname)
            lastname = str.encode(lastname)
            company = str.encode(company)
            """
            Create the new user object
            """
            """
            ***** LIVE SETTINGS *****
            attrs = {}
            attrs['uid'] = [username]
            attrs['cn'] = [fullname]
            attrs['givenName'] = [firstname]
            attrs['displayName'] = [firstname]
            attrs['sn'] = [lastname]
            attrs['o'] = [company]
            attrs['uid'] = [username]
            attrs['mail'] = [username]
            attrs['objectClass'] = [b'inetOrgPerson', b'account',
                                    b'organizationalPerson', b'person',
                                    b'extensibleObject']
            """
            attrs = {}
            attrs['uid'] = [username]
            attrs['objectClass'] = [b'account', b'top']

            ldif = modlist.addModlist(attrs)
            ldap_init.add_s(full_dn, ldif)

            """
            Add the user to the company
            """
            attrs = {}
            attrs['uniqueMember'] = [full_dn]

            ldif = modlist.modifyModList(attrs)
            ldap_init.modify_s(company_full_dn, ldif)
            """
            Search for newly created user to make sure its added
            """
            result = search_user_name(user)

            if not result:
                return False
            else:
                return True

        finally:
            ldap_init.unbind()


def remove_company(company):
    try:
        ldap_init = ldap.initialize(LDAP_SERVER_URI)
        ldap_init.bind(BIND_DN, LDAP_BIND_PASSWORD)

    finally:
        ldap_init.unbind()



