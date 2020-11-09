FROM continuumio/miniconda3

COPY .. /peak_detection
WORKDIR ../peak_detection

COPY environment.yml .
RUN conda env create -f environment.yml

# Make RUN commands use the new environment:
SHELL ["conda", "run", "-n", "audiopeaks", "/bin/bash", "-c"]
RUN conda activate audiopeaks
RUN conda install -c conda-forge librosa
ENTRYPOINT ["conda", "run", "-n", "audiopeaks", "python", "app.py"]