import ldap


def find_user(username: str, ldap_conn) -> list:
    safe_username = ldap.filter.escape_filter_chars(username)
    search_filter = f"(&(objectClass=user)(uid={safe_username}))"
    return ldap_conn.search_s("dc=example,dc=com", ldap.SCOPE_SUBTREE, search_filter)


def authenticate(username: str, password: str, ldap_conn) -> bool:
    safe_rdn = ldap.dn.escape_dn_chars(username)
    bind_dn = f"uid={safe_rdn},ou=people,dc=example,dc=com"
    try:
        ldap_conn.simple_bind_s(bind_dn, password)
        return True
    except Exception:
        return False
