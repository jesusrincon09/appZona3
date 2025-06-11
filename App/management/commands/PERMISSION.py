MODULES = [
    {
        "name": "Deportes",
        "name_url": "sport_list",
        "icon": "fas fa-football-ball",
        "permissions": [
            {"codename": "list_sport", "name": "Listar Deportes"},
            {"codename": "add_sport", "name": "Crear Deporte"},
            {"codename": "edit_sport", "name": "Editar Deporte"},
            {"codename": "delete_sport", "name": "Eliminar Deporte"},
        ],
    },
    {
        "name": "Horarios",
        "name_url": "schedules_list",
        "icon": "far fa-calendar-alt",
        "permissions": [
            {"codename": "list_schedul", "name": "Listar Horarios"},
            {"codename": "add_schedul", "name": "Crear Horarios"},
            {"codename": "edit_schedul", "name": "Editar Horario"},
            {"codename": "delete_schedul", "name": "Eliminar Horario"},
        ],
    },
    {
        "name": "Empresa",
        "name_url": "company_create",
        "icon": "fas fa-home",
        "permissions": [
            {"codename": "add_company", "name": "Crear Empresa"},
            {"codename": "edit_company", "name": "Editar Empresa"},
        ],
    },
    {
        "name": "Espacios",
        "name_url": "spaces_list",
        "icon": "fab fa-fort-awesome",
        "permissions": [
            {"codename": "list_spaces", "name": "Listar Espacios"},
            {"codename": "add_spaces", "name": "Crear Espacio"},
            {"codename": "edit_spaces", "name": "Editar Espacio"},
            {"codename": "delete_spaces", "name": "Eliminar Espacio"},
        ],
    },
    {
        "name": "Reservas",
        "name_url": "reservation_list",
        "icon": "fas fa-concierge-bell",
        "permissions": [
            {"codename": "list_reservation", "name": "Listar Reservas"},
            {"codename": "add_reservation", "name": "Crear Reservas"},
            {"codename": "edit_reservation", "name": "Editar Reservas"},
            {"codename": "delete_reservation", "name": "Eliminar Reservas"},
        ],
    },
    {
        "name": "Usuarios",
        "name_url": "user_list",
        "icon": "fas fa-user",
        "permissions": [
            {"codename": "list_users", "name": "Listar Usuarios"},
            {"codename": "add_user", "name": "Crear Usuario"},
            {"codename": "permision", "name": "Gestionar Permisos"},
            {"codename": "edit_user", "name": "Editar Usuario"},
            {"codename": "delete_user", "name": "Eliminar Usuario"},
        ],
    },
    {
        "name": "Roles",
        "name_url": "role_list",
        "icon": "fas fa-user-cog",
        "permissions": [
            {"codename": "list_rol", "name": "Listar Roles"},
            {"codename": "add_rol", "name": "Crear Rol"},
            {"codename": "edit_rol", "name": "Editar Rol"},
            {"codename": "delete_rol", "name": "Eliminar Rol"},
        ],
    },
    {
        "name": "Logs",
        "name_url": "logs_list",
        "icon": "fas fa-file-alt",
        "permissions": [
            {"codename": "list_logs", "name": "Listar Logs"},
        ],
    },
]
