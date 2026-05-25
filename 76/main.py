#76	Elimina un contacto.

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

agenda["contactos"].remove({
        "nombre":"Claudio",
        "telefono":"+56 9 98989898"
    })
print(agenda)

agenda["contactos"].pop(0)

print(agenda)