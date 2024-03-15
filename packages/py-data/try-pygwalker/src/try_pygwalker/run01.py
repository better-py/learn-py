import os

import gradio as gr
import pandas as pd
from loguru import logger
from pygwalker.api.gradio import PYGWALKER_ROUTE, get_html_on_gradio

with gr.Blocks() as demo:
    logger.debug(f"{os.getcwd()}")

    df = pd.read_csv("https://kanaries-app.s3.ap-northeast-1.amazonaws.com/public-datasets/bike_sharing_dc.csv")

    # save csv file
    df.to_csv(f"{os.getcwd()}/tmp/gw_data.csv", index=False)

    filename = f"{os.getcwd()}/tmp/gw_config.json"
    if not os.path.exists(filename):
        # touch file
        # open(filename, 'a').close()
        os.makedirs(os.path.dirname(filename), exist_ok=True)

    pyg_html = get_html_on_gradio(df, spec=filename,
                                  spec_io_mode="rw")
    gr.HTML(pyg_html)

app = demo.launch(app_kwargs={
    "routes": [PYGWALKER_ROUTE]
})
