from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class Data_Ingestion_Config:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path
    
@dataclass(frozen = True)
class Data_Validation_Config:
    root_dir: Path
    unzip_dir: Path
    STATUS_FILE: str
    all_schema: dict
    
@dataclass(frozen=True)
class Data_Transformation_Config:
    root_dir: Path
    data_path: Path
    
@dataclass(frozen=True)
class Model_Trainer_Config:
    root_dir: Path
    train_path: Path
    test_path: Path
    params: dict
    target_column: str