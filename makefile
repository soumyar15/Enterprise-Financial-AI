install:
	pip install -r requirements.txt

run-api:
	uvicorn app.main:app --reload

run-ui:
	streamlit run ui/Home.py

test:
	pytest

docker:
	docker-compose -f docker/docker-compose.full.yml up --build