# %%
from    pathlib             import  Path
from    monstry.Builder     import  Builder
from    monstry.DataCleaner import  DataCleaner

from dotenv import load_dotenv
import os
load_dotenv(dotenv_path=".sample_env")

# %%
def main():
    config_path =   "./config_files/entur_custom_config.json"
    builder     =   Builder(config_path=config_path)
    xroad_custom   = DataCleaner(builder , os.getenv("TABLE_NAME"))
    base_dir    =   Path("./")

    xroad_custom.__exactitud_funciones_config__(
        "./funciones_validacion/funciones_validacion.py",
        "./funciones_validacion/funciones_validacion_custom.py"
    )
    xroad_custom_resumen = xroad_custom.get_resumen()
    xroad_custom_resumen.iloc[::-1].set_index("COLUMNA")
    
    xroad_custom.to_csv_resumen_table(
        output_dir  =   os.getenv("OUTPUT_DIR") ,
        base_dir    =   base_dir,
        file_name   =   os.getenv("OUTPUT_FILE_NAME")
    )
    
    xroad_custom.total_score_gauge_save(
    output_dir  =   os.getenv("OUTPUT_DIR") ,
    base_dir    =   base_dir,
    file_name   =   os.getenv("OUTPUT_FILE_NAME")
    )

# %% [markdown]
# Run main process

# %%

if __name__ == "__main__":
    main()


