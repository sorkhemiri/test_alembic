# ALEMBIC
to create folder structure
```bash
alembic init alembic
```
to create a migration
```bash
alembic revision -m "migration name"
```
+ we can add migration hash in (depends_on) variable
+ every migration refers to the migration before in the file
+ only the last migration hash gets saved

for applying migrations
```bash
alembic upgrade head
```
for reverting one migration
```bash
 alembic downgrade -1
```
for upgrade to a migration
```bash
alembic upgrade migration_hash
```
db url gets defined in alembic.ini and can be parametrized through env.py as shown in example
