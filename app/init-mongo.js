
/*
// 1. Rol para solo consultas (read-only)
db.createRole({
  role: "consultor",
  privileges: [
    {
      resource: { db: "myTestDB", collection: "" },
      actions: ["find"],
    },
  ],
  roles: [],
});

// 2. Rol para hacer todo (read-write + admin)
db.createRole({
  role: "administrador",
  privileges: [
    {
      resource: { db: "myTestDB", collection: "" },
      actions: ["find", "insert", "update", "remove", "dropCollection"],
    },
    {
      resource: { db: "myTestDB", collection: "" },
      actions: ["dbAdmin", "userAdmin"],
    },
  ],
  roles: [],
});
*/

db.createUser({
  user: "socies_admin",
  pwd: "socies_password",
  roles: [
    { role: "readWrite", db: "myTestDB" }
  ]
});

db.createUser({
  user: "socies_reader",
  pwd: "reader_password",
  roles: [
    { role: "read", db: "myTestDB" }
  ]
});