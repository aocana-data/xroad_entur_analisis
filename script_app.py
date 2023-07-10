# %%
from    pathlib             import  Path
from    monstry.Builder     import  Builder
from    monstry.DataCleaner import  DataCleaner

from dotenv import load_dotenv
import os
load_dotenv()

# %%
config_path =   "./entur_config.json"
builder     =   Builder(config_path=config_path)

# %%
xroad_default   = DataCleaner(builder , os.getenv("TABLE_NAME"))

# %%
resumen_default = xroad_default.get_resumen()
resumen_default.iloc[::-1]

# %%
base_dir    =   Path("./")

xroad_default.to_csv_resumen_table(
    output_dir  =   os.getenv("OUTPUT_DIR") ,
    base_dir    =   base_dir,
    file_name   =   os.getenv("OUTPUT_FILE_NAME")
)

# %%
xroad_default.total_score_gauge_save(
    output_dir  =   os.getenv("OUTPUT_DIR") ,
    base_dir    =   base_dir,
    file_name   =   os.getenv("OUTPUT_FILE_NAME")
)


