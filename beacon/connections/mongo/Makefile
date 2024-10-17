build:
	docker cp data/analyses.json mongoprodspain:tmp/analyses.json
	docker cp data/biosamples.json mongoprodspain:tmp/biosamples.json
	docker cp data/cohorts.json mongoprodspain:tmp/cohorts.json
	docker cp data/datasets.json mongoprodspain:tmp/datasets.json
	docker cp data/genomicVariations.json mongoprodspain:tmp/genomicVariations.json
	docker cp data/individuals.json mongoprodspain:tmp/individuals.json
	docker exec mongoprodspain mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27021/beacon?authSource=admin" --file /tmp/datasets.json --collection datasets
	docker exec mongoprodspain mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27021/beacon?authSource=admin" --file /tmp/individuals.json --collection individuals
	docker exec mongoprodspain mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27021/beacon?authSource=admin" --file /tmp/cohorts.json --collection cohorts
	docker exec mongoprodspain mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27021/beacon?authSource=admin" --file /tmp/analyses.json --collection analyses
	docker exec mongoprodspain mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27021/beacon?authSource=admin" --file /tmp/biosamples.json --collection biosamples
	docker exec mongoprodspain mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27021/beacon?authSource=admin" --file /tmp/genomicVariations.json --collection genomicVariations