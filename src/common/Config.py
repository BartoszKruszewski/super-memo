from pathlib import Path


class Config:
    main_dir = Path(__file__)
    data_dir = main_dir / "data"
