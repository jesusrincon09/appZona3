def get_grouped_permissions(permission_queryset, modules):
    grouped = {}
    permissions = {p.codename: p for p in permission_queryset}

    for module in modules:
        module_name = module["name"]
        grouped[module_name] = []

        for perm in module["permissions"]:
            codename = perm["codename"]
            if codename in permissions:
                permission = permissions[codename]
                permission.display_name = perm["name"]
                grouped[module_name].append(permission)

    return grouped