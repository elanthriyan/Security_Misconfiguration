def get_user_data(role: str):
    """
    Improper trust in client-controlled role
    """
    if role == "admin":
        return {
            "username": "administrator",
            "permissions": ["read", "write", "delete"],
            "flag": "SMC{r0l3_tru5t_f41l_2aa9}"
        }

    return {
        "username": "guest",
        "permissions": ["read"]
    }
