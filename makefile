generate:
	./prisma/scripts/generate.sh lang=python

dev:
	uvicorn app.main:app --reload