generate:
	python -m app.scripts.generate_openapi_schema

dev:
	uvicorn app.main:app --reload