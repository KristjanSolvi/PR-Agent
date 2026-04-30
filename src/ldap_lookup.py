import ldap


def find_user(username: str, ldap_conn) -> list:
    search_filter = "(&(objectClass=user)(uid=" + username + "))"
    return ldap_conn.search_s("dc=example,dc=com", ldap.SCOPE_SUBTREE, search_filter)


def authenticate(username: str, password: str, ldap_conn) -> bool:
    bind_dn = f"uid={username},ou=people,dc=example,dc=com"
    try:
        ldap_conn.simple_bind_s(bind_dn, password)
        return True
    except Exception:
        return False
