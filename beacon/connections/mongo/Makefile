build:
	gunzip /data/vault/oriol/oriol_beacon_data/pop11_sub2/gv_pop11_sub2_chr22.json.gz
	cp /data/vault/oriol/oriol_beacon_data/pop11_sub2/gv_pop11_sub2_chr22.json data/caseLevelData/genomicVariations.json
	rm /data/vault/oriol/oriol_beacon_data/pop11_sub2/gv_pop11_sub2_chr22.json
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/genomicVariations.json --collection genomicVariations
	gunzip /data/vault/oriol/oriol_beacon_data/EGAD50000000314/genomicVariations.json.gz
	cp /data/vault/oriol/oriol_beacon_data/EGAD50000000314/genomicVariations.json data/caseLevelData/genomicVariations.json
	rm  /data/vault/oriol/oriol_beacon_data/EGAD50000000314/genomicVariations.json
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/genomicVariations.json --collection genomicVariations
	gunzip /data/vault/oriol/oriol_beacon_data/EGAD00001008392/genomicVariations.json.gz
	cp /data/vault/oriol/oriol_beacon_data/EGAD00001008392/genomicVariations.json data/caseLevelData/genomicVariations.json
	rm /data/vault/oriol/oriol_beacon_data/EGAD00001008392/genomicVariations.json
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/genomicVariations.json --collection genomicVariations
	docker exec beaconspreg python /beacon/connections/mongo/reindex.py	
	gunzip /data/vault/oriol/oriol_beacon_data/pop11_sub2/datasets.json.gz
	cp /data/vault/oriol/oriol_beacon_data/pop11_sub2/datasets.json data/caseLevelData/datasets.json
	rm /data/vault/oriol/oriol_beacon_data/pop11_sub2/datasets.json
	gunzip /data/vault/oriol/oriol_beacon_data/pop11_sub2/individuals.json.gz
	cp /data/vault/oriol/oriol_beacon_data/pop11_sub2/individuals.json data/caseLevelData/individuals.json
	rm /data/vault/oriol/oriol_beacon_data/pop11_sub2/individuals.json
	gunzip /data/vault/oriol/oriol_beacon_data/pop11_sub2/caseLevelData.json.gz
	cp /data/vault/oriol/oriol_beacon_data/pop11_sub2/caseLevelData.json data/caseLevelData/caseLevelData.json
	rm /data/vault/oriol/oriol_beacon_data/pop11_sub2/caseLevelData.json
	gunzip /data/vault/oriol/oriol_beacon_data/pop11_sub2/targets.json.gz
	cp /data/vault/oriol/oriol_beacon_data/pop11_sub2/targets.json data/caseLevelData/targets.json
	rm /data/vault/oriol/oriol_beacon_data/pop11_sub2/targets.json
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/datasets.json --collection datasets
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/individuals.json --collection individuals
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/caseLevelData.json --collection caseLevelData
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/targets.json --collection targets
	gunzip /data/vault/oriol/oriol_beacon_data/EGAD50000000314/analyses.json.gz
	cp /data/vault/oriol/oriol_beacon_data/EGAD50000000314/analyses.json data/caseLevelData/analyses.json
	rm /data/vault/oriol/oriol_beacon_data/EGAD50000000314/analyses.json
	gunzip /data/vault/oriol/oriol_beacon_data/EGAD50000000314/biosamples.json.gz
	cp /data/vault/oriol/oriol_beacon_data/EGAD50000000314/biosamples.json data/caseLevelData/biosamples.json
	rm /data/vault/oriol/oriol_beacon_data/EGAD50000000314/biosamples.json
	gunzip /data/vault/oriol/oriol_beacon_data/EGAD50000000314/cohorts.json.gz
	cp /data/vault/oriol/oriol_beacon_data/EGAD50000000314/cohorts.json data/caseLevelData/cohorts.json
	rm /data/vault/oriol/oriol_beacon_data/EGAD50000000314/cohorts.json
	gunzip /data/vault/oriol/oriol_beacon_data/EGAD50000000314/datasets.json.gz
	cp /data/vault/oriol/oriol_beacon_data/EGAD50000000314/datasets.json data/caseLevelData/datasets.json
	rm /data/vault/oriol/oriol_beacon_data/EGAD50000000314/datasets.json
	gunzip /data/vault/oriol/oriol_beacon_data/EGAD50000000314/individuals.json.gz
	cp /data/vault/oriol/oriol_beacon_data/EGAD50000000314/individuals.json data/caseLevelData/individuals.json
	rm /data/vault/oriol/oriol_beacon_data/EGAD50000000314/individuals.json
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/datasets.json --collection datasets
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/individuals.json --collection individuals
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/analyses.json --collection analyses
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/biosamples.json --collection biosamples
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/cohorts.json --collection cohorts
	gunzip /data/vault/oriol/oriol_beacon_data/EGAD00001008392/biosamples.json.gz
	cp /data/vault/oriol/oriol_beacon_data/EGAD00001008392/biosamples.json data/caseLevelData/biosamples.json
	rm /data/vault/oriol/oriol_beacon_data/EGAD00001008392/biosamples.json
	gunzip /data/vault/oriol/oriol_beacon_data/EGAD00001008392/cohorts.json.gz
	cp /data/vault/oriol/oriol_beacon_data/EGAD00001008392/cohorts.json data/caseLevelData/cohorts.json
	rm /data/vault/oriol/oriol_beacon_data/EGAD00001008392/cohorts.json
	gunzip /data/vault/oriol/oriol_beacon_data/EGAD00001008392/datasets.json.gz
	cp /data/vault/oriol/oriol_beacon_data/EGAD00001008392/datasets.json data/caseLevelData/datasets.json
	rm /data/vault/oriol/oriol_beacon_data/EGAD00001008392/datasets.json.gz
	gunzip /data/vault/oriol/oriol_beacon_data/EGAD00001008392/individuals.json.gz
	cp /data/vault/oriol/oriol_beacon_data/EGAD00001008392/individuals.json data/caseLevelData/individuals.json
	rm /data/vault/oriol/oriol_beacon_data/EGAD00001008392/individuals.json
	gunzip /data/vault/oriol/oriol_beacon_data/EGAD00001008392/runs.json.gz
	cp /data/vault/oriol/oriol_beacon_data/EGAD00001008392/runs.json data/caseLevelData/runs.json
	rm /data/vault/oriol/oriol_beacon_data/EGAD00001008392/runs.json
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
	rm -r data/caseLevelData