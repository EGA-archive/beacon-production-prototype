docker-compose up -d --build beaconprod db
sleep 15s
cd beacon/connections/mongo/
make