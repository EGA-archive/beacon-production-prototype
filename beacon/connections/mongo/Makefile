build:
	docker exec mongoprod mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27017/beacon?authSource=admin" --file /data/GCAT/datasets.json --collection datasets
	docker exec mongoprod mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27017/beacon?authSource=admin" --file /data/GCAT/female_genomicVariations.json --collection genomicVariations
	docker exec mongoprod mongoimport --jsonArray --uri "mongodb://root:example@127.0.0.1:27017/beacon?authSource=admin" --file /data/GCAT/male_genomicVariations.json --collection genomicVariations
