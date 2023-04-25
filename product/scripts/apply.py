from yoyo import read_migrations, get_backend

backend = get_backend('mysql://root:@mysql/product')
migrations = read_migrations('../migrations')
backend.apply_migrations(backend.to_apply(migrations))