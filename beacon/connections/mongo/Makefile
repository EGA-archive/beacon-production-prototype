build:
	zcat /data/landing/vault/oriol/oriol_beacon_data/pop11_sub2/gv_pop11_sub2_chr22.json.gz > data/caseLevelData/genomicVariations.json
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/genomicVariations.json --collection genomicVariations

	zcat /data/landing/vault/oriol/oriol_beacon_data/EGAD50000000314/genomicVariations.json.gz > data/caseLevelData/genomicVariations.json
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/genomicVariations.json --collection genomicVariations

	zcat /data/landing/vault/oriol/oriol_beacon_data/EGAD00001008392/genomicVariations.json.gz > data/caseLevelData/genomicVariations.json
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/genomicVariations.json --collection genomicVariations

	docker exec beaconspreg python /beacon/connections/mongo/reindex.py	

	zcat /data/landing/vault/oriol/oriol_beacon_data/pop11_sub2/datasets.json.gz > data/caseLevelData/datasets.json
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/datasets.json --collection datasets

	zcat /data/landing/vault/oriol/oriol_beacon_data/pop11_sub2/individuals.json.gz > data/caseLevelData/individuals.json
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/individuals.json --collection individuals

	zcat /data/landing/vault/oriol/oriol_beacon_data/pop11_sub2/caseLevelData.json.gz > data/caseLevelData/caseLevelData.json
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/caseLevelData.json --collection caseLevelData

	zcat /data/landing/vault/oriol/oriol_beacon_data/pop11_sub2/targets.json.gz > data/caseLevelData/targets.json
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/targets.json --collection targets

	zcat /data/landing/vault/oriol/oriol_beacon_data/EGAD50000000314/analyses.json.gz > data/caseLevelData/analyses.json
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/analyses.json --collection analyses

	zcat /data/landing/vault/oriol/oriol_beacon_data/EGAD50000000314/biosamples.json.gz > data/caseLevelData/biosamples.json
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/biosamples.json --collection biosamples

	zcat /data/landing/vault/oriol/oriol_beacon_data/EGAD50000000314/cohorts.json.gz > data/caseLevelData/cohorts.json
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/cohorts.json --collection cohorts

	zcat /data/landing/vault/oriol/oriol_beacon_data/EGAD50000000314/datasets.json.gz > data/caseLevelData/datasets.json
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/datasets.json --collection datasets

	zcat /data/landing/vault/oriol/oriol_beacon_data/EGAD50000000314/individuals.json.gz > data/caseLevelData/individuals.json
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/individuals.json --collection individuals

	zcat /data/landing/vault/oriol/oriol_beacon_data/EGAD00001008392/biosamples.json.gz > data/caseLevelData/biosamples.json
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/biosamples.json --collection biosamples

	zcat /data/landing/vault/oriol/oriol_beacon_data/EGAD00001008392/cohorts.json.gz > data/caseLevelData/cohorts.json
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/cohorts.json --collection cohorts

	zcat /data/landing/vault/oriol/oriol_beacon_data/EGAD00001008392/datasets.json.gz > data/caseLevelData/datasets.json
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/datasets.json --collection datasets

	zcat /data/landing/vault/oriol/oriol_beacon_data/EGAD00001008392/individuals.json.gz > data/caseLevelData/individuals.json
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/individuals.json --collection individuals

	zcat /data/landing/vault/oriol/oriol_beacon_data/EGAD00001008392/runs.json.gz > data/caseLevelData/runs.json
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/runs.json --collection runs

	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file /data/datasets.json --collection datasets
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file /data/individuals.json --collection individuals
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file /data/analyses.json --collection analyses
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file /data/biosamples.json --collection biosamples
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file /data/cohorts.json --collection cohorts
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file /data/runs.json --collection runs
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file /data/genomicVariations.json --collection genomicVariations
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file /data/caseLevelData.json --collection caseLevelData
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file /data/targets.json --collection targets

	docker exec beaconspreg python /beacon/connections/mongo/reindex.py
	docker exec beaconspreg python beacon/connections/mongo/extract_filtering_terms.py