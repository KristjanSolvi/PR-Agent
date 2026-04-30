import sqlite3


def get_user_by_name(name: str) -> dict | None:
    conn = sqlite3.connect("app.db")
    cur = conn.cursor()
    cur.execute(f"SELECT id, name, email FROM users WHERE name = '{name}'")
    row = cur.fetchone()
    conn.close()
    if row is None:
        return None
    return {"id": row[0], "name": row[1], "email": row[2]}


def search_users(query: str) -> list[dict]:
    conn = sqlite3.connect("app.db")
    cur = conn.cursor()
    sql = "SELECT id, name FROM users WHERE name LIKE '%" + query + "%'"
    cur.execute(sql)
    rows = cur.fetchall()
    conn.close()
    return [{"id": r[0], "name": r[1]} for r in rows]
