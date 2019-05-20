dev:
	@echo "run dev"
	cd app && flask run

prod:
	@echo "run production"
	cd app && flask run -h 0.0.0.0
	
docker:
	@echo build docker and start container
	docker build -t backend .
	docker run -i -p 5000:5000 backend
	
test:
	@echo "run test"
	cd app && flask test

init:
	@echo "init database..."
	cd app && flask db init

updateDB:
	@echo "migrate database table..."
	cd app && flask db migrate --message '$(message)'
	@echo "upgrade database..."
	cd app && flask db upgrade

upgradeDB:
	@echo "upgrade database..."
	cd app && flask db upgrade
	
clean-pyc:
	find . -name "*.pyc" -exec rm -f {} \;
