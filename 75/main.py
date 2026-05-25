#75	Actualiza datos de un contacto.

agenda = {
    "contactos":[{
        "nombre":"Claudio",
        "telefono":"+56 9 98989898"
    },
    {
        "nombre":"Victor",
        "telefono":"+56 9 87878787"
    }]
}

print(agenda)

agenda['contactos'][0]['nombre'] = "Juan"

print(agenda)

agenda['contactos'].append({
    "nombre":"Pedro",
    "telefono":"+56 9 565656565"
})

print(agenda)