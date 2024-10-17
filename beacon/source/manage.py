# Please, name the database as the folder's name inside the connections module.

analyses={
    'granularity': {
        'boolean': False,
        'count': False,
        'record': False
    },
    'singleEntryUrl': False,
    'endpoints': {
        'genomicVariant': False
    },
    'testMode': False,
    'database': 'mongo'
}
biosamples={
    'granularity': {
        'boolean': False,
        'count': False,
        'record': False
    },
    'singleEntryUrl': False,
    'endpoints': {
        'analysis': False,
        'genomicVariant': False,
        'run': False
    },
    'testMode': False,
    'database': 'mongo'
}
cohorts={
    'granularity': {
        'boolean': False,
        'count': False,
        'record': False
    },
    'singleEntryUrl': False,
    'endpoints': {
        'analysis': False,
        'individual': False,
        'run': False
    },
    'testMode': False,
    'database': 'mongo'
}
datasets={
    'granularity': {
        'boolean': True,
        'count': True,
        'record': True
    },
    'singleEntryUrl': True,
    'endpoints': {
        'analysis': False,
        'biosample': False,
        'genomicVariant': False,
        'individual': True,
        'run': False
    },
    'testMode': False,
    'database': 'mongo'
}
g_variants={
    'granularity': {
        'boolean': True,
        'count': True,
        'record': True
    },
    'singleEntryUrl': True,
    'endpoints': {
        'analysis': False,
        'biosample': False,
        'individual': False,
        'run': False
    },
    'testMode': False,
    'database': 'mongo'
}
individuals={
    'granularity': {
        'boolean': True,
        'count': True,
        'record': True
    },
    'singleEntryUrl': True,
    'endpoints': {
        'analysis': False,
        'biosample': False,
        'genomicVariant': False,
        'run': False
    },
    'testMode': False,
    'database': 'mongo'
}
runs={
    'granularity': {
        'boolean': False,
        'count': False,
        'record': False
    },
    'singleEntryUrl': False,
    'endpoints': {
        'analysis': False,
        'genomicVariant': False
    },
    'testMode': False,
    'database': 'mongo'
}
filtering_terms={
    'database': 'mongo'
}