# target: help - Display callable targets
help:
	@egrep "^# target:" [Mm]akefile


# target: clean - Clean all ".pyc" files
clean:
	find . -name "*.pyc" -exec rm -rf {} \;


# target: migrate - Migrate all django applications considering app dependencies
migrate:
	python fastlink/manage.py makemigrations fastlink
	python fastlink/manage.py migrate


# target: clean_migration - folders in all django apps
clean_migrations:
	ls fastlink/ | grep -v -e 'manage.py' | xargs -I{} rm -rf fastlink/{}/migrations/
