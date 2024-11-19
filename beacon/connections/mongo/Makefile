build:
	cp /data/vault/oriol/oriol_beacon_data/pop11_sub2/gv_pop11_sub2_chr22.json data/caseLevelData/genomicVariations.json
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/genomicVariations.json --collection genomicVariations
	cp /data/vault/oriol/oriol_beacon_data/EGAD50000000314/genomicVariations.json data/caseLevelData/genomicVariations.json
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/genomicVariations.json --collection genomicVariations
	cp /data/vault/oriol/oriol_beacon_data/EGAD00001008392/genomicVariations data/caseLevelData/genomicVariations.json
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/genomicVariations.json --collection genomicVariations
	docker exec beaconspreg python /beacon/connections/mongo/reindex.py	
	cp /data/vault/oriol/oriol_beacon_data/pop11_sub2/datasets.json data/caseLevelData/datasets.json
	cp /data/vault/oriol/oriol_beacon_data/pop11_sub2/individuals.json data/caseLevelData/individuals.json
	cp /data/vault/oriol/oriol_beacon_data/pop11_sub2/caseLevelData.json data/caseLevelData/caseLevelData.json
	cp /data/vault/oriol/oriol_beacon_data/pop11_sub2/targets.json data/caseLevelData/targets.json
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/datasets.json --collection datasets
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/individuals.json --collection individuals
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/caseLevelData.json --collection caseLevelData
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/targets.json --collection targets
	cp /data/vault/oriol/oriol_beacon_data/EGAD50000000314/analyses.json data/caseLevelData/analyses.json
	cp /data/vault/oriol/oriol_beacon_data/EGAD50000000314/biosamples.json data/caseLevelData/biosamples.json
	cp /data/vault/oriol/oriol_beacon_data/EGAD50000000314/cohorts.json data/caseLevelData/cohorts.json
	cp /data/vault/oriol/oriol_beacon_data/EGAD50000000314/datasets.json data/caseLevelData/datasets.json
	cp /data/vault/oriol/oriol_beacon_data/EGAD50000000314/individuals.json data/caseLevelData/individuals.json
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/datasets.json --collection datasets
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/individuals.json --collection individuals
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/analyses.json --collection analyses
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/biosamples.json --collection biosamples
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/cohorts.json --collection cohorts
	cp /data/vault/oriol/oriol_beacon_data/EGAD00001008392/biosamples.json data/caseLevelData/biosamples.json
	cp /data/vault/oriol/oriol_beacon_data/EGAD00001008392/cohorts.json data/caseLevelData/cohorts.json
	cp /data/vault/oriol/oriol_beacon_data/EGAD00001008392/datasets.json data/caseLevelData/datasets.json
	cp /data/vault/oriol/oriol_beacon_data/EGAD00001008392/individuals.json data/caseLevelData/individuals.json
	cp /data/vault/oriol/oriol_beacon_data/EGAD00001008392/runs.json data/caseLevelData/runs.json
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/datasets.json --collection datasets
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/individuals.json --collection individuals
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/biosamples.json --collection biosamples
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/cohorts.json --collection cohorts
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