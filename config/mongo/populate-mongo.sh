mongo -- "$MONGO_INITDB_DATABASE" <<EOF
    db.user.insert({"_id": ObjectId("5c9ccc140aee604c4ab6cd06"), "user_id": "105398890", "pin": 2091, "user_name": "playvox", "password": "pl4yv0x", "create_date": ISODate("2021-03-06 01:37:14.422Z")})
    db.user.insert({"_id": ObjectId("5c9ccc140aee604c4ab6cd07"), "user_id": "105398891", "pin": 2090, "user_name": "docker", "password": "d0ck3r", "create_date": ISODate("2021-03-06 01:57:14.422Z")})
EOF