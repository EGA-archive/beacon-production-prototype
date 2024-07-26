from aiohttp.web_request import Request
import asyncio
from concurrent.futures import ThreadPoolExecutor
from beacon.response.granularity import build_beacon_boolean_response_by_dataset
from beacon.connections.beaconCLI.g_variants import get_variants
from beacon.logs.logs import log_with_args
from beacon.conf.conf import level

async def builder(request: Request, datasets, qparams):
    include = qparams.query.include_resultset_responses
    skip = qparams.query.pagination.skip
    limit = qparams.query.pagination.limit
    entry_id = request.match_info.get('id', None)
    if entry_id == None:
        entry_id = request.match_info.get('variantInternalId', None)
    datasets_docs={}
    datasets_count={}
    new_count=0
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        done, pending = await asyncio.wait(fs=[loop.run_in_executor(pool, get_variants, entry_id, qparams, dataset) for dataset in datasets],
        return_when=asyncio.ALL_COMPLETED
        )
    for task in done:
        entity_schema, count, dataset_count, records, dataset = task.result()
        if dataset_count != -1:
            new_count+=dataset_count
            datasets_docs[dataset]=records
            datasets_count[dataset]=dataset_count
    
    if include != 'NONE':
        count=new_count
    else:
        if limit == 0 or new_count < limit:
            pass
        else:
            count = limit
    
    response = build_beacon_boolean_response_by_dataset(datasets_docs, datasets_count, count, qparams, entity_schema)
    
            
    return response