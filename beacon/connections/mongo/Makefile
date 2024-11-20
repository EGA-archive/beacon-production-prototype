build:
	zcat /data/landing/vault/oriol/oriol_beacon_data/pop11_sub2/gv_pop11_sub2_chr22.json.gz > data/caseLevelData/input
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/input --collection genomicVariations

	zcat /data/landing/vault/oriol/oriol_beacon_data/EGAD50000000314/genomicVariations.json.gz > data/caseLevelData/input
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/input --collection genomicVariations

	zcat /data/landing/vault/oriol/oriol_beacon_data/EGAD00001008392/genomicVariations.json.gz > data/caseLevelData/input
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/input --collection genomicVariations

	docker exec beaconspreg python /beacon/connections/mongo/reindex.py	

	zcat /data/landing/vault/oriol/oriol_beacon_data/pop11_sub2/datasets.json.gz > data/caseLevelData/input
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/input --collection datasets

	zcat /data/landing/vault/oriol/oriol_beacon_data/pop11_sub2/individuals.json.gz > data/caseLevelData/input
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/input --collection individuals

	zcat /data/landing/vault/oriol/oriol_beacon_data/pop11_sub2/caseLevelData.json.gz > data/caseLevelData/input
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/input --collection caseLevelData

	zcat /data/landing/vault/oriol/oriol_beacon_data/pop11_sub2/targets.json.gz > data/caseLevelData/input
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/input --collection targets

	zcat /data/landing/vault/oriol/oriol_beacon_data/EGAD50000000314/analyses.json.gz > data/caseLevelData/input
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/input --collection analyses

	zcat /data/landing/vault/oriol/oriol_beacon_data/EGAD50000000314/biosamples.json.gz > data/caseLevelData/input
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/input --collection biosamples

	zcat /data/landing/vault/oriol/oriol_beacon_data/EGAD50000000314/cohorts.json.gz > data/caseLevelData/input
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/input --collection cohorts

	zcat /data/landing/vault/oriol/oriol_beacon_data/EGAD50000000314/datasets.json.gz > data/caseLevelData/input
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/input --collection datasets

	zcat /data/landing/vault/oriol/oriol_beacon_data/EGAD50000000314/individuals.json.gz > data/caseLevelData/input
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/input --collection individuals

	zcat /data/landing/vault/oriol/oriol_beacon_data/EGAD00001008392/biosamples.json.gz > data/caseLevelData/input
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/input --collection biosamples

	zcat /data/landing/vault/oriol/oriol_beacon_data/EGAD00001008392/cohorts.json.gz > data/caseLevelData/input
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/input --collection cohorts

	zcat /data/landing/vault/oriol/oriol_beacon_data/EGAD00001008392/datasets.json.gz > data/caseLevelData/input
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/input --collection datasets

	zcat /data/landing/vault/oriol/oriol_beacon_data/EGAD00001008392/individuals.json.gz > data/caseLevelData/input
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/input --collection individuals

	zcat /data/landing/vault/oriol/oriol_beacon_data/EGAD00001008392/runs.json.gz > data/caseLevelData/input
	docker exec mongospreg mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27024/beacon?authSource=admin" --file data/caseLevelData/input --collection runs

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

	docker exec mongospreg /bin/bash -c 'mongo beacon -u root -p example -port 27024 --authenticationDatabase admin --eval "db.filtering_terms.insertMany([{\"type\": \"custom\", \"id\": \"diseases.diseaseCode:colorectal cancer\", \"scopes\": [\"individual\"]}])"'
	docker exec mongospreg /bin/bash -c 'mongo beacon -u root -p example -port 27024 --authenticationDatabase admin --eval "db.filtering_terms.insertMany([{\"type\": \"ontology\", \"id\": \"MONDO:0005575\", \"label\": \"colorectal cancer\", \"scopes\": [\"individual\"]}])"'
	docker exec mongospreg /bin/bash -c 'mongo beacon -u root -p example -port 27024 --authenticationDatabase admin --eval "db.synonyms.insertMany([{\"id\":\"DOID:9256\",\"synonym\":\"MONDO:0005575\"},{\"id\":\"ICD10:C18\",\"synonym\":\"MONDO:0005575\"},{\"id\":\"NCIT:C2955\",\"synonym\":\"MONDO:0005575\"}])"'