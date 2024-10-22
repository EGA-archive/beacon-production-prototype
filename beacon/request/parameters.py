from typing_extensions import Self
from pydantic import (
    BaseModel,
    ValidationError,
    field_validator,
    Field,
    PrivateAttr
)
from strenum import StrEnum
from typing import List, Optional, Union
from beacon.conf.conf import api_version, default_beacon_granularity
from humps.main import camelize
from aiohttp.web_request import Request
from aiohttp import web
import html
import json
from beacon.logs.logs import log_with_args, LOG
from beacon.exceptions.exceptions import raise_exception
from beacon.request.classes import Granularity
from beacon.conf.conf import api_version, beacon_id 

class CamelModel(BaseModel):
    class Config:
        alias_generator = camelize
        allow_population_by_field_name = True


class IncludeResultsetResponses(StrEnum):
    ALL = "ALL",
    HIT = "HIT",
    MISS = "MISS",
    NONE = "NONE"


class Similarity(StrEnum):
    EXACT = "exact",
    HIGH = "high",
    MEDIUM = "medium",
    LOW = "low"


class Operator(StrEnum):
    EQUAL = "=",
    LESS = "<",
    GREATER = ">",
    NOT = "!",
    LESS_EQUAL = "<=",
    GREATER_EQUAL = ">="

class OntologyFilter(CamelModel):
    id: str
    scope: Optional[str] =None
    include_descendant_terms: bool = False
    similarity: Similarity = Similarity.EXACT


class AlphanumericFilter(CamelModel):
    id: str
    value: Union[str, int, List[int]]
    scope: Optional[str] =None
    operator: Operator = Operator.EQUAL


class CustomFilter(CamelModel):
    id: str
    scope: Optional[str] =None


class Pagination(CamelModel):
    skip: int = 0
    limit: int = 10


class RequestMeta(CamelModel):
    requested_schemas: List[str] = []
    api_version: str = api_version


class RequestQuery(CamelModel):
    filters: List[dict] = []
    include_resultset_responses: IncludeResultsetResponses = IncludeResultsetResponses.HIT
    pagination: Pagination = Pagination()
    request_parameters: Union[list,dict] = {}
    test_mode: bool = False
    requested_granularity: Granularity = Granularity(default_beacon_granularity)
    scope: str = None

class SequenceQuery(BaseModel):
    referenceName: Union[str,int]
    start: int
    alternateBases:str
    referenceBases: str
    clinicalRelevance: Optional[str] =None
    mateName: Optional[str] =None
    assemblyId: Optional[str] =None

class RangeQuery(BaseModel):
    referenceName: Union[str,int]
    start: int
    end: int
    variantType: Optional[str] =None
    alternateBases: Optional[str] =None
    aminoacidChange: Optional[str] =None
    variantMinLength: Optional[int] =None
    variantMaxLength: Optional[int] =None
    clinicalRelevance: Optional[str] =None
    mateName: Optional[str] =None
    assemblyId: Optional[str] =None

class DatasetsRequested(BaseModel):
    datasets: list

class GeneIdQuery(BaseModel):
    geneId: str
    variantType: Optional[str] =None
    alternateBases: Optional[str] =None
    aminoacidChange: Optional[str] =None
    variantMinLength: Optional[int] =None
    variantMaxLength: Optional[int] =None
    assemblyId: Optional[str] =None

class BracketQuery(BaseModel):
    referenceName: Union[str,int]
    start: list
    end: list
    variantType: Optional[str] =None
    clinicalRelevance: Optional[str] =None
    mateName: Optional[str] =None
    assemblyId: Optional[str] =None
    @field_validator('start')
    @classmethod
    def start_must_be_array_of_integers(cls, v: list) -> list:
        for num in v:# pragma: no cover
            if isinstance(num, int):
                pass
            else:
                raise ValueError
    @field_validator('end')
    @classmethod
    def end_must_be_array_of_integers(cls, v: list) -> list:
        for num in v:# pragma: no cover
            if isinstance(num, int):
                pass
            else:
                raise ValueError

class GenomicAlleleQuery(BaseModel):
    genomicAlleleShortForm: str
    assemblyId: Optional[str] =None

class AminoacidChangeQuery(BaseModel):
    aminoacidChange: str
    geneId: str
    assemblyId: Optional[str] =None

class RequestParams(CamelModel):
    meta: RequestMeta = RequestMeta()
    query: RequestQuery = RequestQuery()

    def from_request(self, request: Request) -> Self:
        request_params={}
        if request.method != "POST" or not request.has_body or not request.can_read_body:            
            for k, v in request.query.items():
                if k == "requestedSchema":# pragma: no cover
                    self.meta.requested_schemas = [html.escape(v)] # comprovar si és la sanitització recomanada
                elif k == "skip":# pragma: no cover
                    self.query.pagination.skip = int(html.escape(v))
                elif k == "limit":
                    self.query.pagination.limit = int(html.escape(v))
                elif k == "includeResultsetResponses":
                    self.query.include_resultset_responses = IncludeResultsetResponses(html.escape(v))
                elif k == 'datasets':
                    self.query.request_parameters[k] = html.escape(v)
                elif k == 'filters':
                    self.query.request_parameters[k] = html.escape(v)
                elif k in ["start", "end", "assemblyId", "referenceName", "referenceBases", "alternateBases", "variantType","variantMinLength","variantMaxLength","geneId","genomicAlleleShortForm","aminoacidChange","clinicalRelevance", "mateName"]:
                    try:
                        if ',' in v:# pragma: no cover
                            v_splitted = v.split(',')
                            request_params[k]=[int(v) for v in v_splitted]
                        else:
                            request_params[k]=int(v)
                    except Exception as e:
                        request_params[k]=v
                    self.query.request_parameters[k] = html.escape(v)
                else:
                    catch_req_params = {}
                    for k, v in request.query.items():
                        catch_req_params[k]=v
                    err = 'set of request parameters: {} not allowed'.format(catch_req_params)
                    errcode=400
                    raise_exception(err, errcode)
        if request_params != {}:
            try:
                RangeQuery(**request_params)
                return self
            except Exception as e:
                pass
            try:
                SequenceQuery(**request_params)
                return self# pragma: no cover
            except Exception as e:
                pass
            try:
                BracketQuery(**request_params)
                return self# pragma: no cover
            except Exception as e:
                pass
            try:
                GeneIdQuery(**request_params)
                return self# pragma: no cover
            except Exception as e:
                pass
            try:
                AminoacidChangeQuery(**request_params)
                return self# pragma: no cover
            except Exception as e:
                pass
            try:
                GenomicAlleleQuery(**request_params)
                return self# pragma: no cover
            except Exception as e:
                pass
            try:
                DatasetsRequested(**request_params)
                return self# pragma: no cover
            except Exception as e:
                pass
            err = 'set of request parameters: {} not allowed'.format(request_params)
            errcode=400
            raise_exception(err, errcode)
        return self

    def summary(self):
        try:
            list_of_filters=[]
            for item in self.query.filters:
                for k,v in item.items():
                    if v not in list_of_filters:
                        list_of_filters.append(html.escape(v))
            return {
                "apiVersion": self.meta.api_version,
                "requestedSchemas": self.meta.requested_schemas,
                "filters": list_of_filters,
                "requestParameters": self.query.request_parameters,
                "includeResultsetResponses": self.query.include_resultset_responses,
                "pagination": self.query.pagination.dict(),
                "requestedGranularity": self.query.requested_granularity,
                "testMode": self.query.test_mode
            }
        except Exception as e:# pragma: no cover
            err = str(e)
            errcode=500
            raise_exception(err, errcode)
