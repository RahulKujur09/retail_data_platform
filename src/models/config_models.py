from pydantic import BaseModel, Field


class SourceConfig(BaseModel):
    path: str
    format: str
    delimiter: str = ","
    header: bool = True


class DestinationConfig(BaseModel):
    path: str
    format: str
    mode: str = "overwrite"


class SchemaConfig(BaseModel):
    module: str
    variable: str


class QualityConfig(BaseModel):
    required_columns: list[str]
    key_columns: list[str] = Field(default_factory=list)


class PartitionConfig(BaseModel):
    enabled: bool = False
    columns: list[str] = Field(default_factory=list)

class TransformationConfig(BaseModel):
    module : str
    function : str


class DatasetConfig(BaseModel):
    source: SourceConfig
    destination: DestinationConfig
    schema: SchemaConfig | None = None
    quality: QualityConfig | None = None
    partition: PartitionConfig | None = None
    transformation : TransformationConfig | None = None

