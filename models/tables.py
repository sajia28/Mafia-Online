# Define your tables below (or better in another model file) for example
#
# >>> db.define_table('mytable', Field('myfield', 'string'))
#
# Fields can be 'string','text','password','integer','double','boolean'
#       'date','time','datetime','blob','upload', 'reference TABLENAME'
# There is an implicit 'id integer autoincrement' field
# Consult manual for more options, validators, etc.

db.define_table('player',
                Field('user_email', default=get_user_email()),
                Field('bio', 'text'),
                Field('current_game'),
                Field('role'),
                Field('is_dead', 'boolean', default=False),
                Field('image', 'upload', uploadfield='image_file'),
                Field('image_file', 'blob')
)
db.define_table('game',
               Field('id'),
               Field('turn'),
               Field('phase'),
               Field('num_players')
)


# after defining tables, uncomment below to enable auditing
# auth.enable_record_versioning(db)